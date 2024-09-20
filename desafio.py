menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[i] Informações
[q] Sair

[a] Alterar Exibição do Extrato
[v] Virar o dia
=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

larguraDisplay = 40
maxLinhas = 10

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f} (R$ {saldo:.2f})")
                                                        
            print(f"Depósito de R$ {valor:.2f} realizado. Seu saldo agora é: RS {saldo:.2f}.")

        else:
            print("Operação não autorizada. Informe um valor maior que zero.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > limite:
            print("Operação não realizada: excedeu o limite de saque.")
        elif numero_saques > 2:
            print("Operação não realizada: excedeu o número diário de saques (3).")
        elif valor > saldo:
            print("Operação não realizada: saldo insuficiente.")
        elif valor > 0:
            numero_saques += 1
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f} (R$ {saldo:.2f})")
            print(f"Você sacou R$ {valor:.2f}. Seu saldo agora é R$ {saldo:.2f}.")
        else:
            print("Valor inválido. Por favor, informe um valor maior que zero.")
        
    elif opcao == "e":
        print("| Extrato |".center(larguraDisplay, '-'))
        
        if extrato:
            if len(extrato) < maxLinhas:
                for linha in range(len(extrato)):
                    print(f"{linha+1}. {extrato[linha]}".center(larguraDisplay))
            else: 
                for linha in range(maxLinhas):
                    print(f"{-(-maxLinhas-linha)+1}. {extrato[(-maxLinhas-linha)]}".center(larguraDisplay))

            print('')
        else:
            print("Sem movimentações.".center(larguraDisplay))
        
        print(f"Saldo: R$ {saldo:.2f}".center(larguraDisplay))
        print("-".center(larguraDisplay, '-'))

    elif opcao == "a":
        muda = input("""
[t] Mudar o número de transações exibidas.
[l] Mudar a largura da tela de extrato.
                     """)
        if muda == 't':
            valor = int(input("Qual o número de transações que gostaria de exibir? (Entre 1 e 30)\n"))
            if valor > 0 and valor <= 30:
                maxLinhas = valor
                print(f"Alterado com sucesso. Agora o extrato exibirá {valor} linhas.")
            else:
                print("Valor inválido. Por favor, insira um valor entre 25 e 50")
        
        elif muda == "l":
            valor = int(input("Qual a largura desejada da exibição do extrato? (Entre 25 e 50)\n"))
            if valor > 24 and valor <= 50:
                larguraDisplay = valor
                print(f"Alterado com sucesso. Agora o extrato terá a largura de {valor} caracteres.")
            else:
                print("Valor inválido. Por favor, insira um valor entre 25 e 50.")
        else: 
            print("Comando inválido.")

    elif opcao == "v":
        numero_saques = 0
        print("Dia virado. O número de saques diários foi resetado.")

    elif opcao == "i":
        print(f"O número máximo de saques diário é {LIMITE_SAQUES}. Hoje você realizou {numero_saques} saques.")
        print(f"O limite máximo de saque é R$ {float(limite):.2f}. Seu saldo atual é R$ {saldo:.2f}.")

    elif opcao == "q":
        break

    else:
         print("Operação inváilida, por favor selecione novamente a operação desejada.")
