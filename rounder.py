#print('Hello World!')
#number = input('What is your number?')
#print(f'{number}')
#n = float(input('Enter your number:'))
#r = round(n, 2)
#print(r)

#print the statement on separing it by the slash

x = 'sun'
y = 'moon'
z = 'sky'
print(x, y, z, sep= '|', flush= 'true')

# import the math modul

#import  math
#r = math.sqrt(71)
#print(r)

text1 = input("what is your squate?")
length = len(text1)
text2 = text1.upper()
print(length, text2)

#
import math

number = float(input("Enter the number:"))
print(math.sqrt(number))

if math.sqrt(number) < 100 :
    print(f" The square root is less than 100.")

elif   math.sqrt(number)  > 100 :
    print(f"the square is grether than 100." )

else:
    print(f"the square root is 100.")

# the other way

import math
number = float(input("Enter the nmuber: "))

root = math.sqrt(number)
print(f"The square root is:{root:.2f}")
if root < 100 :
    print(f"the square root is less than 100.")

elif root > 100  :
    print(f"the square is grether than 100.")

else:
    print(f"the square is excatly 100.")

    https://vscode.dev/github/ELENGA-ASSEKA/progamming_with_fuction/blob/mainython.3.11_3.11.2544.0_x64__qbz5n2kfra8p0/Lib/_strptime.py