# ** Quanto é 7 elevado na potência 4?**
ex1 = 7 ** 4
print('exercicio 1:', ex1)

# ** Quebre a seguinte string em uma lista:**
s = "Olá, Pai!"
ex2 = s.split(" ")
print('exercicio 2:', ex2)

# ** Dada as variáveis:**
# Planeta = "Terra"
# Diametro = 12742
# ** Use .format() para printar a seguinte frase: **
# O diâmetro da terra é de 12742 kilômetros.
ex3 = "O diâmetro da {} é de {} kilômetros.".format("Terra", 12742)
print('exercicio 3:', ex3)

# ** Dada a lista abaixo, use indexação para obter apenas a string “ola”. ** 
lst = [1,2,[3,4],[5,[100,200,['olá']],23,11],1,7]
ex4 = ''
print('exercicio 4:', ex4)

# ** Dado o seguinte dicionário aninhado, extraia a palavra “hello” **
d = {'k1':[1,2,3,{'café':['banana','mulher','colher',{'alvo':[1,2,3,'olá']}]}]}
ex5 = ''
print('exercicio 5:', ex5)

# ** Qual a principal diferença entre um dicionário e uma tupla? **
print('exercicio 6: Os elementos de uma tupla são acessados pelo index e os elementos do dicionário via chave')

# ** Construa uma função que retire o domínio dado um e-mail no seguinte formato: **
# user@domain.com
# Por exemplo, passando como parâmetro “user@domain.com” retornaria: domain.com
email = "user@domain.com"
ex7 = email[email.index('@') + 1 : ]
print('exercicio 7:', ex7)


