def factorial(n):
    output=1
    for i in range(1,n+1):
        output=output*i
    return output

def permutation(n,r):
    final=(factorial(n))/(factorial(n-r))
    return final

def combination(n,r):
    result=(factorial(n))/((factorial(n-r))*(factorial(r)))
    return result

n=int(input())
r=int(input())

if n<0:
    print("Factorial of this number is undefined")
else:
    print("The Factorial of this number is" ,factorial(n))

if r<0 or n<r or n<0:
    print("Permutation and Combination both does not exist")
else:
    print("The Permutation of n and r is",permutation(n,r))
    print("The combination of n and r is",combination(n,r))

# my first comment 
