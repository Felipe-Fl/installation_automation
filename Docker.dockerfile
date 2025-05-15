# syntax=docker/dockerfile-upstream:master
FROM public.ecr.aws/docker/library/python:3.10-slim

ARG NAME
ENV NAME=${NAME/-/_}

WORKDIR /usr/src/app

# Instalar dependências necessárias
RUN apt-get update && apt-get install -y snapd sudo

# Criar um usuário não-root e definir uma senha
RUN useradd -m -s /bin/bash user && \
    echo "user:____" | chpasswd && \
    echo "user ALL=(ALL) ALL" >> /etc/sudoers

# Alternar para o usuário não-root
USER user

# Copiar o código fonte
COPY src/services /usr/src/app/services
COPY src/handle.py /usr/src/app/handle.py

# Definir o arquivo correto para execução
ENV COMMAND="/usr/src/app/handle.py"

CMD python3 ${COMMAND}

# docker build -t installation_automation -f Docker.dockerfile .
# docker run -it --rm installation_automation /bin/bash/