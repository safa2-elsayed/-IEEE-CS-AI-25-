def probability_Dis ( values ) :
    freq = {}
    for val in values :
        freq[val]=freq.get(val, 0) + 1 

    print("{" ,end=" ")
    for key , val in freq.items() :
        prob = val / len(values)
        print(f"{key} : {prob} ", end=" , ")

    print("}")    

def Conditional_Probability(A,B) :
    A_Freq=sum(A)
    A_B_Freq=sum(1 for i in range(len(A)) if A[i] == 1 and B[i] == 1)
    
    if A_Freq == 0 :
      return 0
    
    return f"{A_B_Freq}/{A_Freq}"

def bayes_Theorem(A,B,C) :
    if B==0 :
      return 0
    return (C*A)/B

if __name__ == "__main__":
    values =list(map(int, input("Enter your Data To get The Probability Distribution of Them : ").split()))
    probability_Dis(values)
    print()

    Event_A= list(map(int, input("Enter The Values of The 1st Event : ").split()))
    Event_B= list(map(int, input("Enter The Values of The 2st Event : ").split()))
    print(f"P(2st event | 1st event) = {Conditional_Probability(Event_A,Event_B)}")
    print()
    
    Prior_a=float(input("Enter The Probability of 1st Event : "))
    Prior_b=float(input("Enter The Probability of 2st Event : "))
    conditional_b_given_a=float(input("Enter the conditional probability of 2nd Event Given 1st Event : "))

    print(f"P( 1st Event | 2st Event ) = {bayes_Theorem(Prior_a,Prior_b,conditional_b_given_a )}")