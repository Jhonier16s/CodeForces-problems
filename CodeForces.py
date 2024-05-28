""" line = input("Introduce dos números separados por espacio: ")
parts = line.split(" ")
m = int(parts[0])
n = int(parts[1])

result = 0
if n >= m:
    result = (n * m) // 2

print(result) """

""" def convertir_a_numeracion_egipcia(numero):
    simbolos = ['H', 'R', 'D', 'F', 'C', 'G', 'T']
    potencias = [1000000, 100000, 10000, 1000, 100, 10, 1]
    numeracion_egipcia = ''

    for i in range(len(simbolos)):
        cantidad = numero // potencias[i]
        if cantidad > 0:
            numeracion_egipcia += simbolos[i] * cantidad
            numero %= potencias[i]

    return numeracion_egipcia

print(convertir_a_numeracion_egipcia(15))  
print(convertir_a_numeracion_egipcia(200))  
print(convertir_a_numeracion_egipcia(1922))  """


# Petya and Strings
""" str = input().strip().lower()
str_2 = input().strip().lower()

if str > str_2:
    print(1)
elif str == str_2:
    print(0)
else:
    print(-1)
 """

# A. Helpful Maths

""" stri = input()
arr = []
result_arr = []

for i in range(len(stri)):
    if stri[i] != "+":
        arr.append(stri[i])

arr.sort()
for i in range(len(arr)):
    result_arr.append(arr[i])
    result_arr.append("+")

result_cadena = "".join(map(str, result_arr))
print(result_cadena[:-1]) """

# way too long
""" n = int(input())

for _ in range(n):
    word = input()

    if len(word) > 10:
        abbreviated = word[0] + str(len(word) - 2) + word[-1]
        print(abbreviated)
    else:
        print(word) """


# A. Boy or Girl

""" user = input()
repeated_letters = set()

for letter in user:
    if letter not in repeated_letters:
        repeated_letters.add(letter)

if len(repeated_letters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

print(repeated_letters)
 """

# A - Bear and Big Brother
""" weight = input()
weightArr = weight.split(" ")

a = int(weightArr[0])
b = int(weightArr[1])
count = 0

if a <= b:

    while a <= b:
        a = a * 3
        b = b * 2
        count += 1

print(count) """

# A. Stones on the Table

""" 
n = int(input())
stones = input()


count = 0
prev_color = stones[0]


for color in stones[1:]:
    if color == prev_color:
        count += 1
    prev_color = color


print(count) """


##A. Word
""" 
word = str(input())

countMAY = 0


for i in word:
    if i.isupper():
        countMAY += 1


if countMAY > len(word) - countMAY:
    print(word.upper())
else:
    print(word.lower()) """

##Kaprekar
""" number = int(input())

square = number * number
squarestr = str(square)

if len(squarestr) % 2 == 0:
    fisrtPart = squarestr[0 : int(len(squarestr) / 2)]
    secondPart = squarestr[int(len(squarestr) / 2) :]

    sum = int(fisrtPart) + int(secondPart)

    if sum == number:
        print("KAPREKAR")
    else:
        print("NO KAPREKAR") """

# Reversible

""" number = input()

numberReversed = number[::-1]
counter = 0

sum = int(number) + int(numberReversed)

if len(str(sum)) % 2 == 0:

    for i in str(sum):
        if int(i) % 2 != 0:
            counter += 1


print(counter)
print(sum)
print("Reversible" if counter == len(str(sum)) else "No reversible") """

# Cuadrado doblado

""" matrix = [[], [], []] """

# Reto - Velas geeek
""" number = int(input())
binary = bin(number)[2:]
reverse = str(binary[::-1])

print("Reversible" if binary == reverse else "No reversible") """

# Wrong Subtraction

""" stri = input()

n = int(stri.split(" ")[0])
k = int(stri.split(" ")[1])

for i in range(k):

    lastDigit = n % 10

    if lastDigit == 0:
        n = n // 10
    else:
        n -= 1

print(n) """

# 110A - Nearly Lucky Number
""" number = input()
count = 0

for i in number:
    if i in "47":
        count += 1

print("YES" if count == 4 or count == 7 else "NO") """

# desencripted maraton
""" p = input().split(" ")
word = ""

for i in p:
    word += chr(int(i))

print("P: ", word) """


# raiz
""" m = float(input("Digite un valor: "))
g1, g2 = 0, m / 2.0
while g1 != g2:
    print("g1", g1)
    print("g2", g2)
    g1 = g2
    g2 = (g1 + m / g1) / 2.0
print(g2) """


# Cuadraro perfecto

""" filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))


matriz = []


print("Valores ingresados:")
for i in range(filas):
    fila = list(map(int, input().split()))
    matriz.append(fila)


print("La matriz ingresada es:")
for fila in matriz:
    print(fila)


suma_total = sum(sum(fila) for fila in matriz)
max_valor = max(max(fila) for fila in matriz)


if (suma_total - max_valor) == max_valor:
    print("Salida: SI")
else:
    print("Salida: NO") """


# A. Anton and Danik

""" number = input()
text = input()

anton = sum(1 for i in text if "A" in i)
danik = sum(1 for i in text if "D" in i)

if anton > danik:
    print("Anton")
elif anton == danik:
    print("Friendship")
else:
    print("Danik") """

# A. Translation
""" 

    word = input()
    wordTranslated = input()
     
    if word[::-1] == wordTranslated:
        print("YES")
    else:
        print("NO") """


# Tram

""" number = int(input())
pasaj = 0
pasajArr = []

for i in range(number):
    nums = list(input().split(" "))
    num1 = int(nums[0])
    num2 = int(nums[1])

    pasaj = (pasaj + num2) - num1
    pasajArr.append(pasaj)

print(max(pasajArr)) """


# A. Vanya and Fence

""" line = list(input().split(" "))

persons = line[0]
maxHeigt = line[1]
countWidht = 0

personsHeigts = list((input().split(" ")))

for i in personsHeigts:
    if int(i) > int(maxHeigt):
        countWidht += 2
    else:
        countWidht += 1

print(countWidht) """

# A. Beautiful Year
""" year = int(input())
while True:
    year += 1
    if len(set(str(year))) == len(str(year)):
        print(year)
        break """


#  Queue at the School

""" n, t = map(int, input().split())
s = input().strip()


queue = list(s)


for _ in range(t):
    i = 0

    while i < n - 1:

        if queue[i] == "B" and queue[i + 1] == "G":

            queue[i], queue[i + 1] = queue[i + 1], queue[i]
            i += 2
        else:
            i += 1


result = "".join(queue)


print(result) """

# A. In Search of an Easy Problem

""" persons = int(input())
validation = 0


difficulties = input().split()

for i in range(persons):

    difficulty = int(difficulties[i])

    if difficulty == 1:
        validation = 1

print("HARD" if validation == 1 else "EASY") """


# A. Calculating Function

""" n = int(input())

if n % 2 == 0:
    print(n // 2)
else:
    print(-(n // 2 + 1)) """


# A. George and Accommodation

""" rooms = int(input())
count = 0

for digit in range(rooms):
    line = input().split(" ")
    persons = line[0]
    capicity = line[1]

    if (int(persons) + 2) <= int(capicity):
        count += 1

print(count) """

# A. Magnets

""" number = int(input())
arr = []

count = 1

for n in range(number):
    arr.append(input())


for n in range(len(arr)):
    if arr[n] != arr[n - 1]:
        count += 1


print(count)
 """

# B. Drinks

""" number = int(input())


juiceTotal = input().split(" ")

juiceTotal = sum(list(map(int, juiceTotal)))

print(juiceTotal / number) """

# A. Ultra-Fast Mathematician

""" number_one = input()
number_two = input()

arrAnswer = []

for index, i in enumerate(number_one):
    if i == number_two[index]:
        arrAnswer.append("0")
    else:
        arrAnswer.append("1")

print("".join(arrAnswer)) """

# A. Ultra-Fast Mathematician whit zip

""" number_one = input()
number_two = input()


arrAnswer = []


for x, y in zip(number_one, number_two):
    if x == y:
        arrAnswer.append("0")
    else:
        arrAnswer.append("1")


answer_string = "".join(arrAnswer)

print(answer_string) """


# A. Is your horseshoe on the other hoof?

""" number = list(input().split(" "))

unico = list(set(number))

print(len(number) - len(unico)) """


# Reto - La serie de Leibniz
""" 
number = int(input())
result = 0


for n in range(number):

    aprox = (-1) ** n / (2 * n + 1)
    result += aprox

result *= 4
print(result) """


# Reto - Palabras pentavocálicas

""" s = input().lower()
condition = 0

if "a" in s and "e" in s and "i" in s and "o" in s and "u" in s:
    condition += 1


print("SI" if condition == 1 else "NO") """


""" # Reto - Palabras pentavocálicas


palabra = input("Ingrese una palabra: ").lower()


if set('aeiou').issubset(palabra):
    print("SI")
else:
    print("NO") """


# Reto - Series de Taylor


# Lectura del ángulo en grados
""" angle_degrees = float(input("Ingrese el ángulo en grados: "))

radians = angle_degrees * 3.1415926535897932384626433832795 / 180

iterations = 10


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


sin_approximation = 0
for n in range(iterations):
    term = ((-1) ** n) * (radians ** (2 * n + 1)) / factorial(2 * n + 1)
    print(term, "term")
    sin_approximation += term

print("Aproximación del seno de", angle_degrees, "grados:", sin_approximation)

import math

angulo_grados = float(input("Ingrese el ángulo en grados: "))


angulo_radianes = math.radians(angulo_grados)


seno = math.sin(angulo_radianes)

print("El seno de", angulo_grados, "grados es:", seno) """


# A. Hulk

""" num = int(input())

st = ""

for n in range(1, num + 1):
    if n % 2 == 0:
        if n == num:
            st += "I love it "
        else:
            st += "I love that "
    else:
        if n == num:
            st += "I hate it "
        else:
            st += "I hate that "


print(st) """

#  	1328A - Divisibility Problem

""" ite = int(input())

results = []


for _ in range(ite):

    a, b = map(int, input().split())

    remainder = a % b

    if remainder == 0:
        moves_needed = 0
    else:

        moves_needed = b - remainder

    results.append(moves_needed)


for result in results:
    print(result) """


# A. I Wanna Be the Guy
""" ite = int(input())

firstLine = input().split()[1:]
secondLine = input().split()[1:]
print(firstLine)
print(secondLine)
levels = set(firstLine + secondLine)

print(levels)

if len(levels) == ite:
    print("I become the guy.")
else:
    print("Oh, my keyboard!") """

# Acepta el reto

# Ventas
""" 
ven = []
max = 0
min = 0
prom = 0
indexMax = 0
indexMin = 0
days = ["MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO", "LUNES"]

for n in range(0, 7):
    day = float(input())
    if day > max:
        max = day
        indexMax = n
    if n == 0:
        min = day
    else:
        if day < min and day != -1.0:
            min = day
            indexMin = n
    ven.append(day)

pro = 0

for n in range(0, 4):
    pro += ven[n]

pro = pro / 4

print(max(ven))
print(min(ven))

if days[indexMax] != days[indexMin]:
    print(days[indexMax], days[indexMin], "SI" if ven[5] > pro else "NO")
else:
    print("EMPATE") """


# Coin ganes


# Número de casos de prueba
""" t = int(input())

results = []

for _ in range(t):
    n = int(input())
    coins = input()

    count_U = coins.count("U")

    if count_U % 2 == 1:
        results.append("YES")
    else:
        results.append("NO")

for result in results:
    print(result) """


# A. Pangram

""" import string

number = int(input())
st = input().lower()

alp = list(map(chr, range(97, 123)))
alphabet = list(string.ascii_lowercase)  # alpphabet
stUnique = list(set(st))

count = 0


for d in stUnique:
    if d in stUnique:
        count += 1

print("YES" if len(alp) == count else "NO") """


# A. Arrival of the General

""" num = int(input())


hs = list(map(int, input().split()))


maxNumber = max(hs)
minNumber = min(hs)


indexMax = hs.index(maxNumber)


indexMin = len(hs) - 1 - hs[::-1].index(minNumber)


if indexMin < indexMax:

    position = indexMax + (num - 1 - indexMin) - 1
else:
    position = indexMax + (num - 1 - indexMin)

print(position) """


# A. Hit the Lottery


# A. Anton and Letters

""" 
line = input()[1:-1].split(",")
arr = []
validation = False

for n in line:
    if type(n) == str and n == "":
        validation = True
    arr.append(n.strip())


setVar = list(set(arr))

print(0 if validation else len(setVar))
 """

# Objs
""" number = int(input(""))

obj = {1: "T", 10: "G", 100: "C", 1000: "F", 10000: "D", 100000: "R", 1000000: "H"}

items_invertidos = list(obj.items())[::-1]

result = ""

for key, value in items_invertidos:
    cantidad = number // key
    result += value * cantidad
    number -= key * cantidad

print(result) """

# tuples
""" number = int(input(""))

obj = [
    (1, "T"),
    (10, "G"),
    (100, "C"),
    (1000, "F"),
    (10000, "D"),
    (100000, "R"),
    (1000000, "H"),
]

items_invertidos = obj[::-1]

result = ""

for key, value in items_invertidos:
    cantidad = number // key
    result += value * cantidad
    number -= key * cantidad

print(result) """

# LISTS

""" number = int(input(""))

keys = [1, 10, 100, 1000, 10000, 100000, 1000000]
values = ["T", "G", "C", "F", "D", "R", "H"]

keys_invertidos = keys[::-1]
values_invertidos = values[::-1]

result = ""

for i in range(len(keys_invertidos)):
    key = keys_invertidos[i]
    value = values_invertidos[i]
    cantidad = number // key
    result += value * cantidad
    number -= key * cantidad

print(result) """

""" s = "hello, world!"
print(s[-1]) """

""" fig = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}

num = int(input())

result = 0

for n in range(num):
    st = input()
    result += fig[st]


print(result) """


""" def generar_matriz(palabra):
    # Validación de la entrada
    if not palabra or not palabra.isalpha() or len(palabra) < 3:
        raise ValueError(
            "La palabra debe tener al menos 3 letras y no contener espacios."
        )

    # Longitud de la palabra
    n = len(palabra)

    # Crear matriz vacía de tamaño n x n
    matriz = [["" for _ in range(n)] for _ in range(n)]

    # Colocar la palabra en la diagonal principal
    for i in range(n):
        matriz[i][i] = palabra[i]

    # Caracteres para la zona 1 (A-M) y zona 2 (N-Z)
    zona1_chars = iter("abcdefghijklm")
    zona2_chars = iter("nopqrstuvwxyz")

    # Rellenar la matriz según las zonas
    for i in range(n):
        for j in range(n):
            if i < j:
                # Zona 1
                matriz[i][j] = next(zona1_chars)
                # Reiniciar el iterador si se agotan los caracteres
                if matriz[i][j] == "m":
                    zona1_chars = iter("abcdefghijklm")
            elif i > j:
                # Zona 2
                matriz[i][j] = next(zona2_chars)
                # Reiniciar el iterador si se agotan los caracteres
                if matriz[i][j] == "z":
                    zona2_chars = iter("nopqrstuvwxyz")

    # Selección de los generales (3 primeros caracteres de cada zona)
    generales_zona1 = [matriz[i][j] for i in range(n) for j in range(n) if i < j][:3]
    generales_zona2 = [matriz[i][j] for i in range(n) for j in range(n) if i > j][:3]

    return matriz, generales_zona1, generales_zona2


# Ejemplo de uso
palabra = "hola"
matriz, generales_zona1, generales_zona2 = generar_matriz(palabra)

print("Matriz:")
for fila in matriz:
    print(" ".join(fila))

print("Generales zona 1:", generales_zona1)
print("Generales zona 2:", generales_zona2)
 """
