class User:
    def __init__(self, cpf, name, birth_date, address):
        self.cpf = cpf
        self.name = name
        self.birth_date = birth_date
        self.address = address


class BankAccount:
    def __init__(self, user, agency, account_number, initial_balance=0):
        self.user = user
        self.agency = agency
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []
        self.daily_withdraw_count = 0
        self.daily_withdraw_limit = 5

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Depósito: +{amount}")
            print(f"Depósito de {amount} feito com sucesso.")
        else:
            print("Operação falhou!  O valor informado é inválido.")

    def withdraw(self, amount):
        if self.daily_withdraw_count >= self.daily_withdraw_limit:
            print("Atingido o limite de saques.")
        elif 0 < amount <= self.balance:
            self.balance -= amount
            self.daily_withdraw_count += 1
            self.transactions.append(f"Saque: -{amount}")
            print(f"Saque de {amount} feito com sucesso.")
        else:
            print("Operação falhou! Saldo insuficiente.")

    def get_statement(self):
        print("\nExtrato:")
        for transaction in self.transactions:
            print(transaction)
        print(f"Saldo actual: {self.balance}")


class Bank:
    def __init__(self):
        self.users = {}
        self.accounts = {}

    def create_user(self, cpf, name, birth_date, address):
        if cpf in self.users:
            raise ValueError("Usuário com esse CPF já existe!")
        user = User(cpf, name, birth_date, address)
        self.users[cpf] = user
        
        print(f"\nUsuário criado!")
        print(f"Nome: {user.name}")
        print(f"CPF: {user.cpf}")
        print(f"Data de nascimento: {user.birth_date}")
        print(f"Endereço: {user.address}\n")
        
        return user

    def create_account(self, cpf, agency, account_number, initial_balance=0):
        if cpf not in self.users:
            raise ValueError("Usuário não encontrado.")
        if cpf in self.accounts:
            raise ValueError("Este usuário já possui uma conta.")
        
        account = BankAccount(self.users[cpf], agency, account_number, initial_balance)
        self.accounts[cpf] = account

        print(f"\nConta criada para {self.users[cpf].name}!")
        print(f"Agência: {agency}, Número de conta: {account_number}")
        print(f"Saldo inicial: {initial_balance}\n")

        return account

    def list_users(self):
        if not self.users:
            print("Nenhum usuário cadastrado.")
        else:
            print("\nLista de Usários:")
            for user in self.users.values():
                print(f"Nome: {user.name}, CPF: {user.cpf}, Data de nascimento: {user.birth_date}, Endereço: {user.address}")

    def list_accounts(self):
        if not self.accounts:
            print("Nenhum conta cadastrada.")
        else:
            print("\nLista de contas:")
            for account in self.accounts.values():
                print(f"Titular: {account.user.name} (CPF: {account.user.cpf}), Agência: {account.agency}, Número de conta: {account.account_number}, Saldo: {account.balance}")


def get_cpf():
    return input("Digite o CPF: ")

def make_deposit(bank):
    cpf = get_cpf()
    account = bank.accounts.get(cpf)
    if account:
        amount = float(input("Depósito: "))
        account.deposit(amount)
    else:
        print("Nenhuma conta registrada para esse CPF.")

def make_withdrawal(bank):
    cpf = get_cpf()
    account = bank.accounts.get(cpf)
    if account:
        amount = float(input("Saque: "))
        account.withdraw(amount)
    else:
        print("Nenhuma conta registrada para esse CPF.")

def view_statement(bank):
    cpf = get_cpf()
    account = bank.accounts.get(cpf)
    if account:
        account.get_statement()
    else:
        print("Nenhuma conta registrada para esse CPF.")

def main():
    bank = Bank()

    options = {
        '1': lambda: bank.create_user(
            get_cpf(),
            input("Digite o nome: "),
            input("Digite a data de nascimento (dd/mm/yyyy): "),
            input("Digite o endereço: ")
        ),
        '2': lambda: bank.create_account(
            get_cpf(),
            input("Digite o número da agência: "),
            input("Digite o número de conta: "),
            float(input("Digite o saldo: "))
        ),
        '3': lambda: make_deposit(bank),
        '4': lambda: make_withdrawal(bank),
        '5': lambda: view_statement(bank),
        '6': lambda: bank.list_accounts(),
        '7': lambda: bank.list_users(),
        '8': exit
    }

    while True:
        option = input("\n1. Criar usário\n2. Criar conta\n3. Depósito\n4. Saque\n5. Ver extrato\n6. Ver contas\n7. Ver usuários\n8. Sair\nEscolhe: ")
        action = options.get(option)
        if action:
            try:
                action()
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
