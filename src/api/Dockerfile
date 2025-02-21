# Usar a imagem oficial do Python 3.10 em versão slim como base
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /API

# Copiar o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências listadas no arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o conteúdo do diretório atual para o diretório de trabalho dentro do container
COPY . .

# Expor a porta 8000 para permitir o acesso ao serviço rodando no container
EXPOSE 8000

# Comando a ser executado quando o container iniciar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]