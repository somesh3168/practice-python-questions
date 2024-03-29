# 4. Write a Python program to get the factorial of a non-negative integer. Go to the editor
# Click me to see the sample solution
# basic
def facto(num):
    f = 1
    for i in range(1,num+1,1):
        f*=i
    return f
    
print(facto(5))
# factorial re - cursion

def facto(num):
    if num <= 1:
        return 1
    else:
        return num* (facto(num-1))
    
print(facto(5))



# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'
sample = 'restart'

first = sample[0]

sample = sample.replace(first,'$')

print(first+sample[1:])

# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 
# Go to the editor
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

abc, xyz =  'abc', 'xyz'

abc ,xyz = abc.replace(abc[-1],xyz[-1]), xyz.replace(xyz[-1],abc[-1])

print(xyz+' '+abc)


# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
samples = ['star','kid','amazing', 'to']

for i,sample in enumerate(samples):
    if sample[-3:] == 'ing':
        samples[i] = sample+'ly'
    elif len(sample) >2:
        samples[i] = sample + 'ing'
    else:
        samples[i] = sample

print(samples)

# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. 
# Return the resulting string. Go to the editor
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

samples = 'The lyrics is not that poor!'
snot = samples.find('not')
spoor = samples.find('poor')
  

if spoor > snot and snot>0 and spoor>0:
    samples = samples.replace(samples[snot:(spoor+4)], 'good')
    print(samples)
else:
    print(samples)

# 8. Write a Python function that takes a list of words and returns the length of the longest one.

samples = ["PHP", "Exercises", "Backend"]
ret = {}
for i,v in enumerate (samples):
    ret[i] = len(v)
m = max(list(ret.values()))
for k,v in ret.items():
    if v == m:
        print('\nLongest word:',samples[k])
        print('Length of the longest word: ',v)

# >>>>>>>>>>> method 2

samples = ["PHP", "Exercises", "Backend"]
m = (max(list(map(len,samples))))
for i,v in enumerate (samples):
    if len(v) == m:
        print('\nLongest word:',v)
        print('Length of the longest word: ',m)
        
# 9. Write a Python program to remove the nth index character from a nonempty string.

sample,n = 'python' , 2
print(''.join(sample.split(sample[n])))

# 10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
sample = 'python' 
print(''.join([sample[-1],sample[1:-1],sample[0]]))
# op = nythop

# 16. Write a Python function to insert a string in the middle of a string. Go to the editor
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def insert_sting_middle(text1, mid):
    text1 = text1.split(' ')
    text1.insert(1,mid)
    print(' '.join(text1))


insert_sting_middle('ranga billa','bc')

# recursion
# 1. Write a Python program to sum all the items in a list. Go to the editor
# Click me to see the sample solution

les = [1,2,3,4]

def sum_li(les=[]):
    if len(les) == 1:
        return les[0]
    else:
        return les[0] + sum_li(les[1:])
        
    
print(sum_li(les))

# 2. Write a Python program to multiplies all the items in a list. Go to the editor
# Click me to see the sample solution


les = [111,2,33,4,5]
maxi = les[0]
for v in les:
    if v > maxi:
        maxi = v
print(maxi)

# 2. Write a Python program to converting an Integer to a string in any base. Go to the editor
# Click me to see the sample solution
# DEcimal to any base

def to_string(n,base):
    
    all_base = '0123456789ABCDEF'
    
    if n < base:
        return all_base[n]
    else:
        return to_string(n//base, base) + all_base[n%base]
        
print(to_string(189,10))



