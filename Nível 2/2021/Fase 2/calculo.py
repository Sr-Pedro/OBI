#Deixei as mudanças no final do arquivo

S = int(input())

A = int(input())
B = int(input())

ListaIntervalo = []
Contador = A
while Contador <= B:
    ListaIntervalo.append(Contador)
    Contador+=1

#print(ListaIntervalo)

ListaNumerosNoIntervaloIguaisAS = []

for i in range(len(ListaIntervalo)):
    
    if len(str(ListaIntervalo[i])) == 1:
        if int(ListaIntervalo[i]) == S:
            ListaNumerosNoIntervaloIguaisAS.append(int(ListaIntervalo[i]))
    else:
        soma = 0
        for digito in str(ListaIntervalo[i]):
            soma += int(digito)
            
            if soma == S:
                ListaNumerosNoIntervaloIguaisAS.append(int(ListaIntervalo[i]))
        
            
#print(ListaNumerosNoIntervaloIguaisAS)
print(len(list(set((ListaNumerosNoIntervaloIguaisAS)))))
#print(len(ListaNumerosNoIntervaloIguaisAS))


S = input()
A = input()
B = input()

#Variável que contará o número de valores cuja soma dos dígitos é igual a S
Count = 0

#Usando range para percorrer os elementos de A a B
for x in range(int(A),int(B)+1):
    
    #Estabelecendo uma variável que será usada posteriormente
    
    sum = 0

    #Iterando sobre cada elemento do intervalo inteiro de A a B.
    #Para que a iteração ocorra, converte-se o valor em string
    #Essa parte do código visa pegar cada dígito e depois convertê-lo para int
    #Convertendo-o, somaremos este à variável anteriormente estabelecida e assim poderemos observar a soma dos dígitos do valor

    for y in str(x):
        sum += int(y)
    #Condicional para ver se a soma dos dígitos do valor é igual a S
    if sum == int(Soma):
        Count += 1
    else:
        continue

print(C)
