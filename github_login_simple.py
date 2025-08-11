#!/usr/bin/env python3
"""
Script simples para gerar link de login do GitHub
"""

import webbrowser
from urllib.parse import urlencode

def generate_github_auth_link():
    """Gera o link de autorização do GitHub"""
    
    # Configurações básicas (você pode alterar estes valores)
    client_id = "YOUR_CLIENT_ID"  # Substitua pelo seu Client ID
    redirect_uri = "http://localhost:8080/callback"
    scope = "repo user"  # Permissões solicitadas
    
    # Parâmetros para o link de autorização
    params = {
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'scope': scope,
        'response_type': 'code',
        'state': 'login_state'
    }
    
    # Constrói a URL de autorização
    auth_url = f"https://github.com/login/oauth/authorize?{urlencode(params)}"
    
    return auth_url

def main():
    print("🔗 GitHub Login - Gerador de Link")
    print("="*40)
    
    # Gera o link
    auth_link = generate_github_auth_link()
    
    print(f"📋 Link de autorização gerado:")
    print(f"{auth_link}")
    
    print("\n⚠️  IMPORTANTE:")
    print("1. Configure seu CLIENT_ID no script")
    print("2. Crie um OAuth App em: https://github.com/settings/developers")
    print("3. Use o link acima para fazer login")
    
    # Pergunta se quer abrir o navegador
    try:
        open_browser = input("\n🌐 Abrir no navegador? (s/n): ").lower().strip()
        if open_browser in ['s', 'sim', 'y', 'yes']:
            webbrowser.open(auth_link)
            print("✅ Navegador aberto!")
        else:
            print("📋 Copie e cole o link no seu navegador")
    except KeyboardInterrupt:
        print("\n\n👋 Operação cancelada pelo usuário")
    
    print("\n📖 Próximos passos:")
    print("1. Clique no link de autorização")
    print("2. Faça login no GitHub")
    print("3. Autorize a aplicação")
    print("4. Copie o código de autorização da URL de redirecionamento")

if __name__ == "__main__":
    main()
