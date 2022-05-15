import string
import random
import pandas
import math
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import contractions
import re

dfTrainingL = pandas.read_csv(
    r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\resultadosL.csv")
dfTrainingSW = pandas.read_csv(
    r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\resultadosSW.csv")
dfTrainingS = pandas.read_csv(
    r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\resultados.csv")

dfDiccLemas = pandas.read_csv(
    r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\diccLemas.csv")
dfDiccStop = pandas.read_csv(
    r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\diccStop.csv")
dfDiccStem = pandas.read_csv(
    r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\diccStem.csv")

dfTestingL = pandas.read_csv(r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\resultadosLT.csv")
dfTestingS = pandas.read_csv(r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\resultadosT.csv")
dfTestingSW = pandas.read_csv(r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\resultadosSWT.csv")

tpLemas = []
tpStop = []
tpStem = []

diccLemas = []
diccStop = []
diccStem = []

for z in range(len(dfDiccLemas)):
    word = dfDiccLemas['Word'].loc[z]
    diccLemas.append(word)

for x in range(len(dfDiccStop)):
    word = dfDiccStop['Word'].loc[x]
    diccStop.append(word)

for y in range(len(dfDiccStem)):
    word = dfDiccStem['Word'].loc[y]
    diccStem.append(word)

lLema1 = 0
lLema0 = 0
lStop1 = 0
lStop0 = 0
lStem1 = 0
lStem0 = 0

clase1 = 0
clase0 = 0

npcLemas1 = 0
npcLemas0 = 0

npcStop1 = 0
npcStop0 = 0

npcStem1 = 0
npcStem0 = 0

for i in range(0, 1500):
    texto = dfTrainingL['Text'].loc[i]
    clase = dfTrainingL['Class'].loc[i]
    values = {"Text": texto, "Class": clase}
    tpLemas.append(values)

    texto2 = dfTrainingSW['Text'].loc[i]
    clase2 = dfTrainingSW['Class'].loc[i]
    values = {"Text": texto2, "Class": clase2}
    tpStop.append(values)

    texto3 = dfTrainingS['Text'].loc[i]
    clase3 = dfTrainingS['Class'].loc[i]
    values = {"Text": texto3, "Class": clase3}
    tpStem.append(values)

    if clase == 1:
        npcLemas1 += len(texto.split())
        npcStop1 += len(texto2.split())
        npcStem1 += len(texto3.split())

        lLema1 += len(texto)
        lStop1 += len(texto2)
        lStem1 += len(texto3)
        clase1 += 1
    else:
        npcLemas0 += len(texto.split())
        npcStop0 += len(texto2.split())
        npcStem0 += len(texto3.split())

        clase0 += 1
        lLema0 += len(texto)
        lStop0 += len(texto2)
        lStem0 += len(texto3)

tpLemasTest = []
tpStopTest = []
tpStemTest = []

for i in range(0, 500):
    texto = dfTestingL['Text'].loc[i]
    clase = dfTestingL['Class'].loc[i]
    values = {"Text": texto, "Class": clase}
    tpLemasTest.append(values)

    texto2 = dfTestingSW['Text'].loc[i]
    clase2 = dfTestingSW['Class'].loc[i]
    values = {"Text": texto2, "Class": clase2}
    tpStopTest.append(values)

    texto3 = dfTestingS['Text'].loc[i]
    clase3 = dfTestingS['Class'].loc[i]
    values = {"Text": texto3, "Class": clase3}
    tpStemTest.append(values)

"""
print(tpLemas)
print(tpStop)
print(tpStem)
print("\n")
print("Longitud promedio de textos por clase 1 / Lemas= " + str(lLema1 / clase1) + " clase 0= " + str(lLema0 / clase0))
print("Longitud promedio de textos por clase 1 / Stopwords= " + str(lStop1 / clase1) + " clase 0= " + str(lStop0 / clase0))
print("Longitud promedio de textos por clase 1 / Steeming= " + str(lStem1 / clase1) + " clase 0= " + str(lStem0 / clase0))

print("Numero de palabras por clase 0 Lemas= " + str(npcLemas0) + " clase 1= " + str(npcLemas1))
print("Numero de palabras por clase 0 Stopwords= " + str(npcStop0) + " clase 1= " + str(npcStop1))
print("Numero de palabras por clase 0 Steeming= " + str(npcStem0) + " clase 1= " + str(npcStem1))


print("\n\n\n\n\n")
"""
"""
#Lemas
b=[]
for i in range(len(tpLemas)):
    a = []
    textoRevisar = tpLemas[i]['Text'].split()
    for j in range(len(textoRevisar)):
        for k in range(len(diccLemas)):
            a.append(0)
            if diccLemas[k] == textoRevisar[j]:
                a[k] += 1
    b.append(a)

f=[]
for j in range(len(tpLemas)):
    for k in range(len(diccLemas)):
        d = tpLemas[j]
        g = diccLemas[k]
        h = b[j][k]

        d[g] = h
    f.append(d)

output = pandas.DataFrame()
output = output.append(f, ignore_index=True)
output.to_csv(r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\resultadosFinalesLemas.csv",
               index=False)
print(output.head())

#Stopwords
b=[]
for i in range(len(tpStop)):
    a = []
    textoRevisar = tpStop[i]['Text'].split()
    for j in range(len(textoRevisar)):
        for k in range(len(diccStop)):
            a.append(0)
            if diccStop[k] == textoRevisar[j]:
                a[k] += 1
    b.append(a)

f=[]

for j in range(len(tpStop)):
    for k in range(len(diccStop)):
        d = tpStop[j]
        g = diccStop[k]
        h = b[j][k]

        d[g] = h
    f.append(d)

output2 = pandas.DataFrame()
output2 = output2.append(f, ignore_index=True)
output2.to_csv(r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\resultadosFinalesStop.csv",
               index=False)
print(output2.head())

#Steeming
b=[]
for i in range(len(tpStem)):
    a = []
    textoRevisar = tpStem[i]['Text'].split()
    for j in range(len(textoRevisar)):
        for k in range(len(diccStem)):
            a.append(0)
            if diccStem[k] == textoRevisar[j]:
                a[k] += 1
    b.append(a)

f=[]

for j in range(len(tpStem)):
    for k in range(len(diccStem)):
        d = tpStem[j]
        g = diccStem[k]
        h = b[j][k]

        d[g] = h
    f.append(d)

output3 = pandas.DataFrame()
output3 = output3.append(f, ignore_index=True)
output3.to_csv(r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\resultadosFinalesStem.csv",
               index=False)
print(output3.head())
"""

r=[]

b=[]
for i in range(len(tpLemasTest)):
    a = []
    textoRevisar = tpLemasTest[i]['Text'].split()
    for j in range(len(textoRevisar)):
        for k in range(len(diccLemas)):
            a.append(0)
            if diccLemas[k] == textoRevisar[j]:
                a[k] += 1
    b.append(a)

for p in range(len(tpLemasTest)):
    for k in range(len(diccLemas)):
        d = tpLemasTest[p]
        g = diccLemas[k]
        h = b[p][k]

        d[g] = h
    r.append(d)

output4 = pandas.DataFrame()
output4 = output4.append(r, ignore_index=True)
output4.to_csv(r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\resultadosFinalesLemasTest.csv",
               index=False)
print(output4.head())

s = []

b=[]
for i in range(len(tpStopTest)):
    a = []
    textoRevisar = tpStopTest[i]['Text'].split()
    for j in range(len(textoRevisar)):
        for k in range(len(diccStop)):
            a.append(0)
            if diccStop[k] == textoRevisar[j]:
                a[k] += 1
    b.append(a)


for p in range(len(tpStopTest)):
    for k in range(len(diccStop)):
        d = tpStopTest[p]
        g = diccStop[k]
        h = b[p][k]

        d[g] = h
    s.append(d)

output5 = pandas.DataFrame()
output5 = output5.append(s, ignore_index=True)
output5.to_csv(
    r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\resultadosFinalesStopTest.csv",
    index=False)
print(output5.head())


t = []

b=[]
for i in range(len(tpStemTest)):
    a = []
    textoRevisar = tpStemTest[i]['Text'].split()
    for j in range(len(textoRevisar)):
        for k in range(len(diccStem)):
            a.append(0)
            if diccStem[k] == textoRevisar[j]:
                a[k] += 1
    b.append(a)

for p in range(len(tpStemTest)):
    for k in range(len(diccStem)):
        d = tpStemTest[p]
        g = diccStem[k]
        h = b[p][k]

        d[g] = h
    t.append(d)

output6 = pandas.DataFrame()
output6 = output6.append(t, ignore_index=True)
output6.to_csv(
    r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\resultadosFinalesStemTest.csv",
    index=False)
print(output6.head())




"""
print(diccLemas)
print(str(len(diccLemas)))
print(diccStop)
print(str(len(diccStop)))
print(diccStem)
print(str(len(diccStem)))
"""
