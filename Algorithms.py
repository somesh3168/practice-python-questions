## Prime number function using skipping half approach - 
def prime(num1):
    if num1 ==1 or num1==0:
        return False
    for i in range(3,num1, 2):
        # print(i)
        if num1%i==0 or num1%2==0:
            return False
    else:
        return True
        
# print(prime(88))
for i in range(0,30):
    if prime(i):
        print(i,end=' ')
        
print(prime(234511))
## Prime number function using binary approach - Flawwweddddddddddd
import time

# starting time
start = time.time()

#body 

def is_prime(x):
    for i in range(2,x,x//2):
        print(i,end='-')
        if x%i==0:
            return False
    else:
        return True
print(is_prime(2347))
# end time
end = time.time()

# total time taken
print("Runtime of the program is", end - start)


######### binary to decimal
def bin_to_dec(x:str):
    x = ''.join(reversed(x))
    tot = 0
    for i,v in enumerate(x):
        tot+=(int(v)*(2**int(i)))
    return (tot)


print(bin_to_dec('1001'))

############# Decimal to Binary algo
ls = []
def dec_to_bin(x):
    if x:
        if x >= 1:
            dec_to_bin(x//2)
        # print(x%2,end='')
        ls.append(x%2)
    return ''.join(list(map(str,ls)))


print(dec_to_bin(50))

#######################################
####### Binary Search Algo
les = [1, 3, 7, 9, 14, 19, 45]
res = 14
f = 0
l = len(les)-1
count = 1
while les[f] != res:
    f = (f+l)//2
    count+=1
    
print(count,f)

#######################################
####### Linear Search Algo
les = [1, 3, 7, 9, 14, 19, 45]
res = 46
# linear search
count = 0

if res in les:
    for i,v in enumerate(les):
        if v == res:
            count = i+1
            globals()  ['f'] = i
else:
    globals()  ['f'] = None
    print('not in list')
    
print(count,f)

#######################################
####### bubble sort Algo
les = [3,1,6,8]
# bubble sort
count = 0

for i in range(len(les)-1,0,-1):
    print(les[i],i,len(les))
    for j in range(i):
        count+=1
        if les[j]>les[j+1]:
            les[j],les[j+1] =les[j+1],les[j]
            
    
print(les,count)
