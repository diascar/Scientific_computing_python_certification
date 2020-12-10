class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        tmp = {"amount": amount, "description": description}
        self.ledger.append(tmp)

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            tmp = {"amount": -amount, "description": description}
            self.ledger.append(tmp)
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance

    def transfer(self, amount, another):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to {}".format(another.name))
            another.deposit(amount, "Transfer from {}".format(self.name))
            return True
        else:
            return False

    def check_funds(self, amount):
        return True if self.get_balance() >= amount else False

    def __str__(self):
        title = f'{self.name:*^30}\n'
        for i in self.ledger:
            title += f'{i["description"][0:23]: <23}{i["amount"]:>7.2f}\n'
        title += f'Total: {self.get_balance()}'
        return title



def create_spend_chart(categories):
    result = 'Percentage spent by category\n'
    labels = [f"{i:>3}" + "| " for i in range(0, 101, 10)]
    labels.reverse()
    expenditure_cat = {cat.name: sum([item['amount'] for item in cat.ledger if item['amount'] < 0]) for cat in categories}
    total_exp = sum(map(lambda x: x[1], expenditure_cat.items()))
    percent_category = {k:round(val/total_exp*100) for k,val in expenditure_cat.items()}
    bars = {}
    for k in percent_category.keys():
        tmp_list = []
        for i in range(0, 101, 10):
            if i <= percent_category[k]:
                tmp_list.append('o  ')
            else:
                tmp_list.append('   ')
        tmp_list.reverse()
        bars[k] = tmp_list
    
    names = [cat.name for cat in categories]
    largest_name = max(len(n) for n in names)
    names = ["{:<{size}}".format(i, size = largest_name) for i in names]

    for i in range(len(labels)):
        line = f"{labels[i]}"
        for cat in categories:
            line += f"{bars[cat.name][i]}"
        result += line + "\n"
    result += '    {}-'.format('---'*len(bars)) + "\n"
    for i in range(largest_name):
        line = f"     "
        for j in names:
            line += f"{j[i]}  "
        if i < (largest_name - 1):
            result += line + "\n"
        else: result += line
    return result

