# working with rounder

#n = float(input("Enter your number:"))
#r = round(n, 2)
#print(r)

#print()
#x = "sun"
#y = " sky"
#z = "moon"
#print(x, y, z, sep="|" , flush= True)

print()

#calling math modul
import math
r = math.sqrt(71)
print(r)

print()

import math

text1  = input("Enter  the motivational quote: ")
length =  len (text1)

text2 = text1.upper()
print(length, text2)
print()
print('Welcom to my channel!')



print()
import math

number = float(input("Enter the number: "))
print(math.sqrt(number))
if math.sqrt(number) < 100 :
    print(f"The square root is less than 100 ")
elif math.sqrt(number) > 100 :
    print(f"The square root is more than 100")
else:
    print(f"The square is equale 100")





item_num = input(f'Entter the number of items: ')
box_num = input(f'Entter the number of boxs: ')

print(f"For {item_num}, items packing {box_num}, ")


      


import math
text1 = input("Enter the motivational quote: ")
length = len(text1)
text2 = text1.upper()
print(length, text2)














import math

number = float(input("Enter the number: "))

root = math.sqrt(number)

print(f"The square root is {root:.2f}")
if  math.sqrt(number) < 100 :
    print(f"The square is less than 100.")
elif math.sqrt(number) > 100 :
    print(f"The square is more than 100.")
else:
    print(f"The square is exactily 100.")

