# 🚀 Instruções Rápidas para Upload no GitHub

## ✅ O que já foi feito

- ✅ Repositório Git local criado
- ✅ Todos os notebooks de PLN adicionados
- ✅ README detalhado criado
- ✅ Arquivo de licença MIT adicionado
- ✅ .gitignore configurado
- ✅ Primeiro commit realizado

## 🔗 Próximos passos para conectar ao GitHub

### 1. Criar repositório no GitHub

1. Acesse: https://github.com/new
2. Nome do repositório: `pln-notebooks` (ou outro nome de sua preferência)
3. Descrição: "Notebooks de Processamento de Linguagem Natural (PLN)"
4. **NÃO** inicialize com README (já temos um)
5. Clique em "Create repository"

### 2. Conectar repositório local ao GitHub

**Opção A: Usar o script automatizado**
```bash
python upload_to_github.py
```

**Opção B: Comandos manuais**
```bash
# Adicionar remote (substitua pela URL do seu repositório)
git remote add origin https://github.com/SEU-USUARIO/pln-notebooks.git

# Fazer push
git push -u origin master
```

### 3. Verificar se funcionou

- Acesse seu repositório no GitHub
- Todos os notebooks devem estar visíveis
- README deve estar formatado corretamente

## 📁 Estrutura do repositório

```
pln-notebooks/
├── README_PLN.md              # Documentação principal
├── LICENSE                    # Licença MIT
├── requirements_pln.txt       # Dependências para PLN
├── .gitignore                # Arquivos ignorados
├── spacy_pos_tagging_ner_.ipynb
├── tfidf_pdfs_google_drive.ipynb
├── Transformers_v.ipynb
├── PLN_DataAugmentation_GoogleTranslator.ipynb
├── Parafrase_OpenAI.ipynb
└── upload_to_github.py       # Script de upload
```

## 🔧 Comandos úteis

```bash
# Ver status
git status

# Ver remotes
git remote -v

# Ver commits
git log --oneline

# Fazer push de mudanças futuras
git add .
git commit -m "Descrição da mudança"
git push
```

## 🆘 Solução de problemas

### Erro: "remote origin already exists"
```bash
git remote remove origin
git remote add origin NOVA_URL
```

### Erro: "fatal: refusing to merge unrelated histories"
```bash
git pull origin master --allow-unrelated-histories
```

### Erro: "authentication failed"
- Verifique se está logado no GitHub
- Use token de acesso pessoal se necessário

## 🎯 Próximos passos após o upload

1. **Adicionar descrição** no repositório GitHub
2. **Configurar tópicos** (tags) para PLN, NLP, Python
3. **Adicionar colaboradores** se necessário
4. **Configurar GitHub Pages** para documentação
5. **Criar releases** para versões estáveis

---

**🎉 Seu repositório de PLN estará disponível no GitHub!**
