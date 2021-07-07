# num1  = 133

def prime(num1):
    if num1 ==1 or num1==0:
        return False
    for i in range(3,num1, 2):
        if num1%i==0 or num1%2==0:
            return False
    else:
        return True
        
# print(prime(88))

def prime_factor(x):
    prime_list = list(filter(prime,[i for i in range(x+1) if i%2!=0 or i==2]))
    return [i for i in prime_list if x%i==0]

print(prime_factor(3168))

# print(list(
#     filter(prime,[x for x in range(45) if x%2!=0 or x==2])
# ))


# for i in range(45):
#     if prime(i):
#         print(i,end=' ')
