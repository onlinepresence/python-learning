def number_pattern(n):
    if(not isinstance(n, int)):
        return "Argument must be an integer value."

    if(n < 1):
        return 'Argument must be an integer greater than 0.'

    numbers = []
    num = 1

    while(num <= n):
        numbers.append(str(num))
        num += 1

    return ' '.join(numbers)

print("Welcome to the number pattern generator.\nI'll provide you with any value from 1 - n where n is the maximum number you provide")
n = int(input("Provide n: "))
print(number_pattern(n))