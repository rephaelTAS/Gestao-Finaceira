


from config.funtion import Function


class Main:
    def __init__(self):
        super().__init__()
        
        self.func = Function()

        self.instrutin()
        self.command = int(input())
        if self.command == 1:
            description = str(input("Drecreva a despesa / receita: "))
            amount = int(input("Qual o valor: "))
            categori = str(input("Qual a categoria: "))
            self.func.add_expens(description, amount, categori)
        
        elif self.command == 2:
            dados = self.func.rede_expenses()
            print(dados)

        elif  self.command == 3:
            id = int(input("QUe despesa apagar (id): "))
            self.func.delete_expense(id)

        elif self.command == 4:
            self.func.listar_expenses()

    def instrutin(self):
             
        print(20*"===")
        print("||Bem Vindo(a) ao seu programa de gestão financeira!      ||")
        print("||                                                        ||")
        print("||Siga as instruções a baixo                              ||")
        print(20*"===")
        print("")
        print("")

        print(20*"===")
        print("[1] Adicionar dispesas / receitas ")
        print("")
        print("[2] Atualizar dispesas / receitas ")
        print("")
        print("[3] Apagar dispesas /  receitas ")
        print("")
        print("[4] visualizar as dispesas / receitas ")
        print("")
        print("[5] Visualizar os gastos ")
        print("")
        print("[6] Visualizar os gastos do mes especifico ")
        print("")
        print("[7] filtrar por categoria ")
        print("")
        print("[8] Limitar os gasto de um mes em especifico ")
        print("")
        print("[9] Exportar dados em um arquivo CSV ")
        print("")
        print("[10] Sair ")
        print(20*"===")
        print("")
        

if __name__ == "__main__":
    app = Main()