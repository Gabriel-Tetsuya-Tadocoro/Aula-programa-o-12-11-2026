'''Aula sobre condicao multipla  Não terminei o exercicio'''
combo = 0
qtde = 0
valor = 0
batata = 0
qtde_batata = 0
valor_batata = 0
bebida = 0
qtde_bebida = 0
valor_bebida = 0
print("programa lanchonete")
print("")
print("1 - X-Salada - R$20,00")
print("2 - X-Egg - R$17,00")
print("3 - X-Bacon - R$25,00")

lanche = int(input("Digite o numero do combo:"))

match lanche:
    case 1:
        print("X-Salada - R$20,00")
        qtde = int(input("quantas unidades deseja? "))
        valor = float(qtde*20.00)
        print("O valor do seu lanche ficou em R$", valor)
        acompanhamento_batata= input("Gostaria de adicionar batata como acompanahmento? (Sim/Não)")
        if acompanhamento_batata == "Sim":
            print("Escolha o tamanho da sua batata:")
            print(" 1 - Batata pequena - R$5,00")
            print(" 2 - Batata Media - R$7,00")
            print(" 3 - Batata Grande - R$9,00")
            batata = int(input("Digite o numero da batata?"))
            match batata:
                case 1:
                    print("Batata Pequena - R$5,00")
                    qtde_batata = int(input("Quantas unidades deseja?"))
                    valor_batata = float(qtde_batata*5.00)
                    print("O valor da batata de R$" , valor_batata)
                case 2:
                    print("Batata Media - R$7,00")
                    qtde_batata = int(input("Quantas unidades deseja?"))
                    valor_batata = float(qtde_batata*7.00)
                    print("O valor da batata de R$" , valor_batata)
                case 3:
                    print("Batata Grande - R$9,00")
                    qtde_batata = int(input("Quantas unidades deseja?"))
                    valor_batata = float(qtde_batata*9.00)
                    print("O valor da batata de R$" , valor_batata)
            valor_batata_hamburguer = float(valor_batata+valor)
            print("o valor total da sua compra ate agora é de", valor_batata_hamburguer)
        else:
            print("O valor total da sua compra ate o momento é de R$", valor)

        bebida= input("Gostaria de adicionar alguma bebida? (Sim/Não)")
        if bebida == "Sim":
            print("Escolha qual sera a sua bebida:")
            print(" 1 - Agua - R$5,00")
            print(" 2 - Refrigerante - R$7,00")
            print(" 3 - Suco de Laranja - R$9,00")
            bebida_escolhida = int(input("Digite o numero da bebida escolhida?"))
            match bebida_escolhida:
                case 1:
                    print("Aguá - R$5,00")
                    qtde_bebida = int(input("Quantas unidades deseja?"))
                    valor_bebida = float(qtde_bebida*5.00)
                    print("O valor da aguá é de R$" , valor_bebida)
                case 2:
                    print("Refrigante - R$7,00")
                    qtde_bebida = int(input("Quantas unidades deseja?"))
                    valor_bebida = float(qtde_bebida*7.00)
                    print("O valor do refrigerante é de R$" , valor_bebida)
                case 3:
                    print("Suco - R$9,00")
                    qtde_bebida = int(input("Quantas unidades deseja?"))
                    valor_bebida = float(qtde_bebida*9.00)
                    print("O valor da batata de R$" , valor_bebida)
            valor_batata_hamburguer_bebida = float(valor_batata+valor+valor_bebida)
            print("o valor total da sua compra ate agora é de", valor_batata_hamburguer_bebida)
    case 2:
        print("X-Egg - R$17,00")
        qtde = int(input("quantas unidades deseja? "))
        valor = float(qtde*17.00)
        acompanhamento_batata= input("Gostaria de adicionar batata como acompanahmento? (Sim/Não)")
        if acompanhamento_batata == "Sim":
            print("Escolha o tamanho da sua batata:")
            print(" 1 - Batata pequena - R$5,00")
            print(" 2 - Batata Media - R$7,00")
            print(" 3 - Batata Grande - R$9,00")
            batata = int(input("Digite o numero da batata?"))
            match batata:
                case 1:
                    print("Batata Pequena - R$5,00")
                    qtde_batata = int(input("Quantas unidades deseja?"))
                    valor_batata = float(qtde_batata*5.00)
                    print("O valor da batata de R$" , valor_batata)
                case 2:
                    print("Batata Media - R$7,00")
                    qtde_batata = int(input("Quantas unidades deseja?"))
                    valor_batata = float(qtde_batata*7.00)
                    print("O valor da batata de R$" , valor_batata)
                case 3:
                    print("Batata Grande - R$9,00")
                    qtde_batata = int(input("Quantas unidades deseja?"))
                    valor_batata = float(qtde_batata*9.00)
                    print("O valor da batata de R$" , valor_batata)
            valor_batata_hamburguer = float(valor_batata+valor)
            print("o valor total da sua compra ate agora é de", valor_batata_hamburguer)

            bebida= input("Gostaria de adicionar alguma bebida? (Sim/Não)")
            if bebida == "Sim":
                print("Escolha qual sera a sua bebida:")
                print(" 1 - Agua - R$5,00")
                print(" 2 - Refrigerante - R$7,00")
                print(" 3 - Suco de Laranja - R$9,00")
                bebida_escolhida = int(input("Digite o numero da bebida escolhida?"))
                match bebida_escolhida:
                    case 1:
                        print("Aguá - R$5,00")
                        qtde_bebida = int(input("Quantas unidades deseja?"))
                        valor_bebida = float(qtde_bebida*5.00)
                        print("O valor da aguá é de R$" , valor_bebida)
                    case 2:
                        print("Refrigante - R$7,00")
                        qtde_bebida = int(input("Quantas unidades deseja?"))
                        valor_bebida = float(qtde_bebida*7.00)
                        print("O valor do refrigerante é de R$" , valor_bebida)
                    case 3:
                        print("Suco - R$9,00")
                        qtde_bebida = int(input("Quantas unidades deseja?"))
                        valor_bebida = float(qtde_bebida*9.00)
                        print("O valor da batata de R$" , valor_bebida)
                valor_batata_hamburguer_bebida = float(valor_batata+valor+valor_bebida)
                print("o valor total da sua compra ate agora é de", valor_batata_hamburguer_bebida)
    case 3:
        print ("X-bacon - R$25,00")
        qtde = int(input("quantas unidades deseja? "))
        valor = float(qtde*25.00)
        acompanhamento_batata= input("Gostaria de adicionar batata como acompanahmento? (Sim/Não)")
        if acompanhamento_batata == "Sim":
            print("Escolha o tamanho da sua batata:")
            print(" 1 - Batata pequena - R$5,00")
            print(" 2 - Batata Media - R$7,00")
            print(" 3 - Batata Grande - R$9,00")
            batata = int(input("Digite o numero da batata?"))
            match batata:
                case 1:
                    print("Batata Pequena - R$5,00")
                    qtde_batata = int(input("Quantas unidades deseja?"))
                    valor_batata = float(qtde_batata*5.00)
                    print("O valor da batata de R$" , valor_batata)
                case 2:
                    print("Batata Media - R$7,00")
                    qtde_batata = int(input("Quantas unidades deseja?"))
                    valor_batata = float(qtde_batata*7.00)
                    print("O valor da batata de R$" , valor_batata)
                case 3:
                    print("Batata Grande - R$9,00")
                    qtde_batata = int(input("Quantas unidades deseja?"))
                    valor_batata = float(qtde_batata*9.00)
                    print("O valor da batata de R$" , valor_batata)
            valor_batata_hamburguer = float(valor_batata+valor)
            print("o valor total da sua compra ate agora é de", valor_batata_hamburguer)

            bebida= input("Gostaria de adicionar alguma bebida? (Sim/Não)")
            if bebida == "Sim":
                print("Escolha qual sera a sua bebida:")
                print(" 1 - Agua - R$5,00")
                print(" 2 - Refrigerante - R$7,00")
                print(" 3 - Suco de Laranja - R$9,00")
                bebida_escolhida = int(input("Digite o numero da bebida escolhida?"))
                match bebida_escolhida:
                    case 1:
                        print("Aguá - R$5,00")
                        qtde_bebida = int(input("Quantas unidades deseja?"))
                        valor_bebida = float(qtde_bebida*5.00)
                        print("O valor da aguá é de R$" , valor_bebida)
                    case 2:
                        print("Refrigante - R$7,00")
                        qtde_bebida = int(input("Quantas unidades deseja?"))
                        valor_bebida = float(qtde_bebida*7.00)
                        print("O valor do refrigerante é de R$" , valor_bebida)
                    case 3:
                        print("Suco - R$9,00")
                        qtde_bebida = int(input("Quantas unidades deseja?"))
                        valor_bebida = float(qtde_bebida*9.00)
                        print("O valor da batata de R$" , valor_bebida)
                valor_batata_hamburguer_bebida = float(valor_batata+valor+valor_bebida)
                print("o valor total da sua compra ate agora é de", valor_batata_hamburguer_bebida)
    case _:
        print ("Opção Invalida. Tente novamente")
print("O valor total da sua compra ficou", valor_batata_hamburguer_bebida)
