from datetime import datetime
import os
import json

class DB_Config:
    def __init__(self):
        super().__init__()
        self.ficheiro = os.path.join("src", "database", "dados.json")

    def rede_file(self):
        if os.path.exists(self.ficheiro):
            with open(self.ficheiro, 'r') as file:
                return json.load(file)
        return []
    
    def save_expenses(self, expenses):
        with open(self.ficheiro, 'w') as file:
            json.dump(expenses, file, indent=4)
    
    def add_expense(self, description, amount, status):
        expenses = self.rede_file()
        expense = {
            'id': self.get_next_id(),
            'date': str(datetime.now().date()),
            'description': description,
            'amount': amount,
            'status': status
        }
        expenses.append(expense)
        self.save_expenses(expenses)
        print(f"Expense added successfully (ID: {expense['id']})")

    def list_expense(self):
        expenses = self.rede_file()
        print(f"{'ID':<4} {'Date':<12} {'Description':<15} {'Amount':<7} {'Status':<20}")
        for expense in expenses:
            print(f"{expense['id']:<4} {expense['date']:<12} {expense['description']:<15} {expense['amount']:<7}  {expense['status']:<20}")
            print("")

    def delete_expense(self, id):
        expenses = self.rede_file()
        expenses = [expense for expense in expenses if expense['id'] != id]
        self.save_expenses(expenses)
        print(f"Expense deleted successfully (ID: {id})")
    
    def get_next_id(self):
        expenses = self.rede_file()
        if len(expenses) == 0:
            return 1
        else:
            return max(expe['id'] for expe in expenses) + 1

    def update_expense(self, id, description=None, amount=None, status=None):
        expenses = self.rede_file()
        for expense in expenses:
            if expense['id'] == id:
                if description:
                    expense['description'] = description

                if amount:
                    expense['amount'] = amount

                if status:
                    expense['status'] = status

                self.save_expenses(expenses)
                print(f"Expense {id} updated successfully")
                return
        print(f"Expense with ID {id} not found")