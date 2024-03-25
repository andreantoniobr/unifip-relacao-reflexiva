def testa_se_e_reflexiva(a, b):
    return (a + 3 * b) % 4 == 0

def gera_pares_da_relacao(range_number):
    relacao = []
    for x in range(range_number):
        if(testa_se_e_reflexiva(x, x)):
            par = f"({x},{x})"
            relacao.append(par)
    return relacao

def imprime_valores_da_relacao(range_number):
    pares = gera_pares_da_relacao(range_number)
    relacao = "R={"
    quantidade_de_pares = len(pares)
    for i in range(quantidade_de_pares):
        relacao += pares[i]
        if(i < quantidade_de_pares - 1):
            relacao += ","
    relacao += "}"
    print(relacao)

def main():
    quantidade_de_pares_exemplo = int(input())
    imprime_valores_da_relacao(quantidade_de_pares_exemplo)

main()