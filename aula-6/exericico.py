import math
import random

height_weight_age = [
    53, 
    165,
    28
]

grades = [
    95,
    90,
    75,
    62
]

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum (vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]


def vector_mean (vectors):
    n = len(vectors)
    return scalar_multiply((1 / n), vector_sum(vectors))

def dot (v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares((vector_subtract(v, w)))

def distance (v, w):
    return math.sqrt(squared_distance(v, w))

def distance_alt(v, w):
    return magnitude(vector_subtract(v, w))

def qtde_amigos_minutos_passados ():
    return ([1, 10, 50, 2, 150], [5, 200, 350, 17, 1])

def qtde_amigos_minutos_passados_sem_outlier ():
    return ([1, 10, 50, 2], [5, 200, 350, 17])

def variance(v):
    mean = sum(v) / len(v)
    print(mean)
    return [v_i - mean for v_i in v]


def covariance(x, y):
    n = len(x)
    return dot(variance(x), variance(y)) / (n-1)

def correlation(x, y):
    desvio_padrao_x = math.sqrt(sum_of_squares(variance(x)) / (len(x) - 1))
    desvio_padrao_y = math.sqrt(sum_of_squares(variance(y)) / (len(y) - 1))

    if desvio_padrao_x > 0 and desvio_padrao_y > 0:
        return covariance(x, y) / desvio_padrao_y / desvio_padrao_x
    else:
        return 0

def correlation_test_with_outlier():
    data = qtde_amigos_minutos_passados()
    resultado = correlation(data[0], data[1])
    print(resultado)

def correlation_test_removing_outlier():
    data = qtde_amigos_minutos_passados_sem_outlier()
    resultado = correlation(data[0], data[1])
    print(resultado)

#testes
def vector_add_test():
    v = [1, 7]
    w = [5, 4]
    r = vector_add(v, w)
    print (r)   


def vector_subtract_test():
    v = [5, 4]
    w = [2, 1]
    r = vector_subtract(v, w)
    print (r) 


def vector_sum_test ():
    v1 = [1, 2, 5, 6]
    v2 = [4, 3, 2, 1]
    v3 = [1, 1, 1, 1]
    r = vector_sum([v1, v2, v3])
    print (r)


def scalar_multiply_test():
    c = 5
    v = [4, 1, 2, 5]
    r = scalar_multiply(c, v)
    print (r)

def vector_mean_test ():
    v1 = [1, 2, 5, 6]
    v2 = [4, 3, 2, 1]
    v3 = [1, 1, 1, 1]
    r = vector_mean([v1, v2, v3])
    print(r)

def dot_test ():
    v = [1, 2]
    w = [3, 4]
    r = dot (v, w)
    print (r)

def sum_of_squares_test():
    v = [1, 2, 3]
    r = sum_of_squares (v)
    print (r)

def magnitude_test ():
    v = [1, 2, 3]
    r = magnitude(v)
    print(r)

def distance_test ():
    u1 = [27, 80, 180]
    u2 = [58, 100, 198]
    u3 = [29, 79, 179]
    print (f'u1 vs u2: {distance(u1, u2)}')
    print (f'u1 vs u3: {distance(u1, u3)}')
    print(f'u2 vs u3: {distance(u2, u3)}')


def variance_test():
    v = [1, 2, 3]
    r = variance(v)
    print (r)

def covariance_tests():
    x = [3, 12, 3]
    y = [1, 7, 4]
    print(f'covariance: {covariance(x, y)}')
    x = [-1, 8, 11]
    y = [8, 2, 2]
    print (f'covariance: {covariance(x, y)}')
    x = [8, 6, 4]
    y = [2, 6, 4]
    print (f'covariance: {covariance(x, y)}')


def correlation_tests_with_table_data():
    x = [3, 12, 3]
    y = [1, 7, 4]
    print(f'correlation: {correlation(x, y)}')
    x = [-1, 8, 11]
    y = [8, 2, 2]
    print(f'correlation: {correlation(x, y)}')
    x = [8, 6, 4]
    y = [2, 6, 4]
    print(f'correlation: {correlation(x, y)}')

# Exercicios 6

def covariancia_idade_amigos():
    idades = [11, 18, 60]
    nro_amigos = [5, 8, 12]
    print(f'covariance: {covariance(idades, nro_amigos)}')


def correlacao_idade_amigos():
    idades = [11, 18, 60]
    nro_amigos = [5, 8, 12]
    print(f'correlation: {correlation(idades, nro_amigos)}')

def qtde_amigos_minutos_passados_v1 (n):
    lista_amigos = []
    lista_minutos = []

    for i in range(n):
        lista_amigos.append(random.randint(0, 1000))
    
    for item in lista_amigos:
        lista_minutos.append(item * 2)

    return (lista_amigos, lista_minutos)

def qtde_amigos_minutos_passados_v2 (n):
    lista_amigos = []
    lista_minutos = []
    aux = 0

    for i in range(n):
        lista_amigos.append(random.randint(0, 1000))
    
    for item in lista_amigos:
        aux = random.randint(1, 9)
        lista_minutos.append(item * -1)

    return (lista_amigos, lista_minutos)

def qtde_amigos_minutos_passados_v3 (n):
    lista_amigos = []
    lista_minutos = []
    aux = 0

    for i in range(n):
        lista_amigos.append(random.randint(0, 1000))
    
    for item in lista_amigos:
        aux = random.randint(0, 1)
        if aux == 1:
            lista_minutos.append(item / 2)
        else:
            lista_amigos.append(item * 2)
    
    return (lista_amigos, lista_minutos)

def correlation_tests_with_table_data_v1_v2_v3(n):

    teste1 = qtde_amigos_minutos_passados_v1 (n)
    print(f'correlation: {correlation(teste1[0], teste1[1])}')

    teste2 = qtde_amigos_minutos_passados_v2 (n)
    print(f'correlation: {correlation(teste2[0], teste2[1])}')

    teste3 = qtde_amigos_minutos_passados_v3 (n)
    print(f'correlation: {correlation(teste3[0], teste3[1])}')