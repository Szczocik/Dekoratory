from accountant import manager
manager.read_file()
manager.execute('zakup')
manager.write_file()
manager.logs_write_file()
print(manager.store)
