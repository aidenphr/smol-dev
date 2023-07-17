# config.py

BASE_URL = "https://www.barcharts.com"

DATABASE_CONFIG = {
    'name': 'barcharts.db',
    'table': 'indices_data'
}

INDICES = ['COR3M', 'COR1M']

DOM_ELEMENT_IDS = {
    'COR3M': 'dom_id_for_cor3m',
    'COR1M': 'dom_id_for_cor1m'
}

LOGGING_CONFIG = {
    'filename': 'app.log',
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
}