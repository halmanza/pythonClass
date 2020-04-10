# Anthony Almanza
# Chapter 2
gender= str(input('Please input male or female: \n'))
age_years= int(input('Input how old year are in (years)\n'))
weight_pounds= int(input('Input your weight (lbs)\n'))
heart_rate= int(input('Input your hear rate(BPM)\n'))
time= int(input('Input duration of excercise in minutes\n'))

Men_calories = ( (age_years * 0.2017) + (weight_pounds * 0.09036) + ((heart_rate * 0.6309) - 55.0969 )) * time / 4.184 
women_calories = ( (age_years * 0.074) - (weight_pounds * 0.05741) + ((heart_rate * 0.4472) - 20.4022 )) * time / 4.184
if (gender == str('male')):
    print(Men_calories,'calories burned for men.')
else :
    print(women_calories,'calories burned for women.')
      
    

# Men_calories = ( (age_years * 0.2017) + (weight_pounds * 0.09036) + ((heart_rate * 0.6309) - 55.0969 )) * time / 4.184 
# women_calories = ( (age_years * 0.074) - (weight_pounds * 0.05741) + ((heart_rate * 0.4472) - 20.4022 )) * time / 4.184

# print(Men_calories,'calories burned for men.')
# print(women_calories,'calories burned for women.')

