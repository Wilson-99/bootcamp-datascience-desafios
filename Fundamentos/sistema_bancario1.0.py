class User:
    users = {}  # Dicionário para armazenar usuários pelo CPF

    def __init__(self, cpf, nome, data_nascimento, endereco):
        if cpf in User.users:
            raise ValueError("Usuário com esse CPF já existe!")
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        User.users[cpf] = self

    @staticmethod
    def get_user_by_cpf(cpf):
        return User.users.get(cpf)

    @staticmethod
    def list_users():
        if not User.users:
            print("Nenhum usuário cadastrado.")
        else:
            print("\nLista de Usuários:")
            for user in User.users.values():
                print(f"Nome: {user.nome}, CPF: {user.cpf}, Data de Nascimento: {user.data_nascimento}, Endereço: {user.endereco}")


class BankAccount:
    accounts_by_cpf = {}  # Dicionário para armazenar contas pelo CPF

    def __init__(self, user, agencia, numero_conta, initial_balance=0):
        if user.cpf in BankAccount.accounts_by_cpf:
            raise ValueError("Este usuário já possui uma conta.")
        self.user = user
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.balance = initial_balance
        self.transactions = []
        self.daily_withdraw_count = 0
        self.daily_withdraw_limit = 5
        BankAccount.accounts_by_cpf[user.cpf] = self

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Depósito: +{amount}")
            print(f"Depósito de {amount} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def withdraw(self, amount):
        if self.daily_withdraw_count >= self.daily_withdraw_limit:
            print("Limite de saques atingido.")
        elif 0 < amount <= self.balance:
            self.balance -= amount
            self.daily_withdraw_count += 1
            self.transactions.append(f"Saque: -{amount}")
            print(f"Saque de {amount} realizado com sucesso.")
        else:
            print("Operação falhou! Você não tem saldo suficiente.")

    def get_statement(self):
        print("\nExtrato da Conta:")
        for transaction in self.transactions:
            print(transaction)
        print(f"Saldo atual: {self.balance}")

    @staticmethod
    def list_accounts():
        if not BankAccount.accounts_by_cpf:
            print("Nenhuma conta cadastrada.")
        else:
            print("\nLista de Contas:")
            for account in BankAccount.accounts_by_cpf.values():
                print(f"Titular: {account.user.nome} (CPF: {account.user.cpf}), Agência: {account.agencia}, Conta: {account.numero_conta}, Saldo: {account.balance}")


def create_user():
    cpf = input("Digite o CPF do usuário: ")
    if User.get_user_by_cpf(cpf):
        print("Usuário já existe. Use outro CPF.")
        return

    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/yyyy): ")
    endereco = input("Digite o endereço: ")

    try:
        novo_usuario = User(cpf, nome, data_nascimento, endereco)
        print(f"Usuário {novo_usuario.nome} criado com sucesso!")
    except ValueError as e:
        print(e)


def create_account():
    cpf = input("Digite o CPF do usuário: ")
    user = User.get_user_by_cpf(cpf)

    if not user:
        print("Usuário não encontrado. Por favor, crie um novo usuário primeiro.")
        return

    agencia = input("Digite o número da agência: ")
    numero_conta = input("Digite o número da conta: ")

    try:
        nova_conta = BankAccount(user=user, agencia=agencia, numero_conta=numero_conta)
        print(f"Conta criada com sucesso para {user.nome}. Agência: {agencia}, Conta: {numero_conta}.")
    except ValueError as e:
        print(e)


def main():
    print("Bem-vindo ao sistema bancário.")

    while True:
        opcao = input("\n1. Criar Usuário\n2. Criar Conta\n3. Depósito\n4. Saque\n5. Ver Extrato\n6. Ver Contas\n7. Ver Lista de Usuários\n8. Sair\nEscolha: ")

        if opcao == '1':
            create_user()

        elif opcao == '2':
            create_account()

        elif opcao == '3':
            cpf = input("Digite o CPF do usuário: ")
            conta = BankAccount.accounts_by_cpf.get(cpf)
            if conta:
                valor = float(input("Valor do depósito: +"))
                conta.deposit(valor)
            else:
                print("Nenhuma conta encontrada para este CPF.")

        elif opcao == '4':
            cpf = input("Digite o CPF do usuário: ")
            conta = BankAccount.accounts_by_cpf.get(cpf)
            if conta:
                valor = float(input("Valor do saque: "))
                conta.withdraw(valor)
            else:
                print("Nenhuma conta encontrada para este CPF.")

        elif opcao == '5':
            cpf = input("Digite o CPF do usuário: ")
            conta = BankAccount.accounts_by_cpf.get(cpf)
            if conta:
                conta.get_statement()
            else:
                print("Nenhuma conta encontrada para este CPF.")

        elif opcao == '6':
            BankAccount.list_accounts()

        elif opcao == '7':
            User.list_users()

        elif opcao == '8':
            print("Obrigado por usar o nosso sistema, volte sempre...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
