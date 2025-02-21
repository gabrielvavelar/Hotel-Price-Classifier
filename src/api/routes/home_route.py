from fastapi import APIRouter

# Criar um roteador APIRouter para definir as rotas da API
router = APIRouter()

# Definir a rota raiz (/) da API
@router.get('/')
def root():
    # Retornar uma mensagem de boas-vindas
    return {"message": "Bem-vindo"}
