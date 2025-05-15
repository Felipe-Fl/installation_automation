# installation_automation

Automatize a instalação de ferramentas e dependências essenciais para ambientes de desenvolvimento Linux.

## Descrição

Este projeto tem como objetivo facilitar a configuração inicial de máquinas Linux para desenvolvedores, instalando automaticamente ferramentas como Git, ASDF, AWS SSO Credentials Helper, Notepad++, Postman, Flameshot, VSCode, pip e Teams for Linux.

## Como usar

### 1. Clone o repositório

```bash
git clone git@github.com:seu-usuario/installation_automation.git
cd installation_automation
```

### 2. (Opcional) Crie e ative um ambiente virtual

```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

### 3. Instale as dependências Python

```bash
pip install -r requirements.txt
```

### 4. Execute o script principal

```bash
python src/handle.py
```

Siga as instruções do terminal para informar a senha do sudo/root quando solicitado.

## Estrutura do Projeto

```
installation_automation/
│
├── src/
│   ├── handle.py
│   └── services/
│       ├── instalers.py
│       └── subprocess_service.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Observações

- Algumas ferramentas (como Postman e Notepad++) podem ser instaladas via Snap ou `.deb`. O script tenta usar o método mais adequado para cada ambiente.
- O uso do Snap em containers Docker pode não funcionar corretamente devido a limitações do kernel.
- Certifique-se de rodar o script em um terminal com permissões de sudo.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.


## Licença

Este projeto é distribuído para uso pessoal e acadêmico.