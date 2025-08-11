#!/usr/bin/env python3
"""
Script de instalação para o projeto GitHub OAuth Login
"""

import subprocess
import sys
import os

def install_requirements():
    """Instala as dependências do projeto"""
    print("📦 Instalando dependências...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def check_python_version():
    """Verifica a versão do Python"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print("❌ Python 3.6+ é necessário!")
        print(f"Versão atual: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detectado")
    return True

def create_config_template():
    """Cria um template de configuração"""
    config_content = '''# Configurações do GitHub OAuth
# Substitua pelos valores reais do seu OAuth App

GITHUB_CONFIG = {
    "client_id": "YOUR_CLIENT_ID_HERE",
    "client_secret": "YOUR_CLIENT_SECRET_HERE",
    "redirect_uri": "http://localhost:8080/callback",
    "scope": "repo user",
    "state": "random_security_string"
}

# URLs do GitHub
GITHUB_URLS = {
    "auth_url": "https://github.com/login/oauth/authorize",
    "token_url": "https://github.com/login/oauth/access_token",
    "api_base": "https://api.github.com"
}
'''
    
    if not os.path.exists("config.py"):
        with open("config.py", "w", encoding="utf-8") as f:
            f.write(config_content)
        print("✅ Arquivo config.py criado")
    else:
        print("ℹ️  Arquivo config.py já existe")

def main():
    print("🚀 Setup do GitHub OAuth Login")
    print("="*40)
    
    # Verifica versão do Python
    if not check_python_version():
        return
    
    # Instala dependências
    if not install_requirements():
        return
    
    # Cria template de configuração
    create_config_template()
    
    print("\n✅ Setup concluído com sucesso!")
    print("\n📖 Próximos passos:")
    print("1. Crie um OAuth App em: https://github.com/settings/developers")
    print("2. Configure suas credenciais no arquivo config.py")
    print("3. Execute: python github_login_simple.py")
    print("\n🔗 Para links diretos: python github_direct_login.py")

if __name__ == "__main__":
    main()
