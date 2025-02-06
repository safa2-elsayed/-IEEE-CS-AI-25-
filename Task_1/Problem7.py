import math 
def IsPrime (n):
   if n == 0:

    return False
   if n == 1:
    return False
   if n == 2:
    return True
   if n%2 == 0:
    return False

   for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
            
   return True

num = int(input("Enter the number : "))
print(f"Prime Factors of {num} are : ")

for i in range(2,num+1) :
    if num % i == 0 :
        if IsPrime(i) :
            print(i)
            
 