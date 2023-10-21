from sqlitemodel import Model, Database

# IMPORTANT
Database.DB_FILE = 'database.db'

class SyncFolder(Model): 
    def __init__(self, id=None):
        Model.__init__(self, id)

        self.name = ''
        self.targetFolder = ''
        self.originFolder = ''

        # Tries to fetch the object by its rowid from the database
        self.getModel()


    # Tells the database class the name of the database table
    def tablename(self):
        return 'syncFolder'


    # Tells the database class more about the table columns in the database
    def columns(self):
        return [
            {
              'name': 'name',
              'type': 'TEXT'
            },
            {
              'name': 'targetFolder',
              'type': 'TEXT'
            },
            {
              'name': 'originFolder',
              'type': 'TEXT'
            }
        ]