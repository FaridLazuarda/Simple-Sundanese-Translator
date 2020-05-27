import matcher
import reader

'''
Memilih method sesuai input
'''
def methodSelector(alg,txt,pat):
    if(alg == 'kmp'):
        return(matcher.KnuthMorris(txt,pat))
    elif(alg == 'bm'):
        return(matcher.BoyerMoore(txt,pat))
    else:
        return(matcher.regexMatch(txt,pat))

'''
Fungsi untuk memisahkan simbol dalam kalimat kedalam sebuah array
'''

def cleanMark(word) :
    i=0
    symbol = {} # membuat dictionary untuk simbol pada kalimat

    no_sym = [] # membuat array untuk tiap kata pada kalimat tanpa simbol
    if(len(word)>0):
        while i<len(word) :
            # memisahkan mark pada kalimat
            if(word[i][-1].lower() != word[i][-1].upper()) : 
                no_sym.append(word[i])
            else :
                no_sym.append(word[i][:-1])
                symbol[i] = word[i][-1]
            i+=1
        # mengembalikan 2 elemen, yaitu kata tanpa simbol dan simbol yang
        # telah dipisahkan
        return no_sym, symbol
    else:
        # jika kata masukannya kosong, return None
        return None

'''
Melakukan translate kata per kata dari input kalimat
Fungsi ini mengembalikan sebuah tuple
akan mengembalikan 1 dan string terjemahan apabila
ditemukan dalam dictionary
akan mengembalikan 0 dan string input apabila tidak 
ada dalam dictionary 
'''
def wordTranslator(word, lang, alg):
    dictionary = reader.read(lang) # meload kamus ke sebuah variabel
    if lang == 'sunda': # jika menggunakan pilihan bahasa sunda-indonesia
        for wordtuple in dictionary: #akan memproses setiap kata pada dictionary
            if len(wordtuple[0]) == len(word):
                found = methodSelector(alg,wordtuple[0], word)
                
                if found == 0 :
                    return (1, wordtuple[1])
    elif lang == 'indo' : # jika menggunakan pilihan bahasa indonesia-sunda
        for wordtuple in dictionary :
            if len(wordtuple[0]) == len(word) :
                found = methodSelector(alg,wordtuple[0], word)
                if found == 0 :
                    return (1,wordtuple[1])
    # mengembalikan sebuah tuple
    # 0 = tidak ketemu
    # 1 = ketemu
    return(0, word)

'''
Menggabungkan kata per kata dari terjemahannya, mengembalikan string hasil
'''
def assemble(word, start, finish) :
    sent = ""
    # loop untuk menggabungkan setiap elemen dari kalimat yang telah ditranslate
    for i in range(start, finish + 1) :
        if i != start :
            sent = sent + " " + word[i]
        else :
            sent = word[i]
    return sent

'''
Translate keseluruhan kalimat
'''
def translate(sentence, language, method) : 
    word = sentence.split(' ')
    if(len(word)>0):
        cleared_sent, mark = cleanMark(word)
    else:
        cleared_sent = [' ']
        mark = {' '}
    # membuat array of stopwords yang akan ditambahkan kata 'teh'
    stopwords = ['abdi', 'aing', 'anjeun', 'dewek', 'ini', 'itu', 'kaula', 'kuring', 'urang',  'hidep', 'maneh', 'sia', 'anjeunna', 'manehna']
    # inisialisasi saat belum menemukan kata 'teh'
    found_teh = False
    
    translated_word = []
    i = 0
    while i < (len(word)) : 
        for j in range(len(word) - 1, i-1, -1): # mengiterasi setiap kata dalam kalimat
            # menggabungkan kata, kemudian ditranslate setiap katanya
            voc = assemble(cleared_sent, i, j)
            translated_vocab = voc
            translation = wordTranslator(voc, language, method)
            if translation[0] == 1 :
                translated_vocab = translation[1]
                if j in mark :
                    translated_vocab = translated_vocab + mark[j]
                break
        
        if(translation[0] == 0):
            # jika tidak ketemu pada dictionary dan katanya adalah 'teh', maka diskip
            if translated_vocab == 'teh' and language == 'sunda':
                if word[i-1] in stopwords :
                    i += 1
                    continue

        translated_vocab = translated_vocab.split(' ') # membuat array untuk setiap hasil translate
        for element in range(len(translated_vocab)) :
            translated_word.append(translated_vocab[element])
        
        if language == 'indo' :
            # menambahkan kata 'teh' setelah stopwords
            if translated_word[-1] in stopwords and not found_teh :
                translated_word.append('teh')
                found_teh = True
        i=j+1
    # mengembalikan kata yang telah digabung
    return assemble(translated_word, 0, len(translated_word)-1)

print(translate('saya orang bandung', 'indo', 'bm'))