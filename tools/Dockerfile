FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"

# --------------------------------------------------
# 1. Dépendances système
# --------------------------------------------------
RUN apt-get update && apt-get install -y \
    software-properties-common \
    git \
    curl \
    wget \
    ca-certificates \
    build-essential \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    net-tools \
    dnsutils \
    whois \
    nano \
    && rm -rf /var/lib/apt/lists/*

# --------------------------------------------------
# 2. Python 3.12
# --------------------------------------------------
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y \
    python3.12 \
    python3.12-venv \
    && rm -rf /var/lib/apt/lists/*

# --------------------------------------------------
# 3. pip + uv
# --------------------------------------------------
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12
RUN python3.12 -m pip install --upgrade pip setuptools wheel
RUN python3.12 -m pip install uv

# --------------------------------------------------
# 4. Installation de holehe via pip
# --------------------------------------------------
RUN python3.12 -m pip install holehe

# --------------------------------------------------
# 5. theHarvester dans /workspace avec uv
# --------------------------------------------------
WORKDIR /workspace

RUN git clone https://github.com/laramies/theHarvester.git && \
    cd theHarvester && \
    uv sync

# --------------------------------------------------
# 6. Commande par défaut
# --------------------------------------------------
CMD ["/bin/bash"]
