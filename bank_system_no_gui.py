class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, name, balance = 0):
        if name in self.accounts:
            print("Esta conta ja existe!")
        else:
            self.accounts[name] = balance
            print(f"Conta com nome {name} criada com sucesso!")

    def deposit_money(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
            print(f"{amount}€ depositado com sucesso!")
        else:
            print("Esta conta nao existe!")

    def withdraw_money(self, name, amount):
        if name in self.accounts:
            if self.accounts[name] >= amount:
                self.accounts[name] -= amount
                print(f"{amount}€ levantado com sucesso!")
            else:
                print("Saldo insuficiente!")
        else:
            print("Esta conta nao existe!")

    def check_balance(self, name):
        if name in self.accounts:
            print(f"Saldo: {self.accounts[name]}€")
        else:
            print("Esta conta nao existe!")
            
    def transfer_money(self, name, receiver, amount):
        if name in self.accounts:
            if receiver in self.accounts:
                if self.accounts[name] >= amount:
                    self.accounts[name] -= amount
                    self.accounts[receiver] += amount
                    print(f"O valor de {amount}€ foi transferido com sucesso para a conta {receiver}!")
                else:
                    print("Saldo insuficiente!")
            else:
                print("A conta do destinatario nao existe!")
        else:
            print("Esta conta nao existe!")

bank = Bank()

#DEBUG
#bank.open_account("John", 1000)
#bank.deposit_money("John", 500)
#bank.withdraw_money("John", 250)
#bank.check_balance("John")
#bank.transfer_money("John", "Lewis", 250)