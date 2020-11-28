"""
HappyNumbers
Como saber se um número é feliz ou triste?

Dado um número inteiro positivo, substitua o número pela soma dos quadrados dos seus dígitos.
Repita o processo até que o resultado seja 1, ou continue.
Os números que resultarem em 1, são felizes. Os que não resultarem em 1 são tristes.

Exemplo
O número 7 é feliz?

$7^2 = 49
$4^2 + 9^2 = 16 + 81 = 97
$9^2 + 7^2 = 81 + 49 = 130
$1^2 + 3^2 + 0^2 = 1 + 9 + 0 = 10
$1^2 + 0^2 = 1

7 é Feliz!

O número 4 é feliz?

$4^2 = 16
$1^2 + 6^2 = 1 + 36 = 37
$3^2 + 7^2 = 9 + 49 = 58
$5^2 + 8^2 = 25 + 64 = 89
$8^2 + 9^2 = 64 + 81 = 145
$1^2 + 4^2 + 5^2 = 1 + 16 + 25 = 42
$4^2 + 2^2 = 16 + 4 = 20
$2^2 + 0^2 = 4 + 0 = 4

4 não é feliz!
"""


def happy(num):
    next_ = sum(int(char) ** 2 for char in str(num))
    return num in (1, 7) if num < 10 else happy(next_)


assert all(happy(n) for n in (1, 10, 100, 130, 97))
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))
