import boto3
import joblib 
from io import BytesIO
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Criar uma sessão boto3
session = boto3.Session(
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token = os.getenv("AWS_SESSION_TOKEN"),
)
# Criar um cliente S3 a partir da sessão boto3
s3_client = session.client('s3')

def get_model(): 
    # Nome do bucket S3 onde o modelo está armazenado
    bucket_name = os.getenv("BUCKET_NAME")
    # Chave (caminho) do arquivo do modelo no Bucket S3
    key = 'Caminho para o modelo.joblib no Bucket S3'
    try:
        # Obter o objeto do S3
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        # Ler os bytes do corpo da resposta
        model_bytes = response['Body'].read()
        # Carregar o modelo a partir dos bytes usando joblib
        return joblib.load(BytesIO(model_bytes))
    
    except Exception as e:
        # Lançar uma exceção em caso de erro ao carregar o modelo do S3
        raise Exception("Erro ao carregar modelo do S3") from e