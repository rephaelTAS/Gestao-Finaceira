from config.db_config import DB_Config
import os
from datetime import datetime


class Function:
    def __init__(self):
        super().__init__()
        self.db_config = DB_Config()

    def rede_expenses(self):
        return self.db_config.rede_file()
    
    def listar_expenses(self):
        self.db_config.list_expense()

    def filtro_cate(self, categoria):
        self.db_config.filtro_categoria(categoria=categoria)
        self.soma_cat(categor=categoria)
    def add_expens(self, description, amount, status):
        self.db_config.add_expense(description=description, amount=amount, status=status)

    def atualizar_expens(self,id, description=None, amount=None, status=None):
        self.db_config.update_expense(id, description=description, amount=amount, status=status)

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
            return total_mes

    def soma_cat(self, categor):
        expenses = self.db_config.rede_file()
        total_mes = 0
        for expense in expenses:
            if expense['status'] == categor:
                total_mes +=  expense['amount']

        print(20*"===")
        print(f"{'Total':<4} {'':<12} {'':<15}{total_mes:<7} ")
        print("")

    def despesas(self, mes=None, status="Saida"):
        dados = self.sumary(mes, status)
        print(f"O total do mês de {mes} foi de {dados}")

    def receitas(self, mes=None, status="Entrada"):
        dados = self.sumary(mes, status)
        print(f"O total do mês de {mes} foi de {dados}")
    
    def total_despesa(self):
        expenses = self.db_config.rede_file()
        self.db_config.list_expense()
        total_geral = 0
        for expense in expenses:
            total_geral += expense['amount']
        
        print(20*"===")
        print(f"{'Total':<4} {'':<12} {'':<15}{total_geral:<7} ")

    def limitar_gasto(self, mes, valor):
        meses = {
            1: "janeiro",
            2: "fevereiro",
            3: "março",
            4: "abril",
            5: "maio",
            6: "junho",
            7: "julho",
            8: "agosto",
            9: "setembro",
            10: "outubro",
            11: "novembro",
            12: "dezembro"
        }

        nome_mes = meses.get(mes)

        daods = self.db_config.rede_file()
        # Filtrar os gastos
        gastos = [item for item in daods if item['status'] == 'Saida']

        # Filtrar pelo mês
        gastos_mes = [
        item for item in gastos 
        if 'date' in item and datetime.strptime(item['date'], '%Y-%m-%d').month == mes
    ]

            # Soma o total gasto no mês filtrado
        total_gasto = sum(float(item['amount']) for item in gastos_mes if 'amount' in item)

        # Verificar se o total gasto excede o valor limite
        if total_gasto > valor:
            print(f"Você excedeu o limite de {valor} no mês {nome_mes.capitalize()}. Total gasto: {total_gasto}")
        else:
            print(f"Você está dentro do limite de {valor} no mês {nome_mes.capitalize()}. Total gasto: {total_gasto}")
        print("")

        
    def exportar_csv(self):
        df = self.db_config.export_csv()
        caminho_csv = os.path.join("src", "dados", "dados.csv")
        df.to_csv(caminho_csv, index=False)

        print("Dados salvos com sucesso")