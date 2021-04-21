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
