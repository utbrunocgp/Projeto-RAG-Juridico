# Sistema RAG 2.0 - Busca Inteligente em Documentos

Sistema de busca semântica em documentos PDF utilizando RAG (Retrieval-Augmented Generation) com Flask, Pinecone, LangChain e OpenAI.

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Usar](#como-usar)
- [API Endpoints](#api-endpoints)
- [Banco de Dados](#banco-de-dados)
- [Desenvolvimento](#desenvolvimento)
- [Troubleshooting](#troubleshooting)

## 🎯 Visão Geral

O Sistema RAG 2.0 é uma aplicação web que permite realizar buscas inteligentes em documentos PDF utilizando técnicas de processamento de linguagem natural. O sistema utiliza:

- **Busca Semântica**: Encontra documentos relevantes baseado no significado da consulta
- **RAG (Retrieval-Augmented Generation)**: Combina busca vetorial com geração de respostas usando IA
- **Interface Web Moderna**: Interface intuitiva estilo ChatGPT para interação com os documentos
- **Autenticação de Usuários**: Sistema de login com gerenciamento de sessões
- **Histórico e Documentos Salvos**: Rastreamento de documentos visualizados e salvos para comparação

## ✨ Funcionalidades

### 🔍 Busca e Consulta
- **Busca Semântica**: Busca inteligente em documentos PDF usando embeddings
- **Filtragem por Palavras-chave**: Filtra resultados baseado em palavras-chave relevantes
- **Ranking Inteligente**: Ordena resultados por relevância semântica
- **Visualização de Documentos**: Prévia de documentos PDF diretamente no navegador

### 💬 Perguntas e Respostas
- **Perguntas Específicas**: Faça perguntas sobre documentos específicos
- **Respostas Contextuais**: Respostas geradas baseadas no conteúdo dos documentos
- **Trechos Relevantes**: Exibe trechos do documento que fundamentam a resposta

### 📊 Comparação de Documentos
- **Comparação Múltipla**: Compare até 5 documentos simultaneamente
- **Análise Comparativa**: Análise automática destacando semelhanças e diferenças
- **Documentos Salvos**: Salve documentos para comparação posterior

### 📚 Gerenciamento
- **Histórico de Documentos**: Lista dos últimos documentos visualizados
- **Documentos Salvos**: Gerencie documentos salvos para comparação
- **Autenticação**: Sistema de login com sessões persistentes

## 🛠 Tecnologias Utilizadas

### Backend
- **Flask 3.1.2**: Framework web Python
- **LangChain**: Framework para aplicações com LLMs
- **Pinecone**: Banco de dados vetorial para armazenamento de embeddings
- **OpenAI**: API para embeddings e geração de respostas
- **SQLite**: Banco de dados relacional para usuários e metadados

### Frontend
- **Bootstrap 5.3.0**: Framework CSS
- **Font Awesome 6.0.0**: Ícones
- **JavaScript (Vanilla)**: Interatividade da interface

### Processamento
- **text-embedding-3-small**: Modelo de embeddings para busca
- **text-embedding-3-large**: Modelo de embeddings para perguntas específicas
- **gpt-4o-mini**: Modelo de linguagem para geração de respostas

## 📦 Pré-requisitos

- Python 3.8 ou superior
- Conta no Pinecone (https://www.pinecone.io/)
- Chave de API da OpenAI (https://platform.openai.com/)
- Git (opcional, para clonar o repositório)

## 🚀 Instalação

### 1. Clone o repositório (ou navegue até o diretório)

```bash
cd "C:\Projeto RAG 2.0\rag poo"
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

## ⚙️ Configuração

### 1. Crie um arquivo `.env` na raiz do projeto

Crie um arquivo chamado `.env` no diretório `rag poo` com o seguinte conteúdo:

```env
# OpenAI API Key
OPENAI_API_KEY=sua_chave_openai_aqui

# Pinecone Configuration
PINECONE_API_KEY=sua_chave_pinecone_aqui
PINECONE_ENVIRONMENT=seu_ambiente_pinecone_aqui
```

### 2. Configure os índices no Pinecone

O sistema utiliza dois índices no Pinecone:

- **`acharag`**: Índice principal para buscas (usa `text-embedding-3-small`)
- **`rag`**: Índice para perguntas específicas (usa `text-embedding-3-large`)

Certifique-se de que ambos os índices existem no seu projeto Pinecone.

### 3. Inicialize o banco de dados

O banco de dados será criado automaticamente na primeira execução. Para criar usuários:

```bash
python criar_usuarios.py
```

Siga as instruções para criar um novo usuário.

## 📁 Estrutura do Projeto

```
rag poo/
├── app/
│   ├── __init__.py              # Inicialização da aplicação Flask
│   ├── routes/                   # Rotas da aplicação
│   │   ├── __init__.py          # Registro de blueprints
│   │   ├── login_auth_routes.py # Autenticação (login/logout)
│   │   ├── main_page_routes.py  # Página principal
│   │   ├── procurar_documento_api.py # API de busca
│   │   ├── pergunta_no_documento.py  # Perguntas específicas
│   │   ├── previa_documento.py      # Visualização de documentos
│   │   ├── compra_documentos.py     # Comparação de documentos
│   │   ├── documentos_recentes.py   # Histórico de documentos
│   │   ├── documentos_salvos.py     # Documentos salvos
│   │   ├── status_api.py             # Status do sistema
│   │   └── dbug_documento.py         # Debug de documentos
│   ├── service/
│   │   └── apis_rag.py          # Inicialização do sistema RAG
│   ├── utils/
│   │   ├── decorator.py         # Decorators (login_required)
│   │   └── normalizar.py        # Normalização de texto
│   ├── templates/
│   │   ├── index.html           # Página principal
│   │   └── login.html           # Página de login
│   └── static/
│       └── documento/           # Arquivos PDF (190 documentos)
├── database.py                  # Gerenciamento do banco de dados
├── criar_usuarios.py            # Script para criar usuários
├── run.py                       # Ponto de entrada da aplicação
├── requirements.txt             # Dependências do projeto
└── rag_system.db                # Banco de dados SQLite (criado automaticamente)
```

## 🎮 Como Usar

### 1. Inicie o servidor

```bash
python run.py
```

Ou usando o launcher do Python no Windows:

```bash
py run.py
```

O servidor iniciará em `http://127.0.0.1:5000`

### 2. Acesse a aplicação

Abra seu navegador e acesse:
```
http://localhost:5000
```

### 3. Faça login

Use as credenciais de um usuário criado anteriormente.

### 4. Realize buscas

- Digite sua pergunta na barra de busca
- Clique em "Buscar" ou pressione Enter
- Visualize os resultados e clique nos documentos para ver detalhes

### 5. Faça perguntas específicas

- Clique em um documento nos resultados
- Clique em "Fazer Pergunta"
- Digite sua pergunta sobre o documento
- Receba uma resposta baseada no conteúdo

### 6. Compare documentos

- Salve documentos usando o botão "Salvar" nos resultados
- Clique em "Comparar Documentos"
- Selecione até 5 documentos salvos
- Digite uma pergunta para comparar
- Visualize a análise comparativa

## 🔌 API Endpoints

### Autenticação

#### `GET /login`
Página de login.

#### `POST /login`
Realiza login do usuário.

**Request Body:**
```json
{
  "email": "usuario@exemplo.com",
  "password": "senha123",
  "remember_me": false
}
```

**Response:**
```json
{
  "success": true,
  "message": "Login realizado com sucesso"
}
```

#### `POST /logout`
Realiza logout do usuário.

### Busca

#### `POST /search`
Realiza busca semântica em documentos.

**Request Body:**
```json
{
  "query": "contrato de associação"
}
```

**Response:**
```json
{
  "success": true,
  "documents": [
    {
      "arquivo": "documento.pdf",
      "score": 0.85,
      "pagina": 5,
      "palavras_encontradas": ["contrato", "associação"],
      "preview": "Trecho do documento..."
    }
  ],
  "query": "contrato de associação"
}
```

### Documentos

#### `POST /document-preview`
Obtém prévia de um documento.

**Request Body:**
```json
{
  "arquivo": "documento.pdf"
}
```

#### `POST /document-qa`
Faz pergunta específica sobre um documento.

**Request Body:**
```json
{
  "arquivo": "documento.pdf",
  "pergunta": "Qual é o valor do contrato?"
}
```

**Response:**
```json
{
  "success": true,
  "arquivo": "documento.pdf",
  "pergunta": "Qual é o valor do contrato?",
  "resposta": "Resposta gerada pela IA...",
  "documentos_relevantes": [
    {
      "pagina": 3,
      "conteudo": "Trecho relevante..."
    }
  ]
}
```

### Comparação

#### `POST /compare-documents`
Compara múltiplos documentos.

**Request Body:**
```json
{
  "arquivos": ["doc1.pdf", "doc2.pdf", "doc3.pdf"],
  "pergunta": "Quais são as diferenças nos valores?"
}
```

**Response:**
```json
{
  "success": true,
  "pergunta": "Quais são as diferenças nos valores?",
  "comparacao": [
    {
      "arquivo": "doc1.pdf",
      "resposta": "Resposta para doc1...",
      "documentos_relevantes": [...]
    }
  ],
  "analise_comparativa": "Análise comparativa completa..."
}
```

### Gerenciamento

#### `POST /track-document`
Registra visualização de documento no histórico.

#### `GET /list-documents`
Lista documentos recentes do usuário.

#### `POST /clear-recent-documents`
Limpa histórico de documentos recentes.

#### `GET /list-comparison-documents`
Lista documentos salvos para comparação.

#### `POST /save-for-comparison`
Salva documento para comparação.

#### `POST /remove-from-comparison`
Remove documento da lista de salvos.

### Sistema

#### `GET /status`
Verifica status do sistema RAG.

#### `GET /debug-documents`
Lista todos os documentos no sistema (debug).

## 💾 Banco de Dados

O sistema utiliza SQLite com três tabelas principais:

### Tabela `users`
Armazena informações dos usuários.

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_access TIMESTAMP,
    is_active INTEGER DEFAULT 1
)
```

### Tabela `saved_documents`
Armazena documentos salvos para comparação.

```sql
CREATE TABLE saved_documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    document_name TEXT NOT NULL,
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE(user_id, document_name)
)
```

### Tabela `recent_documents`
Armazena histórico de documentos visualizados.

```sql
CREATE TABLE recent_documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    document_name TEXT NOT NULL,
    accessed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
)
```

## 🔧 Desenvolvimento

### Modo Debug

O servidor roda em modo debug por padrão (`debug=True`). Isso permite:
- Recarregamento automático ao salvar arquivos
- Mensagens de erro detalhadas
- Debugger interativo

### Criando Novos Usuários

```bash
python criar_usuarios.py
```

### Estrutura de Rotas

As rotas são organizadas em blueprints Flask:

- `login_auth_bp`: Autenticação
- `main_page_bp`: Página principal
- `search_find_bp`: Busca
- `perguntar_documento_bp`: Perguntas específicas
- `previw_documento_bp`: Visualização
- `compara_documento_bp`: Comparação
- `documentos_recentes_bp`: Histórico
- `documentos_salvos_bp`: Documentos salvos
- `status_bp`: Status
- `debug_document_bp`: Debug

### Decorator de Autenticação

Todas as rotas protegidas usam o decorator `@login_required`:

```python
from app.utils.decorator import login_required

@route('/protegida')
@login_required
def rota_protegida():
    # Código da rota
    pass
```

## 🐛 Troubleshooting

### Erro: "Sistema RAG não inicializado"

**Causa**: O sistema RAG não foi inicializado corretamente.

**Solução**:
1. Verifique se as variáveis de ambiente estão configuradas no `.env`
2. Verifique se os índices do Pinecone existem
3. Verifique se as chaves de API estão corretas

### Erro: "Python não foi encontrado"

**Causa**: Python não está no PATH do sistema.

**Solução**:
- Use `py` ou `py -3` no Windows
- Ou adicione Python ao PATH do sistema

### Erro: "Email ou senha incorretos"

**Causa**: Credenciais inválidas ou usuário não existe.

**Solução**:
1. Verifique se o usuário foi criado: `python criar_usuarios.py`
2. Verifique se está usando o email correto
3. Verifique se a senha está correta

### Erro: "Documento não encontrado"

**Causa**: O documento não está no vectorstore do Pinecone.

**Solução**:
1. Verifique se o documento foi indexado no Pinecone
2. Verifique se está usando o nome correto do arquivo
3. Use `/debug-documents` para listar documentos disponíveis

### Servidor não inicia

**Causa**: Porta 5000 já está em uso ou dependências não instaladas.

**Solução**:
1. Feche outros processos usando a porta 5000
2. Instale as dependências: `pip install -r requirements.txt`
3. Verifique se todas as variáveis de ambiente estão configuradas

## 📝 Notas Importantes

- **Segurança**: As senhas são armazenadas como hash SHA-256. Nunca armazene senhas em texto plano.
- **Performance**: O sistema busca até 50 documentos e filtra para os 10 mais relevantes.
- **Limites**: 
  - Máximo de 5 documentos para comparação
  - Últimos 20 documentos no histórico por usuário
- **Modo Debug**: O servidor roda em modo debug por padrão. Para produção, configure um servidor WSGI adequado (Gunicorn, uWSGI, etc.).

## 📄 Licença

Este projeto é de uso interno. Todos os direitos reservados.

## 👥 Suporte

Para questões ou problemas:
1. Verifique a seção [Troubleshooting](#troubleshooting)
2. Verifique os logs do servidor
3. Consulte a documentação das APIs utilizadas (OpenAI, Pinecone, LangChain)

---

**Versão**: 2.0  
**Última atualização**: Dezembro 2025

