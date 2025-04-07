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

ENV PYENV_ROOT /home/vscode/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
RUN curl https://pyenv.run | bash

# Install mise
ENV MISE_DATA_DIR="/mise"
ENV MISE_CONFIG_DIR="/mise"
ENV MISE_CACHE_DIR="/mise/cache"
ENV MISE_INSTALL_PATH="/usr/local/bin/mise"
ENV PATH="/mise/shims:$PATH"
RUN curl https://mise.run | sh

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/