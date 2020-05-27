import re

'''
Pencocokkan string dengan menggunakan library regular expression
Mencari string pattern pada text Jika pattern terdapat pada text, 
fungsi mengembalikan indeks pertama letak kemunculan pattern
Jika tidak ada pattern dalam text, fungsi mengembalikan -1
'''
def regexMatch(text, pattern):
    pattern = pattern.upper()
    text = text.upper()

    if(re.search(pattern, text)): # Ketemu
        return ((re.search(pattern, text)).span()[0])
    else: # tidak ketemu
        return -1
        
'''
Fungsi untuk menghitung nilai fungsi batas (border function)
untuk setiap karakter pada string pattern saat dicocokkan pada teks
dan mengembalikan tabel border
'''
def borderFunc(pattern):
    fail = [0] * len(pattern)
    
    m = len(pattern)
    j = 0
    k = 1
    
    while (k < m):
        if (pattern[j] == pattern[k]): # match
            fail[k] = j + 1
            k += 1
            j += 1
        elif (j > 0):
            j = fail[j-1]
        else: # tidak match sama sekali
            fail[k] = 0
            k += 1
    
    return fail

'''
Fungsi utama dalam pencocokan string menggunakan metode KMP
Mencari pattern dalam text
Jika ditemukan, fungsi mengembalikan indeks pertama letak kemunculan
pattern dalam teks, jika tidak ditemukan, fungsi mengembalikan -1
'''
def KnuthMorris(txt, pat):
    text = txt.lower()
    pattern = pat.lower()

    n = len(text)
    m = len(pattern)

    fail = borderFunc(pattern) # membuat border array
    
    i = 0
    j = 0

    while (i < n):
        if (pattern[j] == text[i]): # character match
            if (j == m-1): # posisi j sudah di akhir pattern
                return i-m + 1
            i+=1
            j+=1
        elif (j > 0):
            j = fail[j-1] # mulai mencocokan dari nilai fail[j-1]
        else:
            i+=1

    return -1; #tidak match

'''
Fungsi untuk mencari nilai last occurence bagi setiap
karakter pada string pattern. Fungsi mengembalikan tabel
last
'''
def lastOccurrance(pattern):
    last = [-1] * 128
    for i in range (len(pattern)):
        last[ord(pattern[i])] = i
    
    return last

'''
Fungsi utama algoritma Booyer Moore dengan mencari pattern
dalam text. Jika ditemukan, fungsi mengembalikan
indeks oertama kemunculan pattern, jika tidak ditemukan, fungsi
mengembalikan -1
'''
def BoyerMoore(text, pattern) :
    pattern = pattern.upper()
    text = text.upper()

    last = lastOccurrance(pattern)
    n = len(text)
    m = len(pattern)
    i = m-1
    
    if (i > n-1):#pattern lebih panjang dari text
        return -1
    
    j = m-1
    while True:
        if (pattern[j] == text[i]): #jika match
            if (j == 0): #pattern sudah sampai awal
                return i
            else: #pattern belum habis, cocokkan secara mundur (looking glass)
                i-=1
                j-=1
        else: # tidak match, lakukan character jump
            lastOcc = last[ord(text[i])]
            i = i + m - min(j, 1 + lastOcc)
            j = m -1
        
        if(i > n-1):
            break #lakukan selama text belum habis
    
    return -1 #text dan pattern tidak match