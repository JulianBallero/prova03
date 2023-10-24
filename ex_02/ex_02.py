def funcao_2(a, r):

    print(a)
    a = a ** r
    print(a)

    return funcao_2(a)

print(funcao_2(2, 2))