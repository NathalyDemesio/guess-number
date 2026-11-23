import random

print("Seja muito bem vindo ao Guess Number!")
choice_number = input("Digite um número teto do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: o valor informado não é numérico. Por favor, execute novamente e informe um número!")
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    answer_user = input("Advinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: o valor informado não é numérico. Por favor, execute novamente e informe um número!")
        continue

    n_choices += 1

    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Chutou alto, o número é menor que isso...")
    else:
        print("Chutou baixo, o número é maior que isso...")

print(f"O número de tentativas foi: {n_choices}")