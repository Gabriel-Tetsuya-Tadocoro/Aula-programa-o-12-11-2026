'''laço de repeticao tabuada'''
total = 0
num = 0
multiplicador = 0

print ("***PROGRAMA TABUADA***")
multiplicador = int(input("Digite o numero para a tabuada escolhida:"))

while(num<=10):
    total = num*multiplicador
    print(num, "x", multiplicador, "=", total)
    num=(num+1)
