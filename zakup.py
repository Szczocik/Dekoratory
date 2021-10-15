from accountant import manager
import pprint
manager.read_file()
manager.execute('zakup')
manager.write_file()
manager.logs_write_file()
pprint.pprint(manager.store)
