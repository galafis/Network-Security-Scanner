import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma-chave-secreta-muito-segura-e-aleatoria'
    # Outras configurações podem ser adicionadas aqui
    # Por exemplo, configurações de banco de dados, limites de taxa, etc.

