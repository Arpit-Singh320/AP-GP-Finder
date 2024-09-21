a=int(input("First term of a series:"))
b=int(input("Second term of a series:"))
c=int(input("Third term of a series::"))


D1 = (b - a)
D2 = (c - b)
R = (c/b)


#FOR AN AP
if((D1 == D2) and D1!= 0 ):

    print("This is an AP")
    print("Do you want to:")
    print("1. Find the nth term of the AP")
    print("2. Sum of first N terms of AP")
    print("3. Find the position of a specific term in the AP")
    option = (input("what you want to find:"))

# TO FIND Nth TERM OF AN AP
    if(option == "Find the nth term of the AP"):
         
        n = int(input("no. of term:"))
        print("your Nth term is:", a + (n - 1)*D1)

# TO FIND SUM OF Nth TERM OF AN AP
    elif (option == "Sum of first N terms of AP"):

        m = int(input("no. of term:"))
        print("Your sum of Nth term is:", m/2* (2*a + (m-1)*D2))

# TO FIND POSITION OF Nth TERM OF AN AP
    elif (option == "Find the position of a specific term in the AP"):

        t = int(input("Write the Nth term:"))
        print("the position of Nth term is:", + t + (t-a/D1)+1)


#FOR GP
elif (b/a == c/b and R>1):
    # A1 = int(a) 
    # B1 = int(b)
    # C1 = int(c)
    print("This is an GP")
    print("Find the nth term of the GP")
    print("Sum of first N terms of GP")
    option = input("what you want find:")

# TO FIND Nth TERM OF GP
    if (option == "Find the nth term of the GP"):
        n = int(input("no. of term:"))
        print("Your Nth term is:", + a*R**(n-1))

# TO FINE SUM OF Nth TERM OF GP
    elif (option == "Sum of first N terms of GP"):
        n = int(input("no. of term:"))
        Q=R**n -1
        O= R-1
        print("Your sum of Nth term is:", + (a*Q)/O )

#FOR INFINITE GP
elif(b/a == c/b and R<1):
    print("this is an infinite GP")
    O = 1-R
    print("The sum of Infinite GP is:", + a/O)

#FOR CONSTANT GP
elif (b/a == c/b and R == 1):
    print(" This is a Constant Series")

else:
    print("The series is neither AP, GP.")

#FOR HP
# if(D3 == D4):
#     A1 = float(a) 
#     B1 = float(b)
#     C1 = float(c)
#     print("This is an HP")
#     option = (input("what you want to find:"))

# # TO FIND Nth TERM OF AN HP
#     if(option == "Nth terms" or "n terms" or "nth term" or " N term"):
#         n = int(input("no. of term:"))
#         print("your Nth term is:", + 1/(A +(n-1)*D3) )

# # TO FIND SUM OF Nth TERM OF AN HP
#     elif (option == "sum of N terms" or "sum of n terms" or "sum of Nth term" or "sum of n term"):
#         n = int(input("no. of term:"))
#         Sn = (n/2)*(2*a + (n-1)*D1)
#         print("Your sum of Nth term is:", + Sn )

# # TO FIND POSITION OF Nth TERM OF AN Hp
#     elif (option == "position of Nth term" or "position of n term"):
#         t = int(input("Write the Nth term:"))
#         A2 = 1/A1
#         T2 = 1/t
#         print("the position of Nth term is:", + ((T2-A2)/D3 + 1) )