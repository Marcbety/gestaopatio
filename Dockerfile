FROM python:3.11-slim

# Instala dependências de sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libopenblas-dev \
    liblapack-dev \
    gfortran \
    libffi-dev \
    pkg-config \
    && apt-get clean

# Cria diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala dependências do projeto
RUN pip install --upgrade pip setuptools wheel
RUN pip install numpy==1.26.4 --only-binary=:all:
RUN pip install -r requirements.txt

# Comando para iniciar o app
CMD ["gunicorn", "main:app"]
