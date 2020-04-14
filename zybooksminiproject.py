# Fun mini section project. Modified from zybooks slightly


size = 5

def get_numbers(num):
    numbers = []
    user_input = input('Enter {} integers:\n'.format(num))

    i = 0
    for token in user_input.split():
        number = int(token)     
        numbers.append(number)  

        print(i, number)
        i += 1

    return numbers


def print_all_numbers(numbers):
    for i in numbers:
      print(i, end=' ')
      

def print_odd_numbers(numbers):
    for i in range(0,len(numbers)):
      if numbers[i] % 2 != 0:
        print(numbers[i],end=' ')
    


def print_negative_numbers(numbers):
    for i in numbers:
      if i < 0:
        print(i, end=' ')

nums = get_numbers(size)
print('All Numbers are:')
print_all_numbers(nums)
print('\nOdd numbers are:')
print_odd_numbers(nums)
print('\n negative numbers are:')
print_negative_numbers(nums)



