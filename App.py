from recomendacao import *

base = carregaMovieLens()

print(getSimilares(base, '1'))
print(getRecomendacoes(base, '212'))