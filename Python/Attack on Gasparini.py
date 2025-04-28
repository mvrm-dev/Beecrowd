num_tita, vida_muro = map(int, input().split())
titan_string = input()
tita_p, tita_m, tita_g = map(int, input().split())

lista_muros = [vida_muro]

i = 0

for titan in titan_string:
    if titan == "P":
        dano = tita_p
    elif titan == "M":
        dano = tita_m
    else: dano = tita_g

    if dano > lista_muros[i]:
        lista_muros.append(vida_muro - dano)
        lista_muros.sort()
        i+=1
    else:
        x = 0
        while x <= len(lista_muros)-1:
            if lista_muros[x] >= dano:
                lista_muros[x] -= dano
                break
            x+=1
    num_tita -= 1

print(len(lista_muros))