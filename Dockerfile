
FROM python:3.11-slim

# Instala dependências de sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libopenblas-dev \
    liblapack-dev \
    gfortran \
    && apt-get clean

# Cria diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala dependências do projeto
RUN pip install --upgrade pip setuptools wheel
RUN pip install numpy==1.26.4 pandas==1.3.3
RUN pip install -r requirements.txt

# Comando para iniciar o app
CMD ["gunicorn", "main:app"]
