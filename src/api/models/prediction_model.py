from pydantic import BaseModel

# Definir um modelo Pydantic para representar uma reserva de hotel
class HotelReservation(BaseModel):
    no_of_adults: int  # Número de adultos
    no_of_children: int  # Número de crianças
    no_of_weekend_nights: int  # Número de noites no final de semana
    no_of_week_nights: int  # Número de noites durante a semana
    required_car_parking_space: bool = True or False  # Necessidade de estacionamento (Verdadeiro ou Falso)
    lead_time: int  # Tempo de antecedência da reserva
    arrival_year: int  # Ano de chegada
    arrival_month: int  # Mês de chegada
    arrival_date: int  # Data de chegada
    no_of_special_requests: int  # Número de pedidos especiais
    type_of_meal_plan: str = "(0-3)"  # Tipo de plano de refeição (0 a 3)
    room_type_reserved: str = "(1-7)"  # Tipo de quarto reservado (1 a 7)
    market_segment_type: str = "(Aviation, Complementary, Corporate, Offline, Online)"  # Segmento de mercado (Aviation, Complementary, Corporate, Offline, Online)

