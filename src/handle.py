
from services.instalers import Instalers
instalers = Instalers()

def main():
    senha = input("Digite a senha do root para continuar...")   

    comands ={
        "teams": instalers.make_teams,
        "git": instalers.make_git,
        "asdf": instalers.make_asdf,
        "ssocreds": instalers.make_ssocreds,
        "notepad": instalers.make_notepad,
        "postman": instalers.make_postman,
        "flameshot": instalers.make_flameshot,
        "vscode": instalers.make_vscode, 
        "pip": instalers.make_pip,
    }

    for name, func in comands.items():
        print(f"Instalando {name}...")
        func(senha)
        print(f"{name} instalado com sucesso!\n")

if __name__ == "__main__":
    main()