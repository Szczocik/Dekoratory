from accountant import manager
manager.read_file()
manager.execute('saldo')
print(manager.saldo)