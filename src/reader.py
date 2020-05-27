'''
membaca file eksternal vocab dan memasukkannya 
ke dalam dictionary
'''

def read(lang):
    dictionary = []
    if(lang == 'sunda'):
        source = open("../docs/sunda.txt", "r")
        word = source.readlines()
        for meaning in word :
            translation = meaning.split(' = ')
            if(translation[1][-1] == '\n') :
                translation[1] = translation[1][:-1]

            translationres = (translation[0], translation[1])
                
            dictionary.append(translationres)
    elif(lang == 'indo'):
        source = open("../docs/indonesia.txt", "r")
        word = source.readlines()
        for meaning in word :
            translation = meaning.split(' = ')
            if(translation[1][-1] == '\n') :
                translation[1] = translation[1][:-1]

            translationres = (translation[0], translation[1])
                
            dictionary.append(translationres)
        
    return dictionary

