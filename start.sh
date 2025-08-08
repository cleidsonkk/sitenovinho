#!/usr/bin/env bash

# Ativar o ambiente virtual (se existir)
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Instalar dependências
pip install -r requirements.txt

# Executar a aplicação Flask
python3 src/main.py


