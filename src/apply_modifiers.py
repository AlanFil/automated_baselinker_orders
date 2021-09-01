
def apply_modifiers(data):
    for ele in data:

        if ele['delivery_method'] == 'Przesyłka kurierska pobranie':
            ele['delivery_method'] = 'DPD - Wysyłka za pobraniem'

        if ele['payment_method'] == 'Płatność przy odbiorze':
            ele['payment_method'] = 'Pobranie'

        if ele['delivery_method'] == 'Przesyłka kurierska':
            ele['delivery_method'] = 'DPD - Przedpłata'

        if ele['delivery_method'] == 'Przesyłka kurierska (DPD) Pobranie':
            ele['delivery_method'] = 'DPD - Wysyłka za pobraniem'

        if ele['delivery_method'] == 'Przesyłka kurierska (Geis) Pobranie':
            ele['delivery_method'] = 'DPD - Wysyłka za pobraniem'

        if ele['delivery_method'] == 'Odbiór w punkcie po przedpłacie - Allegro Paczkomaty 24/7 InPost':
            ele['delivery_method'] = 'DPD - Przedpłata'

        if ele['payment_method'] == 'Raty PayU':
            ele['payment_method'] = 'PayU'

        if ele['payment_method'] == 'za pobraniem':
            ele['payment_method'] = 'Pobranie'

        if ele['payment_method'] == 'Płatność kartą płatniczą':
            ele['payment_method'] = 'PayU'

        if ele['payment_method'] == 'DPD, Płatność przy odbiorze,Przesyłka kurierska pobraniowa':
            ele['payment_method'] = 'DPD - Wysyłka za pobraniem'

        if ele['delivery_method'] == 'DPD, Płatność z góry,Przesyłka kurierska':
            ele['delivery_method'] = 'DPD - Przedpłata'

        if ele['payment_method'] == 'PayU - szybka platność przelewem':
            ele['payment_method'] = 'PayU'

        if ele['delivery_method'] == 'DPD, Płatność przy odbiorze,Przesyłka kurierska pobraniowa':
            ele['delivery_method'] = 'DPD - Wysyłka za pobraniem'

        if ele['payment_method'] == 'Przelewy24':
            ele['payment_method'] = 'PayU'

        if ele['delivery_method'] == 'Allegro Paczkomaty 24/7 InPost':
            ele['delivery_method'] = 'DPD - Przedpłata'

        if ele['delivery_method'] == 'Kurier wieczór pobranie':
            ele['delivery_method'] = 'DPD - Wysyłka za pobraniem'

        if ele['delivery_method'] == 'Kurier wieczór':
            ele['delivery_method'] = 'DPD - Przedpłata'

        if ele['delivery_method'] == 'Kurier DHL pobranie':
            ele['delivery_method'] = 'DPD - Wysyłka za pobraniem'

        if ele['delivery_method'] == 'Kurier DHL':
            ele['delivery_method'] = 'DPD - Przedpłata'

        if ele['delivery_method'] == 'Paczkomaty InPost, Płatność z góry,Przesyłka':
            ele['delivery_method'] = 'DPD - Przedpłata'

        if ele['delivery_method'] == 'Allegro Kurier DPD':
            ele['delivery_method'] = 'DPD - Przedpłata'

        if ele['delivery_method'] == 'Allegro Kurier DPD pobranie':
            ele['delivery_method'] = 'DPD - Wysyłka za pobraniem'

        if ele['delivery_method'] == 'Paczkomaty InPost, Płatność z góry,Przesyłka':
            ele['delivery_method'] = 'DPD - Przedpłata'

        if ele['delivery_method'] == 'GEIS (K-EX) - Przedpłata':
            ele['delivery_method'] = 'Pobranie'

        if 'Paczkomaty' in ele['delivery_method']:
            ele['delivery_method'] = 'DPD - Przedpłata'

        if ele['payment_method'] == 'payu_account':
            ele['payment_method'] = 'PayU'

        if ele['payment_method'] == 'Przelew tradycyjny':
            ele['payment_method'] = 'Przelew'

        if ele['payment_method'] == 'DHL - Przedpłata':
            ele['payment_method'] = 'DPD - Przedpłata'

        if ele['payment_method'] == 'DHL - Przedplata':
            ele['payment_method'] = 'DPD - Przedpłata'

        if ele['payment_method'] == 'DHL - Wysyłka za pobraniem':
            ele['payment_method'] = 'DPD - Przedpłata'

        if ele['payment_method'] == 'Odbior osobisty - Odbior osobisty':
            ele['payment_method'] = 'Odbiór osobisty'

        if ele['payment_method'] == 'Odbior osobisty - Odbior osobisty':
            ele['payment_method'] = 'DPD - Przedpłata'

    return data
