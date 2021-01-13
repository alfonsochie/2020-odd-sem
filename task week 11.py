# %%
class Bank:
    numberOfCustomers = 0

    def __init__(self, bankName, customers):
        self.bankName = bankName
        self.customers = customers

    def addCustomer(self, f, l):
        self.customers.append(Customer(f, l))
        self.numberOfCustomers += 1

    def getNumberOfCustomers(self):
        return self.numberOfCustomers

    def getCustomer(self, index):
        return self.customers[index]


class Customer:
    def __init__(self, f, l):
        self.firstName = f
        self.lastName = l
        self.account = Account()

    def getFName(self):
        return self.firstName

    def getLName(self):
        return self.lastName

    def getAccount(self):
        return self.account

    def setAccount(self, acc):
        self.account = acc


class Account:
    # class variable
    noOfAccounts = 0

    def __init__(self, balance=1000):
        self.balance = balance  # instance variable

    def getBalance(self):
        return self.balance

    def deposit(self, amt):
        if amt > 0:
            self.balance = self.balance + amt
            return True
        else:
            return False

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance = self.balance - amt
            return True
        else:
            return False


def main():
    customers = []
    bCa = Bank("BCA", customers)

    print(bCa.getNumberOfCustomers())

    bCa.addCustomer("Jonathan", "Mannuela")

    print(bCa.getCustomer(0).getAccount().getBalance())

    bCa.addCustomer("Maria", "Edward")

    print(bCa.getCustomer(1).getFName())

    print(bCa.getNumberOfCustomers())


"""
    newCust = Customer("Darren","Wenan")
    
    newCust.setAccount(Account(1000000))
    
    
    print("New account >> ", newCust.getAccount().getBalance())
    if newCust.getAccount().deposit(50000):
        print("Balance updated ", newCust.getAccount().getBalance())
    else:
        print("Invalid transaction!!!")
        print("Balance is not updated ",newCust.getAccount().getBalance())
        
    if newCust.getAccount().withdraw(100000):
        print("Balance updated ", newCust.getAccount().getBalance())
    else:
        print("Invalid transaction!!!")
        print("Balance is not updated ",newCust.getAccount().getBalance())
    
    
    newAccount = Account()
    print("New account >> ", newAccount.getBalance())
    if newAccount.deposit(50000):
        print("Balance updated ", newAccount.getBalance())
    else:
        print("Invalid transaction!!!")
        print("Balance is not updated ",newAccount.getBalance())
        
    if newAccount.withdraw(100000):
        print("Balance updated ", newAccount.getBalance())
    else:
        print("Invalid transaction!!!")
        print("Balance is not updated ",newAccount.getBalance())
"""
if __name__ == "__main__":
    main()

# %%
