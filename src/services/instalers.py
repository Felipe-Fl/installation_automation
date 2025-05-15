
from services.subprocess_service import SubprocessService


class Instalers:
    def __init__(self):
        self.process = SubprocessService()

    def make_teams (self, senha: str) -> None:
        """
        Installs the Teams for Linux application using the Snap package manager.

        Args:
            senha (str): The sudo password required to execute the installation command.

        Raises:
            Exception: If an error occurs during the installation process, it is caught and an error message is printed.
        """
        try:
            print("Instalando o Teams...")
            self.process.run_command("sudo snap install teams-for-linux", senha)            
        except Exception as e:
            print(f"Erro ao instalar o Teams: {e}")

    def make_git (self, senha: str) -> None:
        """
        Installs Git using the system's package manager.

        Args:
            senha (str): The sudo password required to execute the installation command.

        Raises:
            Exception: If an error occurs during the installation process.

        Side Effects:
            Prints status messages to the console regarding the installation progress or errors.
        """
        try:
            print("Instalando o Git...")        
            self.process.run_command("sudo apt-get install -y git-all", senha )            
        except Exception as e:
            print(f"Erro ao instalar o Git: {e}")

    def make_asdf (self, senha: str) -> None:      
        """
        Installs and configures ASDF version manager along with its dependencies and several plugins.
        This method performs the following steps:
            1. Updates the system's package list and installs required build dependencies.
            2. Clones the ASDF repository into the user's home directory and updates the shell configuration.
            3. Installs and configures the following ASDF plugins and tools:
                - awscli (latest version)
                - nodejs (version 20.5.1)
                - serverless (version 3.34.0)
                - python (versions 3.8.18, 3.10.12, and latest, setting 3.10.12 as global)
        Args:
            senha (str): The sudo password required for running privileged commands.
        Raises:
            Exception: If any step in the installation process fails.
        """
        try:
            print("ASDF...")           
            print("Instalando dependências do ASDF...")            
            self.process.run_command("sudo apt-get update", senha)
            self.process.run_command(
                "sudo apt-get install -y build-essential libssl-dev zlib1g-dev "
                "libbz2-dev libreadline-dev libsqlite3-dev curl git "
                "libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev", senha
            )

            print("Clonando o repositório do ASDF...")
            self.process.run_command("git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.15.0")
            self.process.run_command('echo \'. "$HOME/.asdf/asdf.sh"\' >> ~/.bashrc')
            self.process.run_command('echo \'. "$HOME/.asdf/completions/asdf.bash"\' >> ~/.bashrc')
            
                       
            print("Instalando plugins do ASDF...")
            asdf_cmd = '. $HOME/.asdf/asdf.sh &&'
            self.process.run_command(f"{asdf_cmd} asdf plugin add awscli")
            self.process.run_command(f"{asdf_cmd} asdf install awscli latest")
            self.process.run_command(f"{asdf_cmd} asdf global awscli latest")
            self.process.run_command(f"{asdf_cmd} asdf plugin add nodejs")
            self.process.run_command(f"{asdf_cmd} asdf install nodejs 20.5.1")
            self.process.run_command(f"{asdf_cmd} asdf global nodejs 20.5.1")
            self.process.run_command(f"{asdf_cmd} asdf plugin add serverless")
            self.process.run_command(f"{asdf_cmd} asdf install serverless 3.34.0")
            self.process.run_command(f"{asdf_cmd} asdf global serverless 3.34.0")
            self.process.run_command(f"{asdf_cmd} asdf plugin-add python")
            self.process.run_command(f"{asdf_cmd} asdf install python 3.8.18")
            self.process.run_command(f"{asdf_cmd} asdf install python 3.10.12")
            self.process.run_command(f"{asdf_cmd} asdf install python latest")
            self.process.run_command(f"{asdf_cmd} asdf global python 3.10.12")            
        except Exception as e:
            print(f"Erro ao instalar o ASDF: {e}")

    def make_ssocreds (self, senha: str) -> None:
        """
        Installs the AWS SSO Credentials Helper (aws-sso-creds-helper) using npm.

        This method attempts to install the required npm package for AWS SSO credentials
        management. It first ensures that npm is installed via apt-get, then installs
        the aws-sso-creds-helper globally using npm. Both commands are executed with
        elevated privileges using the provided password.

        Args:
            senha (str): The sudo password required to execute privileged commands.

        Raises:
            Prints an error message if installation fails.
        """
        try:
            print("Instalando o SSOCREDS...")
            self.process.run_command("sudo apt-get install -y npm", senha)
            self.process.run_command("npm install -g aws-sso-creds-helper", senha)
        except Exception as e:
            print(f"Erro ao instalar o SSOCREDS: {e}")

    def make_notepad (self, senha: str) -> None:
        """
        Installs Notepad++ using snap on a Linux system.

        This method attempts to install the required 'snapd' package and then installs Notepad++ 
        via the snap package manager. It uses the provided password to execute commands with sudo privileges.

        Args:
            senha (str): The sudo password required to execute installation commands.

        Raises:
            Prints an error message if installation fails.
        """
        try:
            print("Instalando o Notepad++...")
            self.process.run_command("sudo apt-get install -y snapd", senha)
            self.process.run_command("sudo snap install notepad-plus-plus", senha)
        except Exception as e:
            print(f"Erro ao instalar o Notepad++: {e}")        

    def make_postman (self, senha: str) -> None:
        """
        Installs the Postman application using the Snap package manager.

        Args:
            senha (str): The sudo password required to execute the installation command.

        Raises:
            Exception: If an error occurs during the installation process.

        Side Effects:
            Prints status messages to the console regarding the installation progress and errors.
        """
        try:
            print("Instalando o Postman...")
            self.process.run_command("sudo snap install postman", senha)
        except Exception as e:
            print(f"Erro ao instalar o Postman: {e}")        
    
    def make_flameshot (self, senha: str) -> None:
        """
        Installs the Flameshot screenshot tool using the system's package manager.

        Args:
            senha (str): The sudo password required to execute the installation command.

        Raises:
            Exception: If an error occurs during the installation process.

        Side Effects:
            Prints status messages to the console regarding the installation progress or errors.
        """
        try:
            print("Instalando o Flameshot...")
            self.process.run_command("sudo apt install -y flameshot", senha)
        except Exception as e:
            print(f"Erro ao instalar o Flameshot: {e}")        

    def make_vscode (self, senha: str) -> None:
        """
        Downloads and installs Visual Studio Code on a Linux system using a .deb package.

        Args:
            senha (str): The sudo password required for installation commands.

        Raises:
            Exception: If any error occurs during the download or installation process.

        Side Effects:
            - Downloads the VSCode .deb package to /tmp/vscode.deb.
            - Installs the package using sudo privileges.
            - Attempts to fix broken dependencies with 'apt-get install -f -y'.
            - Prints status and error messages to the console.
        """
        try:
            print("Instalando o VSCode...")
            vscode_url = "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
            self.process.download_and_install_deb(vscode_url, "/tmp/vscode.deb", senha)
            self.process.run_command("sudo apt-get install -f -y", senha)    
        except Exception as e:
            print(f"Erro ao instalar o VSCode: {e}")        

    def make_pip (self, senha: str) -> None:
        """
        Installs Python's pip package manager and configures trusted hosts for pip.

        Args:
            senha (str): The sudo password required to execute installation commands.

        Raises:
            Exception: If any error occurs during the installation or configuration process.

        This method attempts to install pip using apt-get and then sets trusted hosts for pip to avoid SSL verification issues when installing packages.
        """
        try:
            print("Instalando o PIP...")
            self.process.run_command("sudo apt-get install -y python3-pip", senha)
            self.process.run_command("pip config set global.trusted-host pypi.org", senha)
            self.process.run_command("pip config set global.trusted-host files.pythonhosted.org", senha)
            self.process.run_command("pip config set global.trusted-host pypi.python.org", senha)
        except Exception as e:
            print(f"Erro ao instalar o PIP: {e}")
        