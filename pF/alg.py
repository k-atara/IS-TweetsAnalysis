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

dfTraining = pandas.read_csv(
    r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\TrainingDS.csv")
dfTesting = pandas.read_csv(
    r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\TestingDS.csv")
textosT = []
textosProcesados = []

for i in range(0, 1500):
    textos = dfTraining['Text'].loc[i]
    textosT.append(textos)

for i in range(0, 500):
    textosTesting = dfTesting['Text'].loc[i]
    textosT.append(textosTesting)


# ------------------------------------------------PREPROCESAMIENTOS------------------

def contractions_word(text):
    # creating an empty list
    expanded_words = []
    for word in text.split():
        # using contractions.fix to expand the shotened words
        expanded_words.append(contractions.fix(word))

    expanded_text = ' '.join(expanded_words)
    return expanded_text


# Text to lowercase and remove punctuation
def text_lowercase_and_remove_punctuation(text):
    out = ''.join([i for i in text if i not in string.punctuation]).lower()
    return out


# Remove default stopwords
# remove stopwords function
def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    expanded_text = ' '.join(filtered_text)
    return expanded_text


# Lemmatization
lemmatizer = WordNetLemmatizer()


# lemmatize string
def lemmatize_word(text):
    word_tokens = word_tokenize(text)
    # provide context i.e. part-of-speech
    lemmas = [lemmatizer.lemmatize(word, pos='v') for word in word_tokens]
    expanded_text = ' '.join(lemmas)
    return expanded_text


def stemming_word(input_str):
    stemmer = PorterStemmer()
    expanded_words = []
    input_str = word_tokenize(input_str)
    for word in input_str:
        expanded_words.append(stemmer.stem(word))
    expanded_text = ' '.join(expanded_words)
    return (expanded_text)


# -------------------------------------------------------FIN FUNCIONES

arrTextosLemas = []
arrTextosStopW = []
arrTextosStem = []

for t in range(len(textosT)):
    tweet = re.sub(r'#\w+|&\w+|@\w+|\w+@\w+.com|\w+@\w+.es', " ", textosT[t])
    # print("Tweet", tweet)
    textoF = contractions_word(tweet)
    # print("TextoF", textoF)
    textosProcesados.append(text_lowercase_and_remove_punctuation(textoF))
    # print("TextoP", textosProcesados[t])

textosProcesadosLemas = textosProcesados
textosProcesadosStopWords = textosProcesados
textosProcesadosSteeming = textosProcesados

# Preprocesamiento, guardar oraciones preprocesadas
for t in range(len(textosProcesados)):
    arrTextosLemas.append(lemmatize_word(textosProcesadosLemas[t]))
    arrTextosStopW.append(remove_stopwords(textosProcesadosStopWords[t]))
    arrTextosStem.append(stemming_word(textosProcesadosSteeming[t]))

res = pandas.DataFrame()
res2 = pandas.DataFrame()
res3 = pandas.DataFrame()
"""
for k in range(1500):
    # print(textosRP[k])
    # id = dfTraining['ID'].loc[k]
    clase = dfTraining['Class'].loc[k]

    resultadosL = pandas.DataFrame(
        {'Text': [arrTextosLemas[k]], 'Class':[clase]})
    res = res.append(resultadosL)
    res.to_csv(r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\ nueva clase\p3\pF\Salidas\ resultadosL.csv",
               index=False)
    res = pandas.read_csv(
        r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\ nueva clase\p3\pF\Salidas\ resultadosL.csv")

    resultadosStem = pandas.DataFrame(
        {'Text': [arrTextosStem[k]], 'Class':[clase]})

    res2 = res2.append(resultadosStem)
    res2.to_csv(r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\ nueva clase\p3\pF\Salidas\ resultados.csv",
                index=False)
    res2 = pandas.read_csv(
        r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\ nueva clase\p3\pF\Salidas\ resultados.csv")

    resultadosSW = pandas.DataFrame(
        {'Text': [arrTextosStopW[k]], 'Class':[clase]})

    res3 = res3.append(resultadosSW)
    res3.to_csv(r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\ nueva clase\p3\pF\Salidas\ resultadosSW.csv",
                index=False)
    res3 = pandas.read_csv(
        r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\ nueva clase\p3\pF\Salidas\ resultadosSW.csv")
"""
"""
for l in range(1500, 2000):
    resultadosL = pandas.DataFrame(
        {'Text': [arrTextosLemas[l]], 'Class': ["?"]})
    res = res.append(resultadosL)
    res.to_csv(r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\ nueva clase\p3\pF\Salidas\ resultadosLT.csv",
               index=False)
    res = pandas.read_csv(
        r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\ nueva clase\p3\pF\Salidas\ resultadosLT.csv")

    resultadosStem = pandas.DataFrame(
        {'Text': [arrTextosStem[l]], 'Class': ["?"]})

    res2 = res2.append(resultadosStem)
    res2.to_csv(r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\ nueva clase\p3\pF\Salidas\ resultadosT.csv",
                index=False)
    res2 = pandas.read_csv(
        r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\ nueva clase\p3\pF\Salidas\ resultadosT.csv")

    resultadosSW = pandas.DataFrame(
        {'Text': [arrTextosStopW[l]], 'Class': ["?"]})

    res3 = res3.append(resultadosSW)
    res3.to_csv(
        r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\ nueva clase\p3\pF\Salidas\ resultadosSWT.csv",
        index=False)
    res3 = pandas.read_csv(
        r"C:\ Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\ nueva clase\p3\pF\Salidas\ resultadosSWT.csv")
"""
diccStem = []
diccStop = []
diccLema = []

# temporales para sacar frecuencias
diccStemTemp = []
diccStopTemp = []
diccLemaTemp = []

listaPalabrasLema = []
listaPalabrasStop = []
listaPalabrasStem = []


def dictFind(palabra, dic):
    for k in range(len(dic)):
        if dic[k]['Text'] == palabra:
            return True
    return False


def dictPos(palabra, dic):
    for k in range(len(dic)):
        if dic[k]['Text'] == palabra:
            return k
    return 0


for i in range(len(textosProcesados)):
    listaPalabrasLema = arrTextosLemas[i].split()
    listaPalabrasStop = arrTextosStopW[i].split()
    listaPalabrasStem = arrTextosStem[i].split()

    for j in range(len(listaPalabrasLema)):
        if not dictFind(listaPalabrasLema[j], diccLemaTemp):
            values = {"Text": listaPalabrasLema[j], "Frec": 1}
            diccLemaTemp.append(values)
        else:
            pos = dictPos(listaPalabrasLema[j], diccLemaTemp)
            diccLemaTemp[pos]['Frec'] += 1

    for k in range(len(listaPalabrasStop)):
        if not dictFind(listaPalabrasStop[k], diccStopTemp):
            values = {"Text": listaPalabrasStop[k], "Frec": 1}
            diccStopTemp.append(values)
        else:
            pos = dictPos(listaPalabrasStop[k], diccStopTemp)
            diccStopTemp[pos]['Frec'] += 1

    for l in range(len(listaPalabrasStem)):
        if not dictFind(listaPalabrasStem[l], diccStemTemp):
            values = {"Text": listaPalabrasStem[l], "Frec": 1}
            diccStemTemp.append(values)
        else:
            pos = dictPos(listaPalabrasStem[l], diccStemTemp)
            diccStemTemp[pos]['Frec'] += 1

for u in range(len(diccLemaTemp)):
    if diccLemaTemp[u]['Frec'] > 10:
        diccLema.append(diccLemaTemp[u]['Text'])

for v in range(len(diccStopTemp)):
    if diccStopTemp[v]['Frec'] > 10:
        diccStop.append(diccStopTemp[v]['Text'])

for w in range(len(diccStemTemp)):
    if diccStemTemp[w]['Frec'] > 10:
        diccStem.append(diccStemTemp[w]['Text'])

print("Vocabulario Lematizados\n")
print(diccLema)
print(len(diccLema))
print("Vocabulario Stop words\n")
print(diccStop)
print(len(diccStop))
print("Vocabulario Steeming\n")
print(diccStem)
print(len(diccStem))

print("Numero de instancias (Training): " + str(len(dfTraining)))
print("Numero de instancias (Testing): " + str(len(dfTesting)))

resDicc1 = pandas.DataFrame()
resDicc2 = pandas.DataFrame()
resDicc3 = pandas.DataFrame()


for m in range(len(diccLema)):
    resultado = pandas.DataFrame({'Word': [diccLema[m]]})
    resDicc1 = resDicc1.append(resultado)
    resDicc1.to_csv(r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\diccLemas.csv",
               index=False)
    resDicc1 = pandas.read_csv(
        r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\diccLemas.csv")

for n in range(len(diccStem)):
    resultado = pandas.DataFrame({'Word': [diccStem[n]]})
    resDicc2 = resDicc2.append(resultado)
    resDicc2.to_csv(r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\diccStem.csv",
               index=False)
    resDicc2 = pandas.read_csv(
        r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\diccStem.csv")

for o in range(len(diccStop)):
    resultado = pandas.DataFrame({'Word': [diccStop[o]]})
    resDicc3 = resDicc3.append(resultado)
    resDicc3.to_csv(r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\diccStop.csv",
                    index=False)
    resDicc3 = pandas.read_csv(
        r"C:\Users\Juan Diego tu papá\Desktop\Sistemas Inteligentes\nueva clase\p3\pF\Salidas\diccStop.csv")
