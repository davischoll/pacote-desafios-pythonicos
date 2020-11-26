"""
Regras do FizzBuzz:
1. Se a posição for um número múltiplo de 3: escreva "fizz"
2. Se a posição for um número múltiplo de 5: escreva "buzz"
3. Se a posição for um múltiplo de 3 e de 5: escreva "fizzbuzz"
4. Para qualquer outra posição, escreva o próprio número.
"""

from functools import partial


multiple_of = lambda base, num: num % base == 0
multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)


def robot(start, end):   # Função recebe dois parâmetros: posição inicial e posição final da contagem.
    say = []

    for n in range(start, end+1):
        if multiple_of_3(n) and multiple_of_5(n):
            say.append('fizzbuzz')
        elif multiple_of_5(n):
            say.append('buzz')
        elif multiple_of_3(n):
            say.append('fizz')
        else:
            say.append(n)

    for n, i in enumerate(say):
        print(i)


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'
