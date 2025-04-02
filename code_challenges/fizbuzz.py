#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizbuzz")
        elif i % 3 == 0:
            print("fiz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)