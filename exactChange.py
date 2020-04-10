#Anthony Almanza
#CIS 150
#Chapter 4



#created a method to store the counter for later usage
def counter(total_change):
#prevents entries below zero and above 100
  if 0 >= total_change or total_change >100:
    print(total_change, ' is an invalid entry.')

  else:   
#uses floor down division and modulo to get amount of coins
    print(total_change // 100, 'dollar(s)')
    total_change = total_change % 100

    print(total_change // 25, 'quarter(s)')
    total_change = total_change % 25

    print(total_change // 10, 'dime(s)')
    total_change = total_change % 10

    print (total_change // 5, 'nickel(s)')
    total_change = total_change % 5

    print(total_change // 1,'penny(ies)')
    total_change = total_change % 1


#while loop with a quit function and utilizing counter method to process input.
user_attempts = 'c'
while user_attempts != 'q':
    total_change= int(input('Please enter number:\n'))
    print(counter(total_change))
    user_attempts = input("type 'q' to quit or 'c' to continue\n")
    
print('Goodbye')        


