
#Tolerância de erro
tolerancia_de_erro: float = 1e-10

#Número máximo de interações
maximo_de_interacoes: int = 10000


#Pi
def computa_pi(termos: int = 1000) -> float:

    def serie_arctan(x: float, n: int) -> float:
        x2 = x * x
        termo = x
        resultado = 0.0
        sinal = 1
        for k in range(termos):
            resultado += sinal * termo / (2 * k + 1)
            termo *= x2
            sinal = -sinal
            if abs(termo) / (2 * k + 3) < tolerancia_de_erro * 1e-8:
                break
        return resultado

    return 4.0 * (4 * serie_arctan(1 / 5, termos) - serie_arctan(1 / 239, termos))

#Número de Euler
def computa_e(termos: int = 50) -> float:

    resultado = 0.0
    fatorial = 1
    for k in range(termos):
        if k > 0:
            fatorial *= k
        resultado += 1.0 / fatorial
    return resultado

#Phi
def computa_phi() -> float:

    x = 2.0
    for _ in range(100):
        x_new = (x + 5.0 / x) / 2.0
        if abs(x_new - x) < 1e-15:
            break
        x = x_new
    return (1.0 + x) / 2.0

#Epsilon
def computa_epsilon() -> float:

    epsilon = 1.0
    while 1.0 + epsilon / 2.0 != 1.0:
        epsilon /= 2.0
    return epsilon


#Constantes globais

pi: float = computa_pi()

e: float = computa_e()

phi: float = computa_phi()

tau: float = 2.0 * pi

inf: float = float("inf")

neg_inf: float = float("-inf")

nan: float = float("nan")

epsilon: float = computa_epsilon()

#Números usuais

ln2 = 0.6931471805599453

ln10 = 2.302585092994046
