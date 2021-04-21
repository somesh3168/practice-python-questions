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
res = 14
# linear search
count = 0
if res in les:
    for i,v in enumerate(les):
        if v == res:
            count = i+1
            globals()  ['f'] = i
    
print(count,f)

