
def to10(list1):
    sumlist = 0
    count = len(list1) - 1
    if (list1[0] > 0):
        list1 = bosu(list1)
        for i in list1:
            sumlist += i * (2 ** count)

            count -= 1
        sumlist = -sumlist
    else:
        for i in list1:
            sumlist += i * (2 ** count)
            count -= 1

    return sumlist


def maketwo_32(n):
    firstvalue = []
    if n < 0:
        n = abs(n)
        while (n != 0):
            firstvalue.append(n % 2)
            n = n // 2

        for i in range(32 - len(firstvalue)):
            if len(firstvalue) < 32:
                firstvalue.append(0)

        firstvalue.reverse()

        return bosu(firstvalue)

    else:
        while (n != 0):
            firstvalue.append(n % 2)
            n = n // 2

        for i in range(32 - len(firstvalue)):
            if len(firstvalue) < 32:
                firstvalue.append(0)

        firstvalue.reverse()

        return firstvalue


def bosu(listvalue):
    newlist = []
    last = len(listvalue) - 1
    count = last
    for i in listvalue:
        if (i == 0):
            newlist.append(1)
        else:
            newlist.append(0)
    # print(newlist,"첫번째")
    if newlist[last] == 0:
        newlist[last] = 1
    else:

        for i in newlist[::-1]:
            # print(i)

            # print(i,count)
            if i == 0:
                newlist[count] = 1

                break
            else:

                newlist[count] = 0
            count -= 1

    return newlist

def gasangi(a, b, c) :
    d = ((not a) and b) + (a and (not b))
    s = ((not c) and d) + (c and (not d))
    c = (d and c) or (a and b)
    return [s, c]

def realgasangi(n, n1) :
    num1 = maketwo_32(n)
    num2 = maketwo_32(n1)
    sign = 0
    i = 31
    sums = []
    c = sign
    last_c = 0
    while i >= 0 :
        a = num1[i]
        b = ((not num2[i]) and sign) + (num2[i] and (not sign))
        resultOperation = gasangi(a,b,c)
        s = resultOperation[0]
        c = resultOperation[1]
        if i == 1:
            last_c = c
        if i == 0 :
            sumOfSum = 0
            for sum in sums:
                sumOfSum = sumOfSum + sum
            z = int(not sumOfSum)
            v = ((not c) and last_c) + (c and (not last_c))
            print(32 - i, "번 계산결과 - C:", c, ", S:", s, ", V:", v,", Z:", z)
        else :
            print(32-i,"번 계산결과 - C:",c,", S:",s,", V: ? Z: ?")

        sums.append(s)
        temp_sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        k = 31
        for v in sums:
            temp_sums[k] = v
            k = k - 1
        print("현재까지의 32비트 레지스터 형태 - ", temp_sums)
        print("------------------------------------------------------------------------")
        i = i - 1
    sums.reverse()
    print("최종 덧셈값 :",to10(sums))

def realgamsangi(n, n1) :
    num1 = maketwo_32(n)
    num2 = maketwo_32(n1)
    sign = 1
    i = 31
    sums = []
    c = sign
    last_c = 0
    while i >= 0 :
        a = num1[i]
        b = ((not num2[i]) and sign) + (num2[i] and (not sign))
        resultOperation = gasangi(a,b,c)
        s = resultOperation[0]
        c = resultOperation[1]
        if i == 1:
            last_c = c
        if i == 0 :
            sumOfSum = 0
            for sum in sums:
                sumOfSum = sumOfSum + sum
            z = int(not sumOfSum)
            v = ((not c) and last_c) + (c and (not last_c))
            print(32 - i, "번 계산결과 - C:", c, ", S:", s, ", V:", v,", Z:", z)
        else :
            print(32-i,"번 계산결과 - C:",c,", S:",s,", V: ? Z: ?")

        sums.append(s)
        temp_sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        k = 31
        for v in sums:
            temp_sums[k] = v
            k = k - 1
        print("현재까지의 32비트 레지스터 형태 - ", temp_sums)
        print("------------------------------------------------------------------------")
        i = i - 1
    sums.reverse()
    print("최종 뺄셈값 :",to10(sums))

n=int(input("십진수 값을입력해주세요 "))
n1=int(input("두번째 값입력하세요 "))
realgasangi(n, n1)
print('===============================')
realgamsangi(n, n1)

