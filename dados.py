from random import randint
dado=0
sacarficha = 5
while dado!= sacarficha:
    dado = randint(1,6)

    if dado != sacarficha:
        print(f"Has sacado {dado}")
    elif dado == 5:
        print(f"Sacaste {dado}")

