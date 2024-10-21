from config.funtion import Function


class Main:
    def __init__(self):
        super().__init__()
        while True:
            self.func = Function()

            self.instrutin()
            self.command = int(input())
            """Adicionando dispesas / reeitas"""
            if self.command == 1:
                description = str(input("Drecreva a despesa / receita: "))
                amount = int(input("Qual o valor: "))

                print("")
                print("Digite 1 para Entrada e 2 para Saida")
                sta = int(input())
                if sta == 1:
                    categori = "Entrada"
                else:
                    categori = "Saida"

                self.func.add_expens(description, amount, categori)
            
            elif self.command == 2:
                """Atualizar dados de receitas / dispesas"""
                # variave
                description = None
                amount = None
                categori = None

                self.func.listar_expenses()
                print("")
                id_exp = int(input("Digite o ID da receita: "))
                print("")
                
                print("Atualizar a descrição [y/n]")
                confi = input("> ")
                if confi == "y":
                    description = input("Nova Descrição: ")
                print("")

                print("Atualizar valor [y/n]")
                confi = input("> ")
                if confi == "y":
                    amount = input("Novo valor: ")
                print("")

                
                print("Atualizar a Status [y/n]")
                confi = input("> ")
                if confi == "y":
                    print("Digite 1 para Entrada e 2 para Saida")
                    sta = int(input("> "))
                    if sta == 1:
                        categori = "Entrada"
                    else:
                        categori = "Saida"


                self.func.atualizar_expens(id=id_exp, description=description, amount=amount, status=categori)
                print(20*"===")
                self.func.listar_expenses()

            elif  self.command == 3:
                id = int(input("QUe despesa apagar (id): "))
                self.func.delete_expense(id)
                print("")
                self.func.listar_expenses()

            elif self.command == 4:
                self.func.listar_expenses()
            
            elif self.command == 5:
                self.func.total_despesa()
            
            elif self.command == 6:
                data = input("Data: ")
                self.func.despesas(data)

            elif self.command == 7:

                categoria = ""
                print("")
                print("Digite 1 para Entrada e 2 para Saida")
                sta = int(input())
                if sta == 1:
                    categoria = "Entrada"
                else:
                    categoria = "Saida"
                self.func.filtro_cate(categoria=categoria)

            elif self.command == 8:
                """Limitar os gasto de um mes em especifico"""
                print("Informe o mês que pretende limitar os gastos")
                print("[1] Janeiro; [2] Fivereiro; [3] Março; [4]Abril; [5] Maio; [6] Junho; [7] Julho; [8] Agosto; [9] Setembro; [10] Outubro; [11] Novembro; [12] Desembro")
                mes = int(input(">: "))
                valor = int(input("O valor: "))
                self.func.limitar_gasto(mes, valor)

            elif self.command == 9:
                self.func.exportar_csv()

            elif self.command == 10:
                break

            else:
                print("Digite apenas os números mencionados na instrução")


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