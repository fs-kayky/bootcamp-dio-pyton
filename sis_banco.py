menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
 
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd' :
        
        print("Depósito\n\n")

        while True:

            valor = float(input("Digite o valor do seu Depósito\n\n=> "))

            if valor > 0:
                print("\n Depósito realizado com sucesso!")
                saldo += valor

                extrato += f"\nDepósito: R$ {valor:.2f}"
                break
            else:
                print("\nDigite um valor valido para depósito!\n\n")
    elif opcao == 's':
        
        print("Saque\n\n")

        while True:

            valor = float(input("Digite o valor que deseja sacar\n\n=>"))

            if valor > limite:
                print("\nValor de saque mais alto que o permitido!\n\n")
            
            elif valor > saldo:
                print("\nSaldo Insuficiente!\n\n")
                break
            
            elif numero_saques >= LIMITE_SAQUES:
                print("\nVocê atingiu o limite de saques diários!\n\n")
                break
            
            elif valor < 0:
                print("\nDigite um valor valido para saque!\n\n")
            
            elif valor <= limite and valor < saldo and numero_saques < LIMITE_SAQUES:
                print("\nSaque concluído com sucesso!\n\n")

                saldo -= valor
                numero_saques += 1
                extrato += f"\nSaque: R$ {valor:.2f}"
                break
        
    elif opcao == 'e':
        print("========== EXTRATO ==========")
        print(extrato + f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")
    elif opcao == 'q':
        print("Obrigado por usar nosso banco!")
        break
    else:
        print("\n\n SELECIONE UMA OPERAÇÃO VALIDA!\n\n")
                