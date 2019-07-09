#defining a new function
def average(numbers):
    media = 0.0
    suma = 0.0
    for number in numbers:
        suma += number
    
    return suma / len(numbers)

nums = [3, 5, 10, 9, 8, 0, 4, 15]
print(f'la media es {average(nums)}')



