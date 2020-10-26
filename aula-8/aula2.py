import math;
import random;
 
def scalar_multiply(escalar,vetor):
    return[escalar*i for i in vetor]
 
def vector_sum(vetores):
    resultado = vetores[0]
    for vetor in vetores[1:]:
        resultado = [resultado[i]+ vetor[i] for i in range(len(vetor))]
        return resultado 
 
def vector_mean(vetores):
    return scalar_multiply(1/len(vetores), vector_sum(vetores))
 
def dot (v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
 
def vector_subtract(v,w):
    return[v_i - w_i for v_i, w_i in zip(v,w)]
 
def sum_of_squares(v):
    return dot(v,v) 
 
def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v,w))
 
class KMeans:
    def __init__(self, k, means = None):
        self.k = k
        self.means = means
        def classify (self, ponto):
            return min(range(self.k), key = lambda i: squared_distance(ponto, self.means[i]) )
            def train(self,pontos):
                if self.means == None:
                    self.means = random.sample(pontos, self.k)
                    assignments = None
                    while True:
                        new_assigments = list (map(self.classify, pontos))
                        if new_assigments == assignments:
                            return
                            assignments = new_assigments 
                            for i in range (self.k):
                                i_points = [p for p, a in zip(pontos, assignments) if a ==i]
                                print(i_points)
                                if i_points:
                                    self.means[i] = vector_mean(i_points)
 
def test_k_means():
 dados = [[1], [3], [6], [7], [10], [11]]
 kmeans = KMeans(3)
 kmeans.train(dados)
 print (kmeans.means)
 
test_k_means()