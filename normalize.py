#Anthony Almanza
#CIS150
#Chapter 5

#empty list for user data
user_data= []

#variable for total number of numbers to be stored
number= int(input('Enter the number of integers:\n'))

#iterates through to the entered number entered
#Also, it adds integer to list
for i in range(0,number):
 add= int(input('Enter your Number {}:'.format(i+1))) 
 user_data.append(add)


#Takes the user_data list and subtracts the values by 10
#Also allows rentry once for integer less than 10
for (index,value) in enumerate(user_data):
  normalized= value - 10
  if value < 10:
    print('To normalize must enter integer greater than 10')
    readd= int(input('Re-enter your number\n'))
    print('\n')
    re_normalized= readd - 10
    print('The normalized integers are:\n{}'.format(re_normalized))
    continue
  print('The normalized integers are:\n {}'.format(normalized))
