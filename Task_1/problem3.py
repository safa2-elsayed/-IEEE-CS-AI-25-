x=int(input("Enter Any Positive Integer : "))
sum=0
while x>0 :
    sum+= (x%10)
    x=x//10

print(f"Summantion of your Number's Digits is {sum}")