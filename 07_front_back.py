"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja ímpar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""


def front_back(a, b):
    """
    if len(a) % 2 == 0:
        a_frente = a[:int(len(a) / 2)]
        a_tras = a[int(len(a) / 2):]
    else:
        a_frente = a[:int(len(a) / 2 + 0.5)]
        a_tras = a[int(len(a) / 2 + 0.5):]

    if len(b) % 2 == 0:
        b_frente = b[:int(len(b) / 2)]
        b_tras = b[int(len(b) / 2):]
    else:
        b_frente = b[:int(len(b) / 2 + 0.5)]
        b_tras = b[int(len(b) / 2 + 0.5):]

    return ''.join([a_frente, b_frente, a_tras, b_tras])
    """

    a1, a2 = a[:len(a) // 2 + len(a) % 2], a[len(a) // 2 + len(a) % 2:]
    b1, b2 = b[:len(b) // 2 + len(b) % 2], b[len(b) // 2 + len(b) % 2:]
    return ''.join([a1, b1, a2, b2])


# --- Daqui para baixo são apenas códigos auxiliares de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
