num = int(input("Enter The Number : "))
sum=0

for i in range(1, num):
    if num % i == 0:
        sum += i
    
if sum == num:
    print(f"{num} is a Perfect Number")
else :
    print(f"{num} is not a Perfect Number")