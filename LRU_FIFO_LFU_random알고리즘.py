print("한칸씩 텀을두고 숫자를 입력해주세요 ex) 1 2 3 4 5 6")
inputlist=list(map(int,input().split()))
stacklimit=int(input("stack의크기는?"))
#print(stacklimit)
def LRU(inputlist):
    import time
    start = time.time()
    stacklist=[]
    count=0
    for i in range(len(inputlist)+1):
        if(i==0):
            continue
        if(len(stacklist)<stacklimit):
            if(i==1):
                stacklist.append((inputlist[:i]))
            else:
                if(inputlist[i-1] in stacklist[-1]):
                    #적중한다면 그 stacklist넣어주기
                    stacklist.append(stacklist[-1])
                    count+=1
                else:
                    #적중하지않는다면 
                    stacklist.append((inputlist[:i]))






        else:#stack limit차있으면

            if(inputlist[i-1] in stacklist[-1]):#적중
                temp=stacklist[-1].pop(0)
                stacklist[-1].insert(stacklimit-1,temp)
                count+=1
            else:
                stacklist[-1].pop(0)
                stacklist[-1].insert(stacklimit-1,inputlist[i-1])
        print(i, stacklist[-1])
        #print(count)
    print("time :", time.time() - start) 
    return (count/len(inputlist))*100
            
        
        
def FIFO(inputlist):
    import time
    start = time.time()
    stacklist=[]
    count=0
    
    for i in range(len(inputlist)+1):
        if(i==0):
            continue
        if(len(stacklist)<stacklimit):
            if(i==1):
                stacklist.append((inputlist[:i]))
            else:
                if(inputlist[i-1] in stacklist[-1]):
                    #적중한다면 그 stacklist넣어주기
                    stacklist.append(stacklist[-1])
                    count+=1
                else:
                    #적중하지않는다면 
                    stacklist.append((inputlist[:i]))






        else:#stack limit차있으면

            if(inputlist[i-1] in stacklist[-1]):#적중
                
                count+=1
            else:
                stacklist[-1].pop(0)
                stacklist[-1].insert(stacklimit-1,inputlist[i-1])
        print(i, stacklist[-1])
        #print(count)
    print("time :", time.time() - start) 
    return (count/len(inputlist))*100
            
        
        
def LFU(inputlist):
    import time
    start = time.time()
    
    stacklist=[]
    countlist=[]
    count=0
    for i in range(len(inputlist)+1):
        if(i==0):
            continue
        if(len(stacklist)<stacklimit):
            if(i==1):
                stacklist.append((inputlist[:i]))
                countlist.append(1)
            else:
                if(inputlist[i-1] in stacklist[-1]):
                    #적중한다면 그 stacklist넣어주기
                    stacklist.append(stacklist[-1])
                    tempnumberindex=stacklist[-1].index(inputlist[i-1])
                    countlist[tempnumberindex]+=1
                    
                    count+=1
                else:
                    #적중하지않는다면 
                    stacklist.append((inputlist[:i]))
                    countlist.append(1)






        else:#stack limit차있으면

            if(inputlist[i-1] in stacklist[-1]):#적중
                stacklist.append(stacklist[-1])
                tempnumberindex=stacklist[-1].index(inputlist[i-1])
                countlist[tempnumberindex]+=1
                count+=1
            else:
                lowindex=countlist.index(min(countlist))
                stacklist[-1].pop(lowindex)
                stacklist[-1].insert(lowindex,inputlist[i-1])
                countlist[lowindex]=1
        print(i, stacklist[-1],countlist)
        #print(count)
    print("time :", time.time() - start) 
    return (count/len(inputlist))*100

def random(inputlist):
    import time
    import random
    start = time.time()
    print(inputlist)
    stacklist=[]
    count=0
    flag=0
    temp2=-1
    for i in range(len(inputlist)):
        if(len(stacklist)<stacklimit):
            if(i==0):
                stacklist.append(inputlist[i])
            else:
                if(inputlist[i] in stacklist):
                    flag=1
                    count+=1
                else:
                    flag=0
                    stacklist.append(inputlist[i])

        else:#stack limit차있으면

            if(inputlist[i] in stacklist):#적중
                count+=1
                flag=1
            else:
                temp2=random.randrange(0,stacklimit)
                #print("빠진값",stacklist[temp2])
                stacklist.pop(temp2)
                flag=0
                stacklist.append(inputlist[i])
        if(flag==1):
            print(i,inputlist[i],stacklist,"적중")
        else:
            print(i,inputlist[i],stacklist)
    print("time :", time.time() - start) 
    return (count/len(inputlist))*100 






print("LRU")
temp=LRU(inputlist)
print(temp)
print("FIFO")
temp=FIFO(inputlist)   
print(temp)
print("LFU")    
temp=LFU(inputlist)
print(temp)
print("Random")
temp=random(inputlist)
print(temp)