numeros = []

numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(5)


print(numeros)


numeros = [10, 20, 30]

numeros.insert(1, 15)

print(numeros)


lista = ["a", "b", "c"]


lista[2]='x'

print(lista)


lista = [5, 10, 15, 20]

del lista[2]
print(lista)


lista = ["maçã", "banana", "laranja"]

lista.remove("banana")

print(lista)


lista = [100, 200, 300, 400]

valor=lista.pop(3)
print(valor)

lista = ["python", "java", "c++"]

valor=lista.pop(1)
print(valor)

lista = [1,2,3,4,5]

lista.clear()
print(lista)

lista = ["a", "b", "d"]

lista.insert (2, "c")
lista.remove("a")

print(lista)


lista = [10, 20, 30, 40, 50]

lista.insert(5, 60)
lista.insert(1, 15)
lista.remove(30)

valor=lista.pop(5)


print(lista)
print(valor)
