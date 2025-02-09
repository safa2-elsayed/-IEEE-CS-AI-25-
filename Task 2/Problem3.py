lst = []  

n = int(input()) 

for _ in range(n):
    command = input().split()  
    
    if command[0] == "insert":
        i = int(command[1])
        e = int(command[2])
        lst.insert(i, e) 
        
    elif command[0] == "print":
        print(lst)  
        
    elif command[0] == "remove":
        e = int(command[1])
        for i in range(len(lst)): 
            if lst[i] == e:
                del lst[i] 
                break 
        
    elif command[0] == "append":
        e = int(command[1])
        lst.append(e)  

    elif command[0] == "sort":
        lst.sort()  
        
    elif command[0] == "pop":
        if lst:  
            lst.pop()  
        
    elif command[0] == "reverse":
        lst.reverse()  
