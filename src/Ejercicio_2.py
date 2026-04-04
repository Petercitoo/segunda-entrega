def crearLista(playlist):
    lista=[]

    for song in playlist:
        lista.append(song["duration"].split(":"))
    return lista


def minSegs(ms):
    totM = 0
    totS = 0
    for i in ms:
        totM += int(i[0])
        totS += int(i[1])

    totM += totS//60
    totS = totS%60

    return totM, totS

def minMax(ms,playlist):
    maximo = -1
    minimo = float('inf')
    for index, song in enumerate(ms):
        totalsong = int(song[0]) * 60 + int(song[1])
        if totalsong>maximo:
            maxDuration = playlist[index]["duration"]
            cancionMax = playlist[index]["title"]
            maximo = totalsong
        if totalsong<minimo:
            minDuration = playlist[index]["duration"]
            cancionMin = playlist[index]["title"]
            minimo = totalsong
    return cancionMin, minDuration, cancionMax, maxDuration
