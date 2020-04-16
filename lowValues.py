# Anthony Almanza

# CIS150

# Chapter 6
def get_user_values(user_values):
  user_input=int(input('Enter the number of integers:\n'))
  for values in range(0,user_input):
        add=int(input('Enter the integer {}:\n'.format(values + 1)))
        user_values.append(add)
        upper_threshold= set(user_values)
        
  return upper_threshold
        
def output_ints_less_than_or_equal_to_threshold(get_user_values,upper_threshold):
  upper_threshold= set(user_values)
  s= sorted(upper_threshold)

  for i in s:
    if i <= s[-1]:
      s.pop()
      print(i)
  return s
     
user_values= []
upper_threshold= set()

get_user_values(user_values) 

print('Display integer less than or equal to: {}\n'.format(user_values[-1]))


print('The integers less than or equal to {} are:\n'.format(user_values[-1]))
output_ints_less_than_or_equal_to_threshold(user_values,upper_threshold)
         

    