from models import Person, Bank


def main():
    masha = Person('masha')
    alex = Person('   alex')
    borys = Person('Borys')

    aval = Bank('aval')
    universal = Bank('universal')

    borys_account_in_aval = aval.open_account(borys)
    borys_account_in_aval2 = aval.open_account(borys)
    borys_account_in_universal = universal.open_account(borys)
    borys_account_in_aval.deposit(100)
    borys_account_in_universal.deposit(50)

    alex_account_in_aval = aval.open_account(alex)
    alex_account_in_aval.deposit(1000)

    print(alex == borys)
    print(alex >= borys)
    print(alex > borys)
    print(alex < borys)

    print(alex.money, borys.money)
    print(aval.money, universal.money)
    alex_account_in_aval.transfer_money(borys_account_in_universal, 234)
    print(alex.money, borys.money)
    print(aval.money, universal.money)

    print(aval > universal)


main()