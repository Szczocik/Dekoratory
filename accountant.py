import sys

ALLOWED_MODE = ('saldo', 'sprzedaz', 'zakup', 'konto', 'magazyn', 'przeglad')  # dozwolone komendy wejścia
ALLOWED_COMMANDS = ('saldo', 'zakup', 'sprzedaz', 'stop')  # dozwolone komendy w programie
mode = ALLOWED_MODE

saldo = None # poczatkowe saldo
store = {}  # MAGAZYN

file = open('baza_danych.txt', 'r')
for line in file.readlines():
    if 'saldo' in line:
        splitted_line = line.split(':')
        saldo = float(splitted_line[1])

    else:
        splitted_line = line.split(';')
        product_name = splitted_line[0]
        product_count = splitted_line[1]
        product_price = splitted_line[2]
        store[product_name] = {
            'count': int(product_count),
            'price': float(product_price),
        }

file.close()

mode = sys.argv[1]

logs = []  # historia operacji

while True:
    command = input("Wpisz rodzaj operacji (saldo, sprzedaz, zakup, stop): ")

    if command not in ALLOWED_COMMANDS:
        print("Niedozwolona komenda!")
        continue
    if command == 'stop':
        file = open('baza_danych.txt', 'w')
        file.write('saldo:' + str(saldo) + '\n')
        for product_name, data in store.items():
            file.write(str(product_name) + ';' + str(data['count']) + ';' + str(data['price']) + '\n')
        file.close()
        print("Koniec programu!")
        break

    if command == 'saldo':
        amount = float(input("Kwota wpłaty/wypłaty: "))
        if (amount < 0) and (saldo + amount < 0):
            print("Nie masz środków na koncie!")
            continue
        saldo += amount

        log = f"Zmiana saldo o: {amount}"
        logs.append(log)
    elif command == 'zakup':
        product_name = input(("Nazwa produktu: "))
        product_count = int(input("Ilość sztuk: "))
        product_price = float(input("Cena za sztukę: "))
        product_total_price = product_count * product_price
        if product_total_price > saldo:
            print(f"Cena za towary ({product_total_price}) przekracza wartość salda {saldo}")
            continue
        else:
            saldo -= product_total_price
            if not store.get(product_name):
                store[product_name] = {'count': product_count, 'price': product_price}
            else:
                store_product_count = store[product_name]['count']
                store[product_name] = {
                    'count': store_product_count+product_count,
                    'price': product_price}
        log = f"Dokonano zakupu produktu: {product_name} w ilości {product_count} sztuk, w cenie jednostkowej {product_price} zł."
        logs.append(log)
    elif command == 'sprzedaz':
        product_name = input(("Nazwa produktu: "))
        product_count = int(input("Ilość sztuk: "))
        product_price = float(input("Cena za sztukę: "))
        if not store.get(product_name):
            print("Produktu nie ma w magazynie!")
            continue
        if store.get(product_name)['count'] < product_count:
            print("Brak wystarczającej ilości towaru!")
            continue
        store[product_name] = {
            'count': store.get(product_name)['count'] - product_count,
            'price': product_price
        }
        saldo += product_count * product_price
        if not store.get(product_name)['count']:
            del store[product_name]

        log = f"Dokonano sprzedaży produktu: {product_name} w ilości {product_count} sztuk, o cenie jednostkowej {product_price}."
        logs.append(log)

if mode == 'sprzedaz':
    product_name = input(("Nazwa produktu: "))
    product_price = float(input("Cena za sztukę: "))
    product_count = int(input("Ilość sztuk: "))
    if not store.get(product_name):
        print("Produktu nie ma w magazynie!")
    if store.get(product_name)['count'] < product_count:
        print("Brak wystarczającej ilości towaru!")
    store[product_name] = {
        'count': store.get(product_name)['count'] - product_count,
        'price': product_price
    }
    saldo += product_count * product_price
    if not store.get(product_name)['count']:
        del store[product_name]
    print(f'Nazwa produktu: {product_name}, cena:{product_price}, ilość: {product_count}.')
elif mode == 'zakup':
    product_name = input(("Nazwa produktu: "))
    product_price = float(input("Cena za sztukę: "))
    product_count = int(input("Ilość sztuk: "))
    product_total_price = product_count * product_price
    if product_total_price > saldo:
        print(f"Cena za towary ({product_total_price}) przekracza wartość salda {saldo}")
    else:
        saldo -= product_total_price
        if not store.get(product_name):
            store[product_name] = {'count': product_count, 'price': product_price}
        else:
            store_product_count = store[product_name]['count']
            store[product_name] = {
                'count': store_product_count + product_count,
                'price': product_price}
    print(f'Nazwa produktu:{product_name}, cena: {product_price}, ilość: {product_count}.')
elif mode == 'saldo':
    amount = float(input("Kwota wpłaty/wypłaty: "))
    comment = input('Komentarz: ')
    if (amount < 0) and (saldo + amount < 0):
        print("Nie masz środków na koncie!")
    saldo += amount
    print(f'Kwota:{amount} {comment}.')
elif mode == 'konto':
    print(f'SALDO: {saldo}')
elif mode == 'magazyn':
    for key, value in store.items():
        print(f'Towar: {key}, ilość sztuk:', value.get('count'))
elif mode == 'przeglad':
    print(f'Historia operacji: {logs}.')
