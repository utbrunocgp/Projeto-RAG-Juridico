# Projeto-RAG-Juridico
# 🤖 Projeto RAG Jurídico

## 📋 Descrição

Sistema de **Retrieval-Augmented Generation (RAG)** especializado em documentos jurídicos, desenvolvido para auxiliar profissionais do direito na busca e análise de informações legais de forma inteligente e eficiente.

## ✨ Funcionalidades

- 🔍 **Busca Inteligente**: Pesquisa semântica em documentos jurídicos
- 📚 **Base de Conhecimento**: Integração com códigos, leis e jurisprudência
- 💬 **Chat Jurídico**: Interface conversacional para consultas legais
- 📊 **Análise de Documentos**: Extração e análise automática de informações
- 🔗 **Citações Automáticas**: Referências precisas a fontes legais
- 📱 **Interface Web**: Acesso via navegador com design responsivo

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python, FastAPI
- **IA/ML**: LangChain, OpenAI GPT, Embeddings
- **Frontend**: React.js, TypeScript
- **Banco de Dados**: PostgreSQL, Vector Database
- **Deploy**: Docker, AWS/Azure

## 🚀 Como Usar

### Pré-requisitos

```bash
# Python 3.8+
python --version

# Node.js 16+
node --version

# Docker (opcional)
docker --version
```

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/utbrunocgp/Projeto-RAG-Juridico.git
cd Projeto-RAG-Juridico
```

2. **Configure o ambiente Python**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

4. **Execute o projeto**
```bash
# Backend
python app/main.py

# Frontend (em outro terminal)
cd frontend
npm install
npm start
```

## 📁 Estrutura do Projeto

```
Projeto-RAG-Juridico/
├── app/                    # Backend FastAPI
│   ├── main.py
│   ├── models/
│   ├── services/
│   └── utils/
├── frontend/              # Frontend React
│   ├── src/
│   ├── public/
│   └── package.json
├── data/                  # Documentos jurídicos
├── docs/                  # Documentação
├── tests/                 # Testes automatizados
└── docker/               # Configurações Docker
```

## 🔧 Configuração

### Variáveis de Ambiente

```env
# OpenAI
OPENAI_API_KEY=sua_chave_aqui

# Banco de Dados
DATABASE_URL=postgresql://user:pass@localhost/rag_juridico

# Configurações da Aplicação
DEBUG=True
SECRET_KEY=sua_chave_secreta
```

## 📚 Documentação

- [Guia de Instalação](docs/instalacao.md)
- [API Reference](docs/api.md)
- [Contribuição](docs/contribuicao.md)
- [FAQ](docs/faq.md)

## 🤝 Como Contribuir

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- **Bruno Costa** - [@utbrunocgp](https://github.com/utbrunocgp)

## 🙏 Agradecimentos

- Comunidade open source
- Contribuidores do projeto
- Profissionais do direito que testaram o sistema

## 📞 Contato

- Email: bruno.costa@exemplo.com
- LinkedIn: [Bruno Costa](https://linkedin.com/in/brunocosta)
- Twitter: [@utbrunocgp](https://twitter.com/utbrunocgp)

---

⭐ **Se este projeto te ajudou, considere dar uma estrela!** 
