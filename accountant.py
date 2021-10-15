
class Manager:
    def __init__(self):
        self.actions = {}
        self.saldo = None
        self.logs = []
        self.store = {}

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb
        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name]()

    def read_file(self, filepath='baza_danych.txt'):
        file = open(filepath, 'r')
        for line in file.readlines():
            if 'saldo' in line:
                splitted_line = line.split(';')
                self.saldo = float(splitted_line[1])
            else:
                splitted_line = line.split(';')
                product_name = splitted_line[0]
                product_count = splitted_line[1]
                product_price = splitted_line[2]
                self.store[product_name] = {
                    'count': int(product_count),
                    'price': float(product_price),
                }
        file.close()

    def write_file(self, filepath='baza_danych.txt'):
        with open(filepath, 'w') as file:
            file.write('saldo;' + str(self.saldo) + '\n')
            for product_name, data in self.store.items():
                file.write(str(product_name) + ';' + str(data['count']) + ';' + str(data['price']) + '\n')
            print("Koniec programu!")

    def logs_read_file(self, filepath='logs.txt'):
        with open(filepath, 'r', encoding='utf8') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            return self.logs.append(lines)


    def logs_write_file(self):
        with open('logs.txt', 'a', encoding='utf8') as file:
            for log in self.logs:
                file.write(log + '\n')


manager = Manager()


@manager.assign("saldo")
def saldo():
    amount = float(input("Kwota wpłaty/wypłaty: "))
    if (amount < 0) and (manager.saldo + amount < 0):
        print("Nie masz środków na koncie!")
    manager.saldo += amount
    log = f"Zmiana saldo o: {amount}"
    manager.logs.append(log)


@manager.assign("zakup")
def zakup():
    product_name = input(("Nazwa produktu: "))
    product_count = int(input("Ilość sztuk: "))
    product_price = float(input("Cena za sztukę: "))
    product_total_price = product_count * product_price
    if product_total_price > manager.saldo:
        print(f"Cena za towary ({product_total_price}) przekracza wartość salda {manager.saldo}")
    else:
        manager.saldo -= product_total_price
        if not manager.store.get(product_name):
            manager.store[product_name] = {'count': product_count, 'price': product_price}
        else:
            manager.store_product_count = manager.store[product_name]['count']
            manager.store[product_name] = {
                'count': manager.store_product_count+product_count,
                'price': product_price}
    log = f"Dokonano zakupu produktu: {product_name} w ilości {product_count} sztuk, w cenie jednostkowej {product_price} zł."
    manager.logs.append(log)


@manager.assign("sprzedaz")
def sprzedaz():
    product_name = input(("Nazwa produktu: "))
    product_count = int(input("Ilość sztuk: "))
    product_price = float(input("Cena za sztukę: "))
    if not manager.store.get(product_name):
        print("Produktu nie ma w magazynie!")
    if manager.store.get(product_name)['count'] < product_count:
        print("Brak wystarczającej ilości towaru!")
    manager.store[product_name] = {
        'count': manager.store.get(product_name)['count'] - product_count,
        'price': product_price
    }
    manager.saldo += product_count * product_price
    if not manager.store.get(product_name)['count']:
        del manager.store[product_name]
    log = f"Dokonano sprzedaży produktu: {product_name} w ilości {product_count} sztuk, o cenie jednostkowej {product_price}."
    manager.logs.append(log)
