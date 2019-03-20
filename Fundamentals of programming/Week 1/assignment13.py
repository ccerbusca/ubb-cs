'''
Description: The function checks if the received number is prime
Input: n - an integer
Output: True or False, depending on whether the integer n is prime or not
'''

def prime(n):
    if (n == 2):
        return True
    if (n % 2 == 0 or n < 2):
        return False
    for i in range(3, n, 2):
        if i * i <= n:
            if (n % i == 0):
                return False
        else:
            break
    return True

'''
Description: The algorithm calculates the sequence without storing it in the
memory and returns the number located on the position specified by the provided
argument
Input: n - integer specifying the position of the number to be calculated
Output: curr - integer representing the number located on the n-th position
'''

def assignment13(n):
    nr = 1
    curr = 1
    count = 1
    while count < n:
        nr += 1
        curr = nr
        count += 1
        div = 2
        ok = False
        while count <= n and div <= nr // 2:
            if nr % div == 0 and prime(div):
                count += 1
                curr = div
                ok = True
            div = div + 1
        if ok == True:
            count -= 1
    return curr

'''
Description: Unit testing function
'''

def testAssignment13():
    assert assignment13(1) == 1
    assert assignment13(2) == 2
    assert assignment13(3) == 3
    assert assignment13(4) == 2
    assert assignment13(10) == 3

testAssignment13()
n = int(input("Introduce the poisition of the element in the sequence:"))
print("The number at the position {} is {}".format(n, assignment13(n)))
