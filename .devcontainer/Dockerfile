FROM mcr.microsoft.com/vscode/devcontainers/base:0-buster

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
        python-openssl \
    && rm -rf /var/lib/apt/lists/*
ENV PYENV_ROOT /home/vscode/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH

# Install mise
RUN curl https://mise.run | sh

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
