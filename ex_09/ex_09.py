def funcao_9(t, n):
    termo_inicial = t
    razao = n + 1

    while True:
            print(termo_inicial)
            termo_inicial = termo_inicial + razao
            razao += 1

print(funcao_9(1, 1))