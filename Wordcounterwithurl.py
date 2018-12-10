from urllib.request import urlopen

fd = urlopen("https://en.wikipedia.org/wiki/Fish")
counter = 0

for line in fd:
    line = line.decode() ##Transforma la pagina en string
    pos = 0

    while True:
        pos = line.find("the", pos) ##Empieza a buscar la palabra "the" en todas las lineas desde la 0


        if pos != 1: ## si no hay la palabra "the", pos da -1 entonces
            counter += 1## si no da -1, el counter suber uno
            pos += 1 ##sube la posicion y sigue leyendo


        else:
            break ##para acabar
print(counter)