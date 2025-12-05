import pymorphy3
import nltk
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
import os
nltk.download('punkt')
nltk.download('punkt_tab')
morph = pymorphy3.MorphAnalyzer()
def normalize_word_and_tags(word):
    parsed = morph.parse(word)[0] 
    lemma = parsed.normal_form
    pos = parsed.tag.POS  
    gender = parsed.tag.gender  
    number = parsed.tag.number  
    case = parsed.tag.case 
    return lemma, pos, gender, number, case
file = open('text_lab1.txt', 'r', encoding='utf-8') 
text = file.read()
file.close()
sent = sent_tokenize(text)
tokens = []
for i in sent:
    tokens.append(word_tokenize(i))
results = []
for word in tokens:
    for i in range(len(word) - 1):
        word1, word2 = word[i], word[i+1]
        lemma1, pos1, gender1, number1, case1 = normalize_word_and_tags(word1)
        lemma2, pos2, gender2, number2, case2 = normalize_word_and_tags(word2)
        if (pos1 == 'NOUN' or pos1 == 'ADJF') and (pos2 == 'NOUN' or pos2 == 'ADJF'):
            if gender1 == gender2 and number1 == number2 and case1 == case2:
                results.append((lemma1, lemma2))
file_output = open('textoutput_lab1.txt', 'w+', encoding='utf-8')
file_output.write("") 
print(f"Найдено пар: {len(results)}")
file_output.write(f"Найдено пар: {len(results)}\n")
for pair in results:
    print(f"{pair[0]} {pair[1]}")
    file_output.write(f"{pair[0]} {pair[1]}\n")   
file_output.close()
