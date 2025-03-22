class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Saldo tidak mencukupi."
        else:
            self.balance -= amount
            return self.balance
        
    def get_balance(self):
        return self.balance
    
    def get_name(self):
        return self.name

while True:    
    user_name = str(input("Masukkan nama: "))
    user_choice = str(input("Masukkan pilihan (Deposit / Withdraw): ")).lower()
    amount = float(input("Masukkan jumlah: "))

    account = BankAccount(user_name, 0)

    if user_choice == "deposit":
        account.deposit(amount)

    elif user_choice == "withdraw":
        print(account.withdraw(amount))

    else:
        print("Pilihan tidak valid.")
        continue

    print(f"\nNama: {account.get_name()}")
    print(f"Saldo: Rp.{account.get_balance():,.2f}\n")

    lagi = str(input("Lagi? (y/n): ")).lower()
    if lagi != "y":
        break
