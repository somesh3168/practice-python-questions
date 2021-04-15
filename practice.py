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


