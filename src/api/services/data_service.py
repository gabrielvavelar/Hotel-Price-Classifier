def get_data(data):
    # Lista de campos que serão extraídos diretamente do objeto data
    direct_fields = [
        'no_of_adults',  # Número de adultos
        'no_of_children',  # Número de crianças
        'no_of_weekend_nights',  # Número de noites no final de semana
        'no_of_week_nights',  # Número de noites durante a semana
        'required_car_parking_space',  # Necessidade de estacionamento
        'lead_time',  # Tempo de antecedência da reserva
        'arrival_year',  # Ano de chegada
        'arrival_month',  # Mês de chegada
        'arrival_date',  # Data de chegada
        'no_of_special_requests'  # Número de pedidos especiais
    ]
    
    # Extrair os valores dos campos diretos do objeto data
    result = [getattr(data, field) for field in direct_fields]
    
    # Codificar o plano de refeições como variáveis dummy
    meal_plans = ['1', '2', '3', '0']
    result.extend([1 if data.type_of_meal_plan == plan else 0 for plan in meal_plans])
    
    # Codificar o tipo de quarto reservado como variáveis dummy
    room_types = ['1', '2', '3', '4', '5', '6', '7']
    result.extend([1 if data.room_type_reserved == room else 0 for room in room_types])
    
    # Codificar o segmento de mercado como variáveis dummy
    market_segments = ['Aviation', 'Complementary', 'Corporate', 'Offline', 'Online']
    result.extend([1 if data.market_segment_type == segment else 0 for segment in market_segments])
    
    # Retornar a lista de valores extraídos e codificados
    return result
