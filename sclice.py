#cortou a palavra pelas cordenadas entre 2 e 5

b = " Hello, World!"
print(b[2:5]);

print(b[:5]); #cortou desde o começo ate o quinto elemento da string

print(b[2:]) #cortou desde a posição 2 até o fim

print(b.upper())
print(b.lower())

print(b.strip()) #remove os espaços desnecessários no fim ou no começo da string
print(b.replace("H", "J")) #troca a letra H por J