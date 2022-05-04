import series
import animes
print("*************************************")
print("******Escolha o que Assistir!********")
print("*************************************")

print("(1) Series (2) Animes")

escolha = int(input("O que você gostaria de assisti ?"))

if(escolha == 1):
    print("Series")
    series.assistir()
elif(escolha == 2):
    print("Animes")
    animes.assistir()


print("Aproveite com uma Pipoca ")