with open("E:\Kraskal1.txt","r") as file:
    massif = file.readlines()

N = int(massif[0])
del massif[0]


#создание массива из файла
massif = [[int(n) for n in x.split()] for x in massif]

#количество столбцов
Len = len(massif[0])

#Список кортежей
Massif = []
for j in range (Len):
    Massif.append([str(massif[0][j]), massif[1][j]])

#Сортировка кортежей по весу
Massif.sort(key = lambda x: x[1])

summa = 0

#множество вершин
ver = []

ver.append(Massif[0][0])
summa += Massif[0][1]
k = 1

del(Massif[0])

for tup in Massif:
    for index in range(len(ver)):
        if tup[0][0] in ver[index] and tup[0][1] in ver[index]:
            break
        elif tup[0][0] in ver[index] and not(tup[0][1] in ver[index]):
            ver[index] += tup[0][1]
            summa += tup[1]
        elif tup[0][1] in ver[index] and not(tup[0][0] in ver[index]):
            ver[index] += tup[0][0]
            summa += tup[1]
        elif not(tup[0][0] in ver[index]) and not(tup[0][1] in ver[index]):
            if len(ver) == 1:
                ver.append(tup[0])
                summa += tup[1]
            else:
                for index_1 in range (1,len(ver)):
                    if not(tup[0][0] in ver[index_1]) and not(tup[0][1] in ver[index_1]):
                        ver.append(tup[0])
                        summa += tup[1]
                    else:
                        if tup[0][0] in ver[index_1] and not(tup[0][1] in ver[index_1]):
                            ver[index_1] += tup[0][1]
                            summa += tup[1]
                        elif tup[0][1] in ver[index_1] and not(tup[0][0] in ver[index_1]):
                            ver[index_1] += tup[0][0]
                            summa += tup[1]
    for index in range (len(ver)):
        for index_1 in range (index+1, len(ver)):
            if tup[0][0] in ver[index_1] and tup[0][0] in ver[index]:
                ver[index_1] = ver[index_1].replace(tup[0][0],'')
                ver[index_1] = ver[index_1].replace(tup[0][1],'')
                ver[index] += ver[index_1]
                ver.remove(ver[index_1])
                summa -= tup[1]
                break

print(summa)

