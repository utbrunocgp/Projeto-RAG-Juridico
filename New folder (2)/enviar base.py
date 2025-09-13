# ====== IMPORTS ======
import os
import re
import unicodedata
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain_community.vectorstores import Chroma
import chromadb

def normalizar_texto(texto):
    texto = unicodedata.normalize("NFKC", texto)

    # Remove caracteres de controle e não imprimíveis
    texto = re.sub(r"[\u200B-\u200D\uFEFF]", "", texto)  # zero-width
    texto = re.sub(r"[\r\n\t]+", " ", texto)             # quebras de linha/controle

    # Remove símbolos desnecessários, mas mantém os jurídicos relevantes
    texto = re.sub(r"[^0-9a-zA-ZÀ-ÿ.,;:/%§º°°\-\s]", " ", texto)

    # Normaliza múltiplos espaços
    texto = re.sub(r"\s{2,}", " ", texto).strip()

    return texto.lower()

def limpar_rodape(texto):
    return re.sub(r"Página \d+ de \d+", "", texto).strip()

# ====== CONFIGURAÇÕES ======
pasta_pdfs = "documentos"
splitter = TokenTextSplitter(
    encoding_name="cl100k_base",
    chunk_size=400,    # tamanho máximo de tokens por chunk
    chunk_overlap=100   # sobreposição de tokens
)

all_docs = []

# ====== CARREGAR E PROCESSAR PDFs ======
for nome_arquivo in os.listdir(pasta_pdfs):
    if nome_arquivo.endswith(".pdf"):
        caminho = os.path.join(pasta_pdfs, nome_arquivo)
        loader = PyPDFLoader(caminho)
        docs = loader.load_and_split()
        
        for doc in docs:
            pagina = doc.metadata.get("page", None)
            
            # Processa apenas páginas 1 e 2
            if pagina not in [0,1]:
                continue


            # Texto original e limpeza de rodapé
            texto_original = doc.page_content
            texto_limpo = limpar_rodape(texto_original)
            texto_normalizado = normalizar_texto(texto_limpo)
            
            # Divide em chunks de tokens
            chunks = splitter.split_text(texto_normalizado)
            
            for chunk in chunks:
                all_docs.append(Document(
                    page_content=chunk,           
                    metadata={
                        "arquivo": nome_arquivo,
                        "pagina": doc.metadata.get("page", None),
                        "original_text": texto_original
                    }
                ))
embeddings = OAIEmbeddings(modelo, chave)
client = chromadb.CloudClient()

vectorstore = Chroma.from_documents(
    documents=all_docs,
    embedding=embeddings,
    client=client,
    collection_name="contratos_juridicos"
)


retriever = vectorstore.as_retriever(
    search_type="similarity",
      search_kwargs={"k":3}
      )

pergunta = "temos contrato com o adriano?"
pergunta=normalizar_texto(pergunta)


resultado = retriever.get_relevant_documents(pergunta)
arquivos_encontrados = set([doc.metadata["arquivo"] for doc in resultado])
print("Documentos correspondentes:", arquivos_encontrados)