
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []
        self.daily_withdraw_count = 0 
        self.daily_withdraw_limit = 5

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Depósito: {amount}")
            print(f"Depósito de {amount} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def withdraw(self, amount):
        if self.daily_withdraw_count >= self.daily_withdraw_limit:
            print(f"Limite de saques atingido.")
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

def main():
    nome = input("Digite o nome do titular da conta: ")
    conta = BankAccount(account_holder=nome)

    while True:
        opcao = input("\n1. Depósito\n2. Saque\n3. Ver Extrato\n4. Sair\nEscolha: ")
        if opcao == '1':
            valor = float(input("Valor do depósito: "))
            conta.deposit(valor)
        elif opcao == '2':
            valor = float(input("Valor do saque: "))
            conta.withdraw(valor)
        elif opcao == '3':
            conta.get_statement()
        elif opcao == '4':
            print("Obrigado por usar o nosso sistema, volte sempre...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
