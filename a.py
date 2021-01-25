import time

inputt = input()
i = 0
operan = []
isOperan = True

# baca inputan
while isOperan:
    if (len(inputt) > 10):
        print("Error")
    else:
        if (inputt[len(inputt)-1] != '+'):
            operan.append(inputt)
            inputt = input()
        else :
            operan.append((inputt.split('+'))[0])
            isOperan = False
input()

hasil = input()

#print(operan)
#print(hasil)

mulai = time.time()
# Mulai kuli

huruf = []
nilai = []
bilangan = []

sama = False

def ada(array, x):
    indeks = -1
    for i in range (len(array)):
        if (array[i] == x):
            indeks = i
    return indeks

def substitusi(kata):
    temp = 0
    pangkat = 1
    for i in range (len(kata)-1,-1,-1):
        temp += pangkat * nilai[ada(huruf, kata[i])]
        pangkat *= 10
    return temp

def find(array, x):
    i = 0
    found = False
    while not found:
        if (array[i] == x):
            found = True
        else:
            i += 1
    if found:
        return i
    else:
        return -1
    

def isValid(array):
    valid = True
    for i in range (len(array)):
        for j in range (len (array)):
            if (i != j and array[i] == array [j]):
                valid = False
    if valid != False:
        for i in range (len(operan)):
            if nilai[find(huruf, operan[i][0])] == 0:
                valid = False
    return valid
        

def persamaan(array):
    jumlah = 0
    for i in range (len(array)-1):
        jumlah += array[i]
    if (jumlah == array[-1]):
        if isValid(nilai):
            return True
        else:
            return False

for i in range (len(operan)):
    for j in range (len(operan[i])):
        if ((ada(huruf, operan[i][j])) == -1):
            huruf.append(operan[i][j])
            nilai.append(9)

for i in range (len(hasil)):
    if (ada(huruf, hasil[i])== -1):
        huruf.append(hasil[i])
        nilai.append(9)

def permutasi():
    for i in range (len(operan)):
        bilangan.append(substitusi(operan[i]))

    bilangan.append(substitusi(hasil))
    
permutasi()

while not persamaan(bilangan) and nilai[0] > -1:
    nilai[-1] -= 1
    i = len(nilai)-1
    while nilai[i] == -1 and i != 0:
        nilai[i] = 9
        if (i-1) != -1:
            nilai[i-1] -= 1
        i -= 1

    bilangan = []
    permutasi()

print(huruf)
print(nilai)
print(bilangan)

if persamaan(bilangan):
    print('ok')
else:
    print("no")

selesai = time.time()

print (selesai-mulai)