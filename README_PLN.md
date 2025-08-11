# 🧠 Processamento de Linguagem Natural (PLN)

Este repositório contém notebooks e projetos relacionados ao Processamento de Linguagem Natural, incluindo técnicas de análise de texto, extração de características e modelos de linguagem.

## 📚 Notebooks Incluídos

### 1. **spacy_pos_tagging_ner_.ipynb**
- **Técnicas**: Análise de Part-of-Speech (POS) e Named Entity Recognition (NER)
- **Ferramentas**: spaCy
- **Funcionalidades**: 
  - Tagging de partes do discurso
  - Identificação de entidades nomeadas
  - Análise sintática de textos

### 2. **tfidf_pdfs_google_drive.ipynb**
- **Técnicas**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Fonte de dados**: PDFs do Google Drive
- **Funcionalidades**:
  - Extração de texto de PDFs
  - Cálculo de TF-IDF
  - Análise de importância de termos

### 3. **Transformers_v.ipynb**
- **Técnicas**: Modelos Transformer
- **Ferramentas**: Hugging Face Transformers
- **Funcionalidades**:
  - Implementação de modelos BERT/GPT
  - Fine-tuning de modelos
  - Análise de embeddings

### 4. **PLN_DataAugmentation_GoogleTranslator.ipynb**
- **Técnicas**: Data Augmentation para PLN
- **Ferramentas**: Google Translator
- **Funcionalidades**:
  - Tradução automática para aumento de dados
  - Técnicas de augmentation de texto
  - Melhoria de datasets para treinamento

### 5. **Parafrase_OpenAI.ipynb**
- **Técnicas**: Parafraseamento de texto
- **Ferramentas**: OpenAI API
- **Funcionalidades**:
  - Geração de paráfrases
  - Análise de similaridade semântica
  - Aplicações em PLN

## 🚀 Como Usar

### Pré-requisitos
```bash
# Instalar dependências básicas
pip install jupyter notebook
pip install pandas numpy matplotlib seaborn

# Dependências específicas por notebook
pip install spacy  # Para spacy_pos_tagging_ner_.ipynb
pip install transformers torch  # Para Transformers_v.ipynb
pip install deep-translator  # Para PLN_DataAugmentation_GoogleTranslator.ipynb
pip install openai  # Para Parafrase_OpenAI.ipynb
```

### Executar os Notebooks
```bash
# Iniciar o Jupyter Notebook
jupyter notebook

# Ou usar Jupyter Lab
jupyter lab
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Jupyter Notebooks**
- **spaCy** - Processamento de linguagem natural
- **Transformers** - Modelos de linguagem
- **Google Translator API** - Tradução automática
- **OpenAI API** - Geração de texto
- **Pandas & NumPy** - Manipulação de dados
- **Matplotlib & Seaborn** - Visualização

## 📊 Aplicações

- **Análise de Sentimentos**
- **Classificação de Texto**
- **Extração de Informações**
- **Tradução Automática**
- **Geração de Texto**
- **Análise de Documentos**
- **Processamento de PDFs**

## 🔬 Áreas de Pesquisa

- **Machine Learning para PLN**
- **Deep Learning em Linguística**
- **Processamento de Texto em Português**
- **Análise de Redes Sociais**
- **Mineração de Texto**
- **Sistemas de Pergunta e Resposta**

## 📖 Recursos Adicionais

- [Documentação do spaCy](https://spacy.io/usage)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [Google Cloud Translation API](https://cloud.google.com/translate)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido para estudos e projetos de Processamento de Linguagem Natural.

---

**⭐ Se este repositório foi útil, considere dar uma estrela!**
