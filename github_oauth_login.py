#!/usr/bin/env python3
"""
Script para conectar ao GitHub usando OAuth
Gera um link de autorização externo para login
"""

import webbrowser
import requests
import json
from urllib.parse import urlencode
import os

class GitHubOAuth:
    def __init__(self):
        # Configurações do GitHub OAuth
        self.client_id = "YOUR_CLIENT_ID"  # Você precisa criar um OAuth App no GitHub
        self.client_secret = "YOUR_CLIENT_SECRET"  # Secreto do seu OAuth App
        self.redirect_uri = "http://localhost:8080/callback"  # URI de redirecionamento
        self.scope = "repo user"  # Escopos de permissão
        
        # URLs do GitHub
        self.auth_url = "https://github.com/login/oauth/authorize"
        self.token_url = "https://github.com/login/oauth/access_token"
        self.api_base = "https://api.github.com"
    
    def generate_auth_url(self):
        """Gera o URL de autorização OAuth"""
        params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'scope': self.scope,
            'response_type': 'code',
            'state': 'random_state_string'  # Para segurança
        }
        
        auth_url = f"{self.auth_url}?{urlencode(params)}"
        return auth_url
    
    def open_auth_browser(self):
        """Abre o navegador com o link de autorização"""
        auth_url = self.generate_auth_url()
        print(f"🔗 Abrindo link de autorização do GitHub...")
        print(f"📋 URL: {auth_url}")
        print("\n⚠️  IMPORTANTE: Configure seu CLIENT_ID e CLIENT_SECRET primeiro!")
        print("📖 Como configurar:")
        print("1. Vá para GitHub.com → Settings → Developer settings → OAuth Apps")
        print("2. Clique em 'New OAuth App'")
        print("3. Preencha as informações:")
        print("   - Application name: Nome da sua aplicação")
        print("   - Homepage URL: http://localhost:8080")
        print("   - Authorization callback URL: http://localhost:8080/callback")
        print("4. Copie o Client ID e Client Secret")
        print("5. Atualize este script com suas credenciais")
        
        # Abre o navegador automaticamente
        try:
            webbrowser.open(auth_url)
            print(f"\n✅ Navegador aberto com o link de autorização!")
        except Exception as e:
            print(f"\n❌ Erro ao abrir navegador: {e}")
            print(f"📋 Copie e cole este link no seu navegador: {auth_url}")
    
    def create_oauth_app_instructions(self):
        """Mostra instruções para criar um OAuth App"""
        print("\n" + "="*60)
        print("📋 INSTRUÇÕES PARA CRIAR OAUTH APP NO GITHUB")
        print("="*60)
        print("1. Acesse: https://github.com/settings/developers")
        print("2. Clique em 'OAuth Apps' → 'New OAuth App'")
        print("3. Preencha:")
        print("   - Application name: [Nome da sua app]")
        print("   - Homepage URL: http://localhost:8080")
        print("   - Authorization callback URL: http://localhost:8080/callback")
        print("4. Clique em 'Register application'")
        print("5. Copie o Client ID e Client Secret")
        print("6. Atualize as variáveis no script")
        print("="*60)

def main():
    print("🚀 GitHub OAuth Login Script")
    print("="*40)
    
    github_oauth = GitHubOAuth()
    
    # Verifica se as credenciais estão configuradas
    if github_oauth.client_id == "YOUR_CLIENT_ID":
        print("❌ Credenciais não configuradas!")
        github_oauth.create_oauth_app_instructions()
        print("\n🔧 Após configurar, execute o script novamente.")
        return
    
    # Gera e abre o link de autorização
    github_oauth.open_auth_browser()
    
    print("\n📝 Após autorizar no GitHub:")
    print("1. Você será redirecionado para localhost:8080/callback")
    print("2. Copie o código de autorização da URL")
    print("3. Use esse código para obter o token de acesso")

if __name__ == "__main__":
    main()
