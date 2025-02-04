FROM python:3.9-slim-bookworm

LABEL MAINTAINER="Davide Rossotto <drossotto@crimson.ua.edu>"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install https://download.pytorch.org/whl/cpu/torch-1.13.1%2Bcpu-cp39-cp39-linux_x86_64.whl
RUN pip install torchaudio==0.13.1+cpu torchvision==0.14.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

RUN pip install torch-spline-conv==1.2.2+pt113cpu -f https://data.pyg.org/whl/torch-1.13.1+cpu.html


RUN pip install --no-cache-dir -r requirements.txt
RUN rm -rf requirements.txt

ARG CUDA=cpu

RUN pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-1.13.1+cpu.html

WORKDIR /app

COPY . .

WORKDIR /app/DeepGlycanSite

CMD ["bash"]

