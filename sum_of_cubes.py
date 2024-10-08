def sumOfCubes(n) :
    if n < 0:
        return
    sum = 0
    for i in range(n+1):
        sum += pow(i, 3)
    return sum

n = int(input('Enter n : '))
sum = sumOfCubes(n)
print(f'Sum : {sum}')