from config.db_config import DB_Config


class Function:
    def __init__(self):
        super().__init__()
        self.db_config = DB_Config()

    def rede_expenses(self):
        return self.db_config.rede_file()
    
    def listar_expenses(self):
        self.db_config.list_expense()

    def add_expens(self, description, amount, status):
        self.db_config.add_expense(description=description, amount=amount, status=status)

    def delete_expense(self, id):
        self.db_config.delete_expense(id=id)

    def sumary(self, mes= None, status=None):
        expenses = self.db_config.rede_file()
        total_geral = 0
        total_mes = 0
        for expense in expenses:
            if status in expense['status']:
                total_geral +=  expense['amount']

        if mes:
            for expense in expenses:
                if expense['date'] == mes:
                    total_mes +=  expense['amount']
            print(f"A receita do mes {mes} foi de {total_mes}")

    def despesas(self, mes=None, status=None):
        self.sumary(mes, status)

    def receitas(self, mes=None, status=None):
        self.sumary(mes, status)
    
    def total_despesa(self):
        expenses = self.db_config.rede_file()
        self.db_config.list_expense()
        total_geral = 0
        for expense in expenses:
            total_geral += expense['amount']
        
        self.despesas(status="Saida")
        self.receitas(status="Entrada")

        