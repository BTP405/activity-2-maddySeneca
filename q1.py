def checkPrime(num):
     if num < 2:
        return False
     for i in range(2, int(num*0.5) + 1):
        if num % i == 0:
            return False
     return True

def getPrimeNumbers(n):
    primeNumbers = [];
    for i in range(2,n):
        if checkPrime(i):
            primeNumbers.append(i);
    
    return primeNumbers;

primeList = getPrimeNumbers(20);
print(primeList)

#here i am first using the check prime function to check if a number is prime or not and then simply running the function
# again and again in the getPrimeNumbers function
# The checkPrime function simply checks if the number is divisible by 
# any number between the range 2 to n/2
