height_weight_age =[
    170,
    70,
    40
]

grades = [
    95,
    90,
    75,
    62
]

def vector_add(v, w):
    #v = [1, 2, 3]
    #w = [4, 5, 6]
    #zip (v, w) = [(1, 4), (2, 5), (3, 6)]
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_add_test():
    v = [5,4]
    w = [2,1]
    r = vector_add(v,w)
    print(r)

def vector_subtract(v,w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_subtract_test(v,w):
    v=[5,4]
    w=[2,1]
    r=vector_subtract(v,w)
    print(r)

def vector_sum(vectors):
    result=vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result,vector)
        return result

def vector_sum_test():
    v1=[1,2,5,6]
    v2=[4,3,2,1]
    v3=[1,1,1,1]
    r=vector_sum([v1,v2,v3])
    print(r)

def scalar_multiply(c,v):
    return [c*v_i for v_i in v]

def scalar_multiply_test():
    c=5
    v=[4,1,2,5]
    r=scalar_multiply(c,v)
    print(r)

def main():
    scalar_multiply_test()
    #vector_sum_test()
    #vector_subtract_test()
    #vector_add_test()

main()