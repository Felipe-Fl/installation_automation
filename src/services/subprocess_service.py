import subprocess

class SubprocessService:
    def __init__(self):
        pass

    def run_command(self, command, senha=None):
        """
        Executes a shell command, optionally using sudo with a provided password.

        Args:
            command (str): The shell command to execute.
            senha (str, optional): The password to use for sudo. If provided, the command is executed with sudo privileges.

        Raises:
            subprocess.CalledProcessError: If the command returns a non-zero exit status.

        Prints:
            The command being executed and any errors encountered during execution.
        """
        try:
            print(f"Executando: {command}")
            if senha:
                # Passar a senha para o comando sudo
                process = subprocess.run(
                    f"echo {senha} | sudo -S {command}",
                    shell=True,
                    check=True,
                    text=True
                )
            else:
                # Executar o comando normalmente
                process = subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o comando: {command}\n{e}")

    def download_and_install_deb(self, url, output_path, senha):
        """
        Downloads a .deb package from the specified URL and installs it using dpkg, resolving dependencies if necessary.

        Args:
            url (str): The URL from which to download the .deb package.
            output_path (str): The local file path where the downloaded .deb package will be saved.
            senha (str): The sudo password required for installation commands.

        Raises:
            Exception: If any error occurs during the download or installation process.

        Side Effects:
            - Downloads a file from the internet.
            - Installs a .deb package on the system.
            - Attempts to fix broken dependencies using apt-get.
            - Prints status messages and errors to the console.
        """
        try:
            print(f"Baixando {url}...")
            self.run_command(f"wget -O {output_path} {url}")
            print(f"Instalando {output_path}...")
            self.run_command(f"sudo dpkg -i {output_path}", senha)
            self.run_command("sudo apt-get install -f -y", senha)  # Corrige dependências, se necessário
        except Exception as e:
            print(f"Erro ao baixar ou instalar o arquivo .deb: {e}")