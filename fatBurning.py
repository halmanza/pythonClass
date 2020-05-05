# Anthony Almanza
# Chapter 10


def get_age():
    age = int(input('Enter an age between 18 and 75: '))
    if 18 > age or age > 75:
        raise ValueError('Invalid age')
       
    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate= (220*.7) - age
    20

    return heart_rate

if __name__ == "__main__":
    try:
        age = get_age()
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age,fat_burning_heart_rate(age)))
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.')
    
        
    
