
def oddremover(arg):
    for x in arg:
        if (x % 2) != 0:
            arg.remove(x)
    return arg

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista)
print(oddremover(lista))


