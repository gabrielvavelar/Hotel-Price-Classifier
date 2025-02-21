from fastapi import APIRouter, HTTPException
from models.prediction_model import HotelReservation
from services.model_service import get_model
from services.data_service import get_data

# Criar um roteador APIRouter para definir as rotas da API
router = APIRouter()

# Carregar o modelo de predição usando a função get_model
model = get_model()

# Definir a rota para a predição (POST /api/v1/predict)
@router.post('/api/v1/predict')
def root(data: HotelReservation): 
    try:
        # Fazer a predição usando o modelo e os dados fornecidos
        prediction = model.predict([get_data(data)])
        
        # Retornar a predição como um inteiro
        return {'prediction': int(prediction[0])}
    
    except Exception as e:
        # Em caso de erro, lançar uma exceção HTTP com uma mensagem de erro
        raise HTTPException(status_code=500, detail="Erro ao fazer a predição!")
