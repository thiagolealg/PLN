# 🔗 GitHub OAuth Login

Este projeto contém scripts para conectar ao GitHub usando OAuth e gerar links de autorização externos para login.

## 📁 Arquivos

- `github_oauth_login.py` - Script completo com classe OAuth
- `github_login_simple.py` - Script simples para gerar link
- `config.py` - Arquivo de configuração para credenciais
- `README.md` - Este arquivo de instruções

## 🚀 Como usar

### 1. Criar OAuth App no GitHub

1. Acesse: https://github.com/settings/developers
2. Clique em "OAuth Apps" → "New OAuth App"
3. Preencha as informações:
   - **Application name**: Nome da sua aplicação
   - **Homepage URL**: `http://localhost:8080`
   - **Authorization callback URL**: `http://localhost:8080/callback`
4. Clique em "Register application"
5. **Copie o Client ID e Client Secret**

### 2. Configurar credenciais

Edite o arquivo `config.py` ou os scripts e substitua:
```python
client_id = "YOUR_CLIENT_ID"  # Seu Client ID real
client_secret = "YOUR_CLIENT_SECRET"  # Seu Client Secret real
```

### 3. Executar o script

```bash
python github_login_simple.py
```

## 🔐 Como funciona

1. **Geração do link**: O script gera uma URL de autorização OAuth
2. **Autorização**: Você clica no link e autoriza no GitHub
3. **Callback**: GitHub redireciona para `localhost:8080/callback` com um código
4. **Token**: Use o código para obter um token de acesso

## 📋 Exemplo de link gerado

```
https://github.com/login/oauth/authorize?client_id=YOUR_ID&redirect_uri=http%3A//localhost%3A8080/callback&scope=repo+user&response_type=code&state=login_state
```

## ⚠️ Importante

- **Nunca compartilhe** seu Client Secret
- Use HTTPS em produção
- Configure corretamente as URLs de redirecionamento
- O estado (`state`) é importante para segurança

## 🛠️ Dependências

```bash
pip install requests
```

## 📚 Recursos adicionais

- [GitHub OAuth Documentation](https://docs.github.com/en/developers/apps/building-oauth-apps)
- [OAuth 2.0 RFC](https://tools.ietf.org/html/rfc6749)

## 🔧 Solução de problemas

### Erro: "Invalid client_id"
- Verifique se o Client ID está correto
- Confirme se o OAuth App foi criado corretamente

### Erro: "Redirect URI mismatch"
- Verifique se a URL de redirecionamento está configurada corretamente no GitHub
- Deve ser exatamente: `http://localhost:8080/callback`

### Link não abre no navegador
- Copie e cole o link manualmente no navegador
- Verifique se o Python tem permissão para abrir navegadores
