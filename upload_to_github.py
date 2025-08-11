#!/usr/bin/env python3
"""
Script para facilitar o upload do repositório PLN para o GitHub
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Executa um comando e mostra o resultado"""
    print(f"\n🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} concluído com sucesso!")
            if result.stdout:
                print(f"📋 Saída: {result.stdout.strip()}")
        else:
            print(f"❌ Erro em {description}: {result.stderr.strip()}")
            return False
        return True
    except Exception as e:
        print(f"❌ Erro ao executar comando: {e}")
        return False

def setup_github_remote():
    """Configura o repositório remoto do GitHub"""
    print("🚀 Configurando repositório remoto do GitHub")
    print("="*50)
    
    # Verifica se já existe um remote
    result = subprocess.run("git remote -v", shell=True, capture_output=True, text=True)
    if "origin" in result.stdout:
        print("ℹ️  Remote 'origin' já configurado")
        return True
    
    # Solicita a URL do repositório
    print("\n📋 Para conectar ao GitHub, você precisa:")
    print("1. Criar um repositório em https://github.com/new")
    print("2. Copiar a URL do repositório (ex: https://github.com/seu-usuario/pln-notebooks.git)")
    
    repo_url = input("\n🔗 Cole a URL do seu repositório GitHub: ").strip()
    
    if not repo_url:
        print("❌ URL não fornecida. Operação cancelada.")
        return False
    
    # Adiciona o remote
    if run_command(f'git remote add origin "{repo_url}"', "Adicionando remote origin"):
        print(f"✅ Repositório remoto configurado: {repo_url}")
        return True
    
    return False

def push_to_github():
    """Faz push para o GitHub"""
    print("\n📤 Fazendo push para o GitHub...")
    print("="*40)
    
    # Verifica se o remote está configurado
    result = subprocess.run("git remote -v", shell=True, capture_output=True, text=True)
    if "origin" not in result.stdout:
        print("❌ Remote 'origin' não configurado. Execute setup_github_remote() primeiro.")
        return False
    
    # Faz push
    if run_command("git push -u origin master", "Push para o GitHub"):
        print("🎉 Repositório enviado para o GitHub com sucesso!")
        return True
    
    return False

def show_status():
    """Mostra o status atual do repositório"""
    print("\n📊 Status do Repositório")
    print("="*30)
    
    # Status do Git
    run_command("git status", "Verificando status do Git")
    
    # Branches
    run_command("git branch -a", "Listando branches")
    
    # Remotes
    run_command("git remote -v", "Listando remotes")

def main():
    print("🚀 Upload para GitHub - Repositório PLN")
    print("="*50)
    
    while True:
        print("\n📋 Opções disponíveis:")
        print("1. Configurar repositório remoto")
        print("2. Fazer push para GitHub")
        print("3. Ver status do repositório")
        print("4. Sair")
        
        try:
            choice = input("\nEscolha uma opção (1-4): ").strip()
            
            if choice == "1":
                setup_github_remote()
            elif choice == "2":
                push_to_github()
            elif choice == "3":
                show_status()
            elif choice == "4":
                print("👋 Até logo!")
                break
            else:
                print("❌ Opção inválida! Escolha de 1 a 4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Operação cancelada pelo usuário")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main()
