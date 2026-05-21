numbar = int(input("Enter a number :"))

print("-"*20)
if numbar<-100:
    print("The number is Negative large")
elif -100<=numbar<0:
    print ("The number is Negative small")    
elif numbar==0:
    print ("The number is Zero") 
elif 0<numbar<=100:
    print ("The number is Positive small")
elif 100<numbar:
    print ("The number is Positive large")            

print("-"*20)