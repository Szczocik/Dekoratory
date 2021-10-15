from accountant import manager
manager.read_file()
manager.execute('saldo')
manager.write_file()
manager.logs_write_file()
print(manager.saldo)