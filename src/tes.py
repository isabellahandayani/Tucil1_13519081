import time

file = open("../test/tes.txt", "r")
input = list(file)
output = []
letter = []
first = []


def uniqueletters():
    operand = True
    cnt = 0
    result = False
    for x in input:
        front = True
        for i in range(len(x)):
            if x[i] == "-":
                operand = False
                break
            
            if x[i] != "\n" and x[i] != "+" and x[i] != " " and x[i] not in letter:
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
    for x in input:
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
    for i in range(10**(len(letter)-1), 10**(len(letter))):
        output = [int(d) for d in str(i)]
        count += 1
        if len(output) == len(letter) and len(set(output)) == len(output) and cek() and valid():
            break
    return count

def clean(cnt):
    global output, first, letter, input
    i = 0
    while i < (cnt+1) and len(input) > 0:
        input.pop(0)
        i += 1
    output = []
    first = []
    letter = []

def main():
    while len(input) > 0:
        start = time.time()
        cnt = uniqueletters()
        tes = permutation()
        end = time.time()
        print(output)
        print("Banyaknya tes :", tes)
        print(f"Waktu : {end-start}")
        clean(cnt)


if __name__ == "__main__":
    main()