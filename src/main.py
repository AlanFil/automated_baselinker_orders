from src.apply_modifiers import apply_modifiers
from src.create_xml import create_xml
from src.download_orders import download_orders

if __name__ == '__main__':
    orders = download_orders()

    data = apply_modifiers(orders['orders'])

    create_xml(orders['orders'])

