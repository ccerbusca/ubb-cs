'''
Description: The function checks if the received number is prime
Input: n - an integer
Output: True or False, depending on whether the integer n is prime or not
'''

def prime(n):
    if (n % 2 == 0 or n < 2):
        return False
    if (n == 2):
        return True
    for i in range(3, n, 2):
        if i * i <= n:
            if (n % i == 0):
                return False
        else:
            break
    return True

'''
Description: The following function returns the first prime number bigger than the one received
Input: n - an integer
Output: nr - the next prime bigger than the one received as a parameter
'''

def nextPrime(n):
    nr = n + 1
    while not prime(nr):
        nr = nr + 1
    return nr

'''
Description: The determinePairs function returns a list of pairs of numbers, stored also as a list, the sum of which is equal to n
Input: n - an integer
Output: List - a list containing the pairs of numbers that if summed up, equal to n
'''

def determinePairs(n):
    if (n < 2 or n % 2 == 1):
        print("Only even numbers greater than 2 can be written as the sum of 2 prime numbers")
    p1 = 2
    List = []
    while (2 * p1 <= n):
        if (prime(n - p1) == True):
            List.append([p1, n - p1])
        p1 = nextPrime(p1)
    return List

'''
Description: The function prints all the pairs from the provided list
Input: List - a list containing the pairs of numbers that if summed up, equal to n
Output: none
'''

def printList(List):
    print("The number {} can be written as the sum of the following pairs of prime numbers:".format(n))
    for l in List:
        print(l[0], l[1])

'''
Description: Main function that calls the other ones
Input: n - integer specified by the user
Output: none
'''

def assignment_2(n):
    List = determinePairs(n)
    printList(List)

'''
Description: Test function for the assignment
'''
def testAssignment2():
    assert determinePairs(8) == [[3, 5]]
    assert determinePairs(8) == [[3, 3]]
    assert determinePairs(8) == [[3, 7], [5, 5]]
    assert determinePairs(8) == [[5, 7]]

n = input("Introduce the number: ")
assignment_2(int(n))
            
