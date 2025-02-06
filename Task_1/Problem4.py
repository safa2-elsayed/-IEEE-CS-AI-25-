sentense=input("Enter Your Sentence : ")

words=sentense.split()
for word in words :
    print(word[::-1] , end=" ")