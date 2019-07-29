# An array of N numbers
# find the number that divides all numbers in the array

def findDivisor(arr, n):

    if n > 1:
        i = 0
        num = 0
        for i in range(0, n):
            for j in range(0, n):
                if((arr[j] % arr[i]) >= 1):
                    break

            if (j == n - 1):
                return a[i]

        return -1

# Driver code
a = [ 25, 20, 5, 10, 100 ]
n = len(a)
print(findDivisor(a, n))


a = [ 9, 3, 6, 2, 15 ]
n = len(a)
print(findDivisor(a, n))
