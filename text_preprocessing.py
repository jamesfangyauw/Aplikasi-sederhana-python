from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
f=open("data kumpulan kalimat .txt", "r")
text=f.read()
#remove punctuation 
punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
text_no_punct = ""
for char in text:
    if char not in punctuations:
        text_no_punct = text_no_punct + char

#tokenization
tokenize_word = word_tokenize(text_no_punct)

#lower case converting
words=[]
for word in tokenize_word :
    words.append(word.lower())

#stop words
stops = set(stopwords.words('indonesian'))
word_tokens_no_stopwords = [w for w in words if not w in stops]

#stemming
factory = StemmerFactory()
stemmer = factory.create_stemmer()
word_stemming = []
for word in word_tokens_no_stopwords:
        word_stemming.append(stemmer.stem(word))

i=True
while i==True :
    print("======Menu=====")
    print("1. Word Tokenization")
    print("2. Lower Case Converting")
    print("3. Stop Word Removal")
    print("4. Stemming")
    print("5. Exit")
    print("  NB : If you want to change dataset, please edit the file named 'data kumpulan kalimat .txt' which is included in this folder of script file")

    no=input("Choose the number of menu = ")
    no = int(no)
    if no==1:
        print("\n=====Word Tokenize=====\n")
        print(tokenize_word, "\n \n")
        
    elif no==2:
        print("\n=====Lower Case Converting=====\n")
        print(words, "\n \n")
    elif no==3:
        print("\n=====Stop Word Removal=====\n")
        print(word_tokens_no_stopwords, "\n \n")
    elif no==4 :
        print("\n=====Stemming=====\n")
        print(word_stemming, "\n \n")
    elif no==5 :
        exit()
    else :
        print("Input the number range 1-5")