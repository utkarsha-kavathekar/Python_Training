##Using some basic functions to work with string
str1="Hello Python "
print(str1)
print("Length of str1 is %d "%len(str1))
print("Slicing of string : %s"%str1[6:])

print(str1.join(['1','2','3']))
print(str1.count('l'))

print(str1*2)

#Some advance functions used with string

str2="hello World"
print("Slicing with stride of 2:",str2[0::2])
print("Reversing string using stride",str2[::-1])

print("capitalized string:",str2.capitalize())
print("Chaeck all char are lower case ",str2.islower())
print("Return index of found substring in str",str2.find('World'))
print("Check if space is present in string ",str2.isspace())

str3="   Hey hello new python functions hello world  "
print("Removes white spaces at start and end ",str3.lstrip())
print("checks that straing contains only digit char '234'","234".isdigit())
print("Replace substr with new str",str3.replace('hello','Hello'))
print("Split string with given delimiter bydefault with space:",str3.split())
