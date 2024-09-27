FROM python:3.10-slim

WORKDIR /MVP Final

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app/app:$PYTHONPATH

# Copie apenas o requirements.txt inicialmente
COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos
COPY . .

# Exponha a porta que sua aplicação irá rodar
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "app/app.py"]
