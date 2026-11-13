'''Aula sobre condicao multipla - Não terminie o exercicio'''
combo = 0
qtde = 0
valor = 0
batata = 0
qtde_batata = 0
valor_batata = 0
bebida = 0
print("programa lanchonete")
print("")
lanche = int(input("Digite o numero do combo:"))

match lanche:
    case 1:
        print("X-Salada - R$20,00")
        qtde = int(input("quantas unidades deseja? "))
        valor = float(qtde*20.00)
        print("O valor do seu lanche ficou em R$", valor)
        acompanhamento_batata= input("Gostarua de adicionar batata como acompanahmento? (Sim/Não)")
        if acompanhamento_batata == "Sim":
            print("Escolha o tamanho da sua batata:")
            print(" 1 - Batata pequena - R$5,00")
            print(" 2 - Batata pequena - R$7,00")
            print(" 3 - Batata pequena - R$9,00")
            batata = int(input("Digite o numero da batata?"))
            match batata:
                case 1:
                    print("Batata Pequena - R$5,00")
                    qtde_batata = int(input("Quantas unidades deseja?"))
                    valor_batata = float(qtde_batata*5.00)
                    
                    print("O valor da batata de R$"+valor_batata)
                    
                case 2:
                    print("Batata Media - R$7,00")
                    qtde_batata = int(input("Quantas unidades deseja?"))
                    valor_batata = float(qtde_batata*7.00)
                    print("O valor da batata de R$"+valor_batata)
                case 3: 
                    print("Batata Pequena - R$9,00")
                    qtde_batata = int(input("Quantas unidades deseja?"))
                    valor_batata = float(qtde_batata*9.00)
                    print("O valor da batata de R$"+valor_batata)
            print("o valor total da sua compra é de"valor+valor_batata)
        else:
            print("Gostaria de adicionar alguma bebida? (Sim/Não)")
        
                


    case 2:
        print("X-Egg - R$17,00")
        qtde = int(input("quantas unidades deseja? "))
        valor = float(qtde*17.00)
    case 3:
        print ("X-bacon - R$25,00")
        qtde = int(input("quantas unidades deseja? "))
        valor = float(qtde*25.00)
    case _:
        print ("Opção Invalida. Tente novamente")
print("O valor da sua compra é de R$", valor)