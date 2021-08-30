import xml.etree.ElementTree as xml
import datetime


def create_xml(data):
    root = xml.Element('order_list')

    for ele in data:
        date = datetime.datetime.fromtimestamp(ele['date_add']).strftime('%d.%m.%Y %H:%M:%S')
        subtotal = str(format(int(ele['payment_done']) - int(ele['delivery_price']), '.2f'))
        order = xml.Element('order')

        xml.SubElement(order, 'id').text = str(ele['order_id'])  # [numer_zamowienia]
        xml.SubElement(order, 'date').text = date  # [data_zakupu]
        xml.SubElement(order, 'notes')
        xml.SubElement(order, 'shipping_method').text = ele['delivery_method']  # [wysylka_nazwa]
        xml.SubElement(order, 'payment_method').text = ele['payment_method']  # [platnosc_nazwa]
        xml.SubElement(order, 'payment_surcharge').text = '0.00'  # 0.00
        xml.SubElement(order, 'total').text = str(format(ele['payment_done'], '.2f'))  # [wartosc_calkowita]
        xml.SubElement(order, 'subtotal').text = subtotal  # [wartosc_produktow]
        xml.SubElement(order, 'tax')
        xml.SubElement(order, 'shipping_cost').text = str(format(ele['delivery_price'], '.2f'))  # [wysylka_cena]

        customer_info = xml.SubElement(order, 'customer_info')
        xml.SubElement(customer_info, 'title')
        xml.SubElement(customer_info, 'email').text = ele['email']  # [klient_email]
        xml.SubElement(customer_info, 'first_name').text = ele['delivery_fullname']  # [dostawa_imie_nazwisko]
        xml.SubElement(customer_info, 'last_name').text = ele['delivery_fullname']  # [dostawa_imie_nazwisko]
        xml.SubElement(customer_info, 'phone').text = ele['phone']  # [klient_telefon]
        xml.SubElement(customer_info, 'adress').text = ele['delivery_address']  # [platnik_adres]
        xml.SubElement(customer_info, 'address_line2')
        xml.SubElement(customer_info, 'address_line3')
        xml.SubElement(customer_info, 'state')
        xml.SubElement(customer_info, 'country').text = 'PL'  # PL
        xml.SubElement(customer_info, 'zipcode').text = ele['delivery_postcode'] + ' ' + ele['delivery_city']  #
        # [platnik_kod_pocztowy] [platnik_miasto]

        billing_info = xml.SubElement(customer_info, 'billing_info')
        xml.SubElement(billing_info, 'title')
        xml.SubElement(billing_info, 'company_name').text = ele['delivery_company']  # [platnik_firma]
        xml.SubElement(billing_info, 'nip').text = ele['invoice_nip']  # [platnik_nip]
        xml.SubElement(billing_info, 'first_name').text = ele['delivery_fullname']  # [platnik_imie_nazwisko]
        xml.SubElement(billing_info, 'last_name').text = ' '  # " "
        xml.SubElement(billing_info, 'phone').text = ele['phone']  # [klient_telefon]
        xml.SubElement(billing_info, 'address').text = ele['delivery_address']  # [platnik_adres]
        xml.SubElement(billing_info, 'address_line2').text = ' '  # " "
        xml.SubElement(billing_info, 'address_line3')
        xml.SubElement(billing_info, 'city').text = ele['delivery_city']
        xml.SubElement(billing_info, 'state')
        xml.SubElement(billing_info, 'country').text = 'PL'  # PL
        xml.SubElement(billing_info, 'zipcode').text = ele['delivery_postcode']  # [platnik_kod_pocztowy]

        shipping_info = xml.SubElement(customer_info, 'shipping_info')
        xml.SubElement(shipping_info, 'title')
        xml.SubElement(shipping_info, 'company_name').text = ele['delivery_company']  # [platnik_firma]
        xml.SubElement(shipping_info, 'nip').text = ele['invoice_nip']  # [platnik_nip]
        xml.SubElement(shipping_info, 'first_name').text = ele['delivery_fullname']  # [platnik_imie_nazwisko]
        xml.SubElement(shipping_info, 'last_name').text = ' '  # " "
        xml.SubElement(shipping_info, 'phone').text = ele['phone']  # [klient_telefon]
        xml.SubElement(shipping_info, 'address').text = ele['delivery_address']  # [platnik_adres]
        xml.SubElement(shipping_info, 'address_line2').text = ' '  # " "
        xml.SubElement(shipping_info, 'address_line3')
        xml.SubElement(shipping_info, 'city').text = ele['delivery_city']  # [platnik_miasto]
        xml.SubElement(shipping_info, 'state')
        xml.SubElement(shipping_info, 'country').text = 'PL'  # PL
        xml.SubElement(shipping_info, 'zipcode').text = ele['delivery_postcode']  # [platnik_kod_pocztowy]

        order_items = xml.SubElement(order, 'order_items')
        for item in ele['products']:
            xml.SubElement(order_items, 'product_id').text = str(item['order_product_id'])  # [produkt_sku]
            xml.SubElement(order_items, 'product_ean').text = str(item['ean'])  # [produkt_ean]
            xml.SubElement(order_items, 'product_name').text = item['name']  # [produkt_nazwa]
            xml.SubElement(order_items, 'price').text = str(format(item['price_brutto'], '.2f'))  # [cena_brutto_szt]
            xml.SubElement(order_items, 'quantity').text = str(item['quantity'])  # [ilosc]

        root.append(order)

    tree = xml.ElementTree(root)

    with open(f'result.xml', 'wb') as file:
        tree.write(file)
