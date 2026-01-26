# ПОГАНИЙ КОД (Anti-pattern)
class DatabaseHandler:
    def connect(self):
        print("Connected to DB")
    def execute_query(self, query):
        print(f"Executing: {query}")

class MonthlyReport:
    
    def __init__(self):
        self.db_handler = DatabaseHandler()

    def create(self):
        self.db_handler.connect()
        self.db_handler.execute_query('ffff')

report = MonthlyReport()
report.create()