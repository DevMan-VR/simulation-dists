# Python3 implementation of the
# above approach
 
# Function to generate random numbers
def multiplicativeCongruentialMethod(Xo, m, a,
                                     randomNums,
                                     noOfRandomNums):
 
    # Initialize the seed state
    randomNums[0] = Xo
 
    # Traverse to generate required
    # numbers of random numbers
    for i in range(1, noOfRandomNums):
         
        # Follow the linear congruential method
        randomNums[i] = (randomNums[i - 1] * a) % m
 
     

# Seed value
Xo = 221102
     
# Modulus parameter
m = pow(2,64) # 2 a la 64
     
# Multiplier term
a = 7
 
# Number of Random numbers
# to be generated
noOfRandomNums = 10
 
# To store random numbers
randomNums = [0] * (noOfRandomNums)
 
# Function Call
multiplicativeCongruentialMethod(Xo, m, a,randomNums,noOfRandomNums)
 
# Print the generated random numbers
for i in randomNums:
    print(i, end = " ")