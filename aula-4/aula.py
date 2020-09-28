from matplotlib import pyplot as plt
from collections import Counter

def grafico_linha ():
  years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
  gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
  plt.plot (years, gdp, color='green', marker='o', linestyle='solid')
  plt.title ("GDP Nominal")
  plt.ylabel ("Bilhões de $")
  plt.show()

def grafico_barra ():
  movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
  num_oscars = [5, 11, 3, 8, 10]
  xs = [i for i, _ in enumerate (movies)]
  plt.bar(xs, num_oscars)
  plt.ylabel ("# de Premiações")
  plt.xlabel ("Filmes favoritos")
  plt.xticks ([i for i, _ in enumerate(movies)], movies)
  plt.show()

def grafico_histograma():
  grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
  decil = lambda grade: grade // 10 * 10
  decis = [decil (grade) for grade in grades]
  histograma = Counter (decis)
  plt.bar(
    [
      x for x in histograma.keys()
    ],
    histograma.values(),
    8
  )
  plt.axis ([-5, 105, 0, 5])
  plt.xticks ([10 * i for i in range (11)])
  plt.xlabel ("Decil")
  plt.ylabel ("# de Alunos")
  plt.title ("Distribuição das Notas do Teste 1")
  plt.show()

def mencoes_data_science_sem_valor_zero ():
  mencoes = [500, 505]
  anos = [2013, 2014]
  plt.bar (anos, mencoes, 0.4)
  plt.xticks(anos)
  plt.ylabel ("# de vezes que ouvimos alguem falar de data science")
  plt.axis ([2012.5, 2014.5, 499, 506])
  plt.title ("Olhe o grande aumento")
  plt.show()

def mencoes_data_science_com_valor_zero():
  mencoes = [500, 505]
  anos = [2013, 2014]
  plt.bar(anos, mencoes, 0.4)
  plt.xticks(anos)
  plt.ylabel("# de vezes que ouvimos alguem falar de data science")
  plt.axis([2012.5, 2014.5, 0, 550])
  plt.title("Veja a diferença")
  plt.show()

def grafico_dispersao ():
  amigos = [70, 65, 72, 63, 71, 64, 60, 64, 67]
  minutos = [175, 170, 205, 120, 220, 130, 105, 145, 190]
  rotulos = ['a', 'b', 'c', 'd', 'e', 'f', 'g' ,'h', 'i']
  plt.scatter(amigos, minutos)
  for rotulo, num_amigos, total_minutos in zip (rotulos, amigos, minutos):
    plt.annotate(
      rotulo,
      xy = (num_amigos, total_minutos),
      xytext= (5, -5),
      textcoords = 'offset points'
    )
  plt.title ("Minutos diários vs. Números de amigos")
  plt.xlabel ("# amigos")
  plt.ylabel ("Média de minutos diária passados na rede")
  plt.show()



def main():
  #grafico_linha()
  #grafico_barra()
  #grafico_histograma()
  #mencoes_data_science_com_valor_zero()
  grafico_dispersao()

main()