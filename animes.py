import programas_lista
def assistir():
    print("*********************************************")
    print("****** Bem vindo, escolha seu Anime!********")
    print("*********************************************")

    print("Como você gostaria de Filtra?")
    print("(1) Temporadas (2) Data de lançamento")

    filtro = int(input(" Escolha seu Filtro ?"))

    if (filtro == 1):
        print("Temporadas")
        programas_lista.imprimir_temporada_animes()

    elif (filtro == 2):
        print("Data de lançamento")
        programas_lista.imprimir_lançamento_anime()



if(__name__ == "__main__"):
    assistir()