FROM mcr.microsoft.com/vscode/devcontainers/base:debian
# Install pyenv
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    git \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libffi-dev \
    liblzma-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYENV_ROOT=/home/vscode/.pyenv
ENV PATH=$PYENV_ROOT/bin:$PATH
RUN curl https://pyenv.run | bash


# Configure poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true