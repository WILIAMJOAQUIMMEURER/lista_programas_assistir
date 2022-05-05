class Series():
    def __init__(self, nome, ano, temporadas):
        self.duracao = temporadas
        self.nome = nome
        self.ano = ano

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} Temp - {self.ano} Lançamento'


class Animes():
    def __init__(self, nome, ano, temporadas,):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Ano Lançamento: {self.ano} '


samurai_x = Animes("Samurai X ", 1994, 4,)
dragon_ball = Animes("Dragon Ball ", 1986, 16,)
cavaleiros_do_zodíaco = Animes("Cavaleiros do Zodíaco", 1986, 10)
boku_no_hero_academia = Animes('Boku no Hero Academia', 2014, 6)
jujutsu_kaisen = Animes('Jujutsu Kaisem ', 2021, 2)
kimetsu_no_yaiba = Animes('Kimetsu no Yaiba', 2021, 2)
naruto_clasico = Animes("Naruto Clasico ", 1999, 9)
naruto_shippuden = Animes("Naruto Shippuden ", 2007, 20)
one_piece = Animes("One Piece ", 1999, 20)
atlanta = Series('atlanta', 2016, 2)
demolidor = Series('demolidor', 2016, 2)
the_good_doctor = Series("The Good Doctor", 2017, 5 )
vinkings = Series("Vikings", 2013, 6)


def imprimir_temporada_animes():

    lista_temporada = [jujutsu_kaisen,kimetsu_no_yaiba,samurai_x,boku_no_hero_academia,
                       naruto_clasico, cavaleiros_do_zodíaco]

    for l in lista_temporada:
        print(l)


def imprimir_temporadas_series():

   lista_temporada_serie = [atlanta,demolidor,the_good_doctor,vinkings]

   for k in lista_temporada_serie:
       print(k)


def imprimir_lançamento_anime():

    lista_lançamento = [dragon_ball,cavaleiros_do_zodíaco,samurai_x,one_piece,naruto_clasico,
                        naruto_shippuden,boku_no_hero_academia,jujutsu_kaisen,kimetsu_no_yaiba]

    for lis in lista_lançamento:
        print(lis)
def imprimir_lançamento_serie():

    lista_lançamento_serie = [vinkings,demolidor,atlanta,the_good_doctor]

    for lançamento in lista_lançamento_serie:
        print (lançamento)


