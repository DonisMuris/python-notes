def valida_doc(num):
  if num < 10000 or num > 99999:
    return False

  a = num // 10000
  b = (num // 1000) % 10
  c = (num // 100) % 10
  d = (num // 10) % 10
  e = num % 10

  if (b**4) % 3 != 0 or (d**4) % 3 != 0:
    return False

  if c == 0 or c == 1:
    return False

  if c + e <= 3:
    return False

  if a != 2 and a != 5 and a != 9:
    return False

  return True

num1 = int(input('Digite o primeiro numero de documento: '))
num2 = int(input('Digite o segundo numero de documento: '))
num3 = int(input('Digite o terceiro numero de documento: '))

print(valida_doc(num1))
print(valida_doc(num2))
print(valida_doc(num3))
