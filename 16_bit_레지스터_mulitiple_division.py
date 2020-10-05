def to10(list1):
    sumlist=0
    count=len(list1)-1
    if(list1[0]>0):
        list1=bosu(list1)
        for i in list1:
            sumlist+=i*(2**count)
           
            count-=1
        sumlist=-sumlist
    else:
        for i in list1:
            sumlist+=i*(2**count)
            count-=1

    return sumlist



def maketwo(n):
    firstvalue=[]
    if n<0:
        n=abs(n)   
        while(n!=0):
            firstvalue.append(n%2)
            n=n//2

        for i in range(16-len(firstvalue)):
            if len(firstvalue)<16:
                firstvalue.append(0)

        firstvalue.reverse()

        return bosu(firstvalue)

    else:
        while(n!=0):
            firstvalue.append(n%2)
            n=n//2
        
        for i in range(16-len(firstvalue)):
            if len(firstvalue)<16:
                firstvalue.append(0)

        firstvalue.reverse()
        
        return firstvalue


def bosu(listvalue):
    newlist=[]
    last=len(listvalue)-1
    count=last
    for i in listvalue:
        if(i==0):
            newlist.append(1)
        else:
            newlist.append(0)
    #print(newlist,"첫번째")
    if newlist[last]==0:
        newlist[last]=1
    else:
        
        for i in newlist[::-1]:
            #print(i)
            
            #print(i,count)
            if i==0:
                newlist[count]=1
                
                break
            else:
                
                newlist[count]=0
            count-=1    
            
                
        
    return newlist
            
            

def plus(A,M):
    carry=[0]
    sumam=[]
    for i in range(16):
        i=15-i
        carry.append((A[i]+M[i]+carry[-(i-15)])//2)
        
       
        sumam.append((A[i]+M[i]+carry[-(i-15)])%2)
    sumam.reverse()
    return sumam

def divide(n,n1):
    a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    
    Q=maketwo(n)
    M=maketwo(n1)
    flag=0
    if(Q[0]!=M[0]):
        flag=1
    Mprime=bosu(M)
    #print(Q)
    #print(M)
    print("A: ",a,"Q: ",Q )
    print("M: ",M,"count=",0)
    newa=[]
    if(Q[0]==1):
        for i in a:
            newa.append(1)#A 1로초기화
            
    if(len(newa)==16):
        a=newa#A로 다시 할당 
    count=15
    for i in range(len(a)):
        value=Q.pop(0)#shift
        a.pop(0)
        a.insert(15,value)
        print("left Shift")
        print("A: ",a,"Q: ",Q,"M: ",M )
        #a[count]=value
        if(a[0]!=M[0]):#사이클 2
            print("A=A+M")
            if(plus(a,M)[0]==a[0]):
                print("0연산 성공")
            
                Q.insert(15,1)
                a=plus(a,M)
            else:
                Q.insert(15,0)
                #에이는 건드리지않음
    
            
        else:#부호가서로같음
            print("A=A-M")
            
        
                
            if(plus(a,Mprime)[0]==a[0]):
                print("1연산성공")
                #print(a,Mprime)
                #print(plus(a,Mprime))
                a=plus(a,Mprime)
                Q.insert(15,1)
            elif(plus(a,Mprime)[0]!=a[0]):
                print("연산실패")
                #에이는 놔두면됨
                if(plus(a,Mprime)==c):
                    a=c
                    Q.insert(15,1)
                    
                else:#0이 아닐때 
                    Q.insert(15,0)  
            
        print("A: ",a,"Q: ",Q)
        print("M: ",M,"count=",i+1 )
        
            
        count-=1
    if(flag):
        Q=bosu(Q)
        
    if(a[0]==1):
        a=bosu(a)
        
    print("몫 :",to10(Q),"나머지: ",to10(a))

def multiple(n1,n):
    
    a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Q=maketwo(n1)
    M=maketwo(n)
    Mprime=bosu(M)
    print("A: ",a,"Q: ",Q)
    print("M: ",M,"count=",0 )
    Q1=0
    for i in  range(len(Q)):
        
        if(Q[15]==1 and Q1==0):
            if(plus(a,Mprime)[0]==0):#a 첫요소 검사
                print('right shift')
                print('A-M')
                a=plus(a,Mprime)
                tempvalue=a.pop(15)
                a.insert(0,0)
                tempvalue2=Q.pop(15)
                Q.insert(0,tempvalue)
                
                Q1=tempvalue2
                #print(1)
            else:
                print('right shift')
                print('A-M')
                a=plus(a,Mprime)
                tempvalue=a.pop(15)
                a.insert(0,1)
                tempvalue2=Q.pop(15)
                Q.insert(0,tempvalue)
                Q1=tempvalue2
                #print(2)
        elif(Q[15]==0 and Q1==1):
            
            if(plus(a,M)[0]==0):
                print('right shift')
                print('A+M')
                a=plus(a,M)
                tempvalue=a.pop(15)
                a.insert(0,0)
                tempvalue2=Q.pop(15)
                Q.insert(0,tempvalue)
                Q1=tempvalue2
                #print(3)
            else:
                print('right shift')
                print('A+M')
                a=plus(a,M)
                tempvalue=a.pop(15)
                a.insert(0,1)
                tempvalue2=Q.pop(15)
                Q.insert(0,tempvalue)
                Q1=tempvalue2
                #print(4)
        elif((Q[15]==0 and Q1==0) or (Q[15]==1 and Q1==1)):
            if(a[0]==0):
                print('rightshift')
                tempvalue=a.pop(15)
                a.insert(0,0)
                tempvalue2=Q.pop(15)
                Q.insert(0,tempvalue)
                Q1=tempvalue2
                #print(5)
            if(a[0]==1):
                print('rightshift')
                tempvalue=a.pop(15)
                a.insert(0,1)
                tempvalue2=Q.pop(15)
                Q.insert(0,tempvalue)
                Q1=tempvalue2
                #print(6)
        print("A: ",a,"Q: ",Q)
        print("M: ",M,"count=",i+1 )
    newlist=a+Q
    if(newlist[0]==1):
        newlist=bosu(newlist)
        print("곱셈 값",-to10(newlist))
    else:
        print("곱셈 값",to10(newlist))
    
    
                
n=int(input("십진수 값을입력해주세요"))
n1=int(input("두번째 값입력하세요 "))   
divide(n,n1)
print('===============================')
#multiple(n1,n)