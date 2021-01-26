import time


# Input 

text = []
output = []
letter = []
first = []


def analyse():
    # Menyimpan huruf-huruf unik pada operand dan hasil
    # Kemudian mengembalikan jumlah operand dan hasil yang terlibat

    # Kamus
    # operand, result, front : bool
    # cnt : int
    operand = True
    cnt = 0
    result = False
    for x in text:
        front = True
        for i in range(len(x)):

            if x[i] == "-":
                operand = False
                break
            
            if x[i] != "\n" and x[i] != "+" and x[i] != " ":
                if x[i] not in letter:
                    letter.append(x[i])
                if front:
                    first.append(x[i])
                    front = False

            if not operand and i == (len(x)-1):
                result = True
            
        cnt += 1
        if result:
            break
    return cnt


def searchIdx(x):
    # Mengembalikan index pada array letter yang memiliki huruf x
    # KAMUS
    # i : int
    # found : bool

    i = 0 
    found = False
    while i < len(letter) and not found:
        if letter[i] == x:
            found = True
        else:
            i += 1
    return i


def cek():
    operand = True
    totalsum = 0
    for x in text:
        sum = 0
        if operand:
            i = 0
            while i < len(x) and operand:
                if x[i] == "-":
                    operand = False
                elif x[i] != "\n" and x[i] != " " and x[i] != "+":
                    sum = 10*sum + output[searchIdx(x[i])]
                i += 1
            if operand:
                totalsum += sum
        else:
            for i in range(len(x)):
                if x[i] != "\n" and x[i] != " " and x[i] != "+":
                    sum = 10*sum + output[searchIdx(x[i])]
            return sum == totalsum

def valid():
    i = 0
    valid = True
    while i < len(first) and valid:
        if(output[searchIdx(first[i])] == 0):
            valid = False
        else:
            i += 1
    return valid

    

def permutation():
    global output
    count = 0
    found = False
    for i in range(10**(len(letter)), (10**(len(letter) - 1)), - 1):
        output = [int(d) for d in str(i)]
        count += 1
        if  len(set(output)) == len(output) and cek() and valid():
            found = True
            break
    return (count, found)

def clean(cnt):
    global output, first, letter, text
    i = 0
    while i < (cnt+1) and len(text) > 0:
        text.pop(0)
        i += 1
    output = []
    first = []
    letter = []

def main():
    global text
    filename = input("Masukkan nama file: ")
    try :
        file = open(f"../test/{filename}", "r")
        text = list(file)
        while len(text) > 0:
            start = time.time()
            cnt = analyse()
            tes = permutation()
            if(tes[1]):
                for i in range(cnt):
                    inNumber = ""
                    for j in range(len(text[i])):
                        if text[i][j] != "\n" and text[i][j] != " " and text[i][j] != "-" and text[i][j] != "+":
                            inNumber = inNumber + str(output[searchIdx(text[i][j])])
                        else:
                            inNumber = inNumber + text[i][j]
                    print(text[i].rstrip('\n'), inNumber.rstrip('\n'))
            else:
                print("No solution found")
            end = time.time()
            print("Banyaknya tes :", tes[0])
            print(f"Waktu : {end-start} detik")
            clean(cnt)
        file.close()
    except:
        print("No File Found")

    print("Enter to close..")
    input()
    
if __name__ == "__main__":
    main()
