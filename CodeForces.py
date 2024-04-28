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
