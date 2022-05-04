class Series():
    def __init__(self, nome, ano, temporadas):
        self.duracao = temporadas
        self.nome = nome
        self.ano = ano

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} Temp - {self.ano} Lançamento'


class Animes():
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas
    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Ano Lançamento: {self.ano} '


samurai_x = Animes("Samurai X ", 1994, 4)
dragon_ball = Animes("Dragon Ball ", 1986, 16)
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
    print(jujutsu_kaisen)
    print(kimetsu_no_yaiba)
    print(samurai_x)
    print(boku_no_hero_academia)
    print(naruto_clasico)
    print(cavaleiros_do_zodíaco)

def imprimir_temporadas_series():
    print(atlanta)
    print(demolidor)
    print(the_good_doctor)
    print(vinkings)

def imprimir_lançamento_anime():
    print(dragon_ball)
    print(cavaleiros_do_zodíaco)
    print(samurai_x)
    print(one_piece)
    print(naruto_clasico)
    print(naruto_shippuden)
    print(boku_no_hero_academia)
    print(jujutsu_kaisen)
    print(kimetsu_no_yaiba)
def imprimir_lançamento_serie():
    print(vinkings)
    print(demolidor)
    print(atlanta)
    print(the_good_doctor)


