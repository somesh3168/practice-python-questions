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


# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.
