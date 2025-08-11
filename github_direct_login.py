#!/usr/bin/env python3
"""
Script para gerar links diretos de login do GitHub
Útil para acessar rapidamente sem configurar OAuth
"""

import webbrowser

def generate_direct_links():
    """Gera links diretos para o GitHub"""
    
    links = {
        "Login": "https://github.com/login",
        "Sign Up": "https://github.com/signup",
        "Settings": "https://github.com/settings",
        "Developer Settings": "https://github.com/settings/developers",
        "OAuth Apps": "https://github.com/settings/developers",
        "Personal Access Tokens": "https://github.com/settings/tokens",
        "SSH Keys": "https://github.com/settings/keys",
        "Profile": "https://github.com/settings/profile"
    }
    
    return links

def main():
    print("🔗 GitHub - Links Diretos de Acesso")
    print("="*50)
    
    links = generate_direct_links()
    
    print("📋 Links disponíveis:")
    for i, (name, url) in enumerate(links.items(), 1):
        print(f"{i:2d}. {name:<20} {url}")
    
    print("\n🌐 Escolha uma opção:")
    print("0. Sair")
    
    while True:
        try:
            choice = input("\nEscolha (0-8): ").strip()
            
            if choice == "0":
                print("👋 Até logo!")
                break
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(links):
                selected_name = list(links.keys())[choice_num - 1]
                selected_url = links[selected_name]
                
                print(f"\n🔗 Abrindo: {selected_name}")
                print(f"📋 URL: {selected_url}")
                
                # Abre no navegador
                webbrowser.open(selected_url)
                print("✅ Navegador aberto!")
                
                # Pergunta se quer continuar
                continue_choice = input("\nContinuar? (s/n): ").lower().strip()
                if continue_choice not in ['s', 'sim', 'y', 'yes']:
                    break
            else:
                print("❌ Opção inválida! Escolha de 0 a 8.")
                
        except ValueError:
            print("❌ Digite um número válido!")
        except KeyboardInterrupt:
            print("\n\n👋 Operação cancelada pelo usuário")
            break
    
    print("\n💡 Dica: Para usar OAuth completo, execute:")
    print("   python github_login_simple.py")

if __name__ == "__main__":
    main()
