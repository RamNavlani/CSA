#Logic Gates
def OR(A,B):   
    return A|B	
def AND(A, B):
	return A & B
def NOT(A):
	return ~A+2
def NAND(A, B):
	return NOT(AND(A, B))
def NOR(A, B):
	return NOT(OR(A, B))
def XOR(A, B):
	return A ^ B
def XNOR(A, B):
	return NOT(XOR(A, B))
print("""Enter the chooise which gate you wanna use:
          1. OR
          2. AND
          3. NOT
          4. NAND
          5. NOR
          6. XOR
          7. XNOR""")
choise=int(input("Enter the chooise:"))
if(choise==1):
    A=int(input("Enter the value:"))
    B=int(input("Enter the value:"))    
    OR(A,B)
    if(A==0 and B==0):
	    print("Output of 0 OR 0 is", OR(0, 0))
    if(A==0 and B==1):
        print("Output of 0 OR 1 is", OR(0, 1))
    if(A==1 and B==0):
        print("Output of 1 OR 0 is", OR(1, 0))
    if(A==1 and B==1):
        print("Output of 1 OR 1 is", OR(1, 1))
if(choise==2):
    A=int(input("Enter the value:"))
    B=int(input("Enter the value:"))
    AND(A,B)
    if(A==0 and B==0):
        print("Output of 0 AND 0 is", AND(0, 0))
    if(A==0 and B==1):
        print("Output of 0 AND 1 is", AND(0, 1))
    if(A==1 and B==0):
        print("Output of 1 AND 0 is", AND(1, 0))
    if(A==1 and B==1):
        print("Output of 1 AND 1 is", AND(1, 1))
if(choise==3):
    A=int(input("Enter the value:"))
    NOT(A)
    if(A==0):
        print("Output of NOT 0 is", NOT(0))
    if(A==1):
        print("Output of NOT 1 is", NOT(1))
if(choise==4):
    A=int(input("Enter the value:"))
    B=int(input("Enter the value:"))
    NAND(A,B)
    if(A==0 and B==0):
        print("Output of 0 NAND 0 is", NAND(0, 0))
    if(A==0 and B==1):
        print("Output of 0 NAND 1 is", NAND(0, 1))
    if(A==1 and B==0):
        print("Output of 1 NAND 0 is", NAND(1, 0))
    if(A==1 and B==1):
        print("Output of 1 NAND 1 is", NAND(1, 1))
if(choise==5):
    A=int(input("Enter the value:"))
    B=int(input("Enter the value:"))
    NOR(A,B)
    if(A==0 and B==0):
        print("Output of 0 NOR 0 is", NOR(0, 0))
    if(A==0 and B==1):
        print("Output of 0 NOR 1 is", NOR(0, 1))
    if(A==1 and B==0):
        print("Output of 1 NOR 0 is", NOR(1, 0))
    if(A==1 and B==1):
        print("Output of 1 NOR 1 is", NOR(1, 1))
if(choise==6):
    A=int(input("Enter the value:"))
    B=int(input("Enter the value:"))
    XOR(A,B)
    if(A==0 and B==0):
        print("Output of 0 XOR 0 is", XOR(0, 0))
    if(A==0 and B==1):
        print("Output of 0 XOR 1 is", XOR(0, 1))
    if(A==1 and B==0):
        print("Output of 1 XOR 0 is", XOR(1, 0))
    if(A==1 and B==1):
        print("Output of 1 XOR 1 is", XOR(1, 1))
if(choise==7):
    A=int(input("Enter the value:"))
    B=int(input("Enter the value:"))
    XNOR(A,B)
    if(A==0 and B==0):
        print("Output of 0 XNOR 0 is", XNOR(0, 0))
    if(A==0 and B==1):
        print("Output of 0 XNOR 1 is", XNOR(0, 1))
    if(A==1 and B==0):
        print("Output of 1 XNOR 0 is", XNOR(1, 0))
    if(A==1 and B==1):
        print("Output of 1 XNOR 1 is", XNOR(1, 1))
if(choise!=1 and choise!=2 and choise!=3 and choise!=4 and choise!=5 and choise!=6 and choise!=7):
     print("Pls enter the valid choise") 
     
     
     
#Jk FLIP FLOPS

# Initialize the J and K inputs
J = 0
K = 0

# Initialize the flip flop output and state
output = 0
state = 0

# Define the flip flop function
def jk_flip_flop(J, K, state):
    if J == 1 and K == 1:
        # Toggle the flip flop state
        if state == 0:
            state = 1
        else:
            state = 0
    elif J == 1:
        # Set the flip flop state to 1
        state = 1
    elif K == 1:
        # Set the flip flop state to 0
        state = 0
    # Output the flip flop state
    return state

# Test the flip flop function with various inputs
output = jk_flip_flop(0, 0, output)
print("Output: ", output)  # Output: 0

output = jk_flip_flop(1, 0, output)
print("Output: ", output)  # Output: 1

output = jk_flip_flop(0, 1, output)
print("Output: ", output)  # Output: 0

output = jk_flip_flop(1, 1, output)
print("Output: ", output)  # Output: 1

output = jk_flip_flop(1, 1, output)
print("Output: ", output)  # Output: 0
