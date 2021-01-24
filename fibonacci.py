import numpy as np

memo = np.zeros([-1] * 5)
print(memo)
def fibo(n):
    if(n == 0):
        return 0
    elif(n ==1):
        return 1
    
    return fibo(n - 1) + fibo(n - 2)

if __name__ == "__main__":
    print("input integer")
    s = input()
    result = fibo(int(s))
    print(result)