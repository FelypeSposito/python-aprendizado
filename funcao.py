#aqui da para criar uma variavel dentro de uma funcao e subsituir a funcao global que foi declarada anteriormente.
#Essa variavel apenas funcionará dentro da funcao, fora dela a global tomará lugar

x = "essa aqui"

def funcao():
 print("essa é a variavel global: " + x);

funcao(); #declarando uma funcao com uma variavel de fora;

def funcao2():
 x = "tambem da para criar uma variavel "
 print(x + "usando um tipo temporario");

funcao2(); #declarando uma funcao com uma variavel de fora;


#alem disso tambem da para criar uma variavel global dentro de uma função:
def funcao3():
 global a
 a = "variavel global"
 print(a);

funcao3();


print(a)#esse print nao tem nada relacionado a funcao3, mas consegue fazer o print da string definida dentro da funcao
#por ter o elemento "global"

