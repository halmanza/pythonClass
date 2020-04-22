# Anthony Almanza
# Chapter 8

courses_rooms= dict(
    CS101=3004,
    CS102=4501,
    CS103=6755,
    NT110=1244,
    CM241=1411

)
course_num_instructor= dict(
    CS101='Haynes',
    CS102='Alvarado',
    CS103='Rich',
    NT110='Burke',
    CM241='Lee'

)
course_num_times= dict(
    CS101='8:00 a.m.',
    CS102='9:00 a.m.',
    CS103='10:00 a.m.',
    NT110='11:00 a.m.',
    CM241='1:00 p.m.'
)
# User interface for input 
def user_interface():
    user_input=str(input('Please input the course number for information: \n')).upper()
    sorted_interface=sorted(courses_rooms,key=str.lower)
    compare_interface= [user_input]
    modified_input= user_input.strip()
    
    if len(user_input) < 5:
      print('Class format is (CS101), please re-enter')
    elif compare_interface[0] not in sorted_interface:
      print("Class number doesn't exist. Please re-try")
    
    return modified_input

# Process user input to search dictionaries
def dictionary_searcher(user_input):
    for x in str(user_input):
        i= user_input

    for course, room in courses_rooms.items():
        if user_input == course:
          location= room
    for course, instructor in course_num_instructor.items():
        if user_input == course:
          inst=instructor   

    for course, time in course_num_times.items():
        if user_input == course:
          course_time=time
    print()
    print('{course} location is at room:{rm}\nInstrucor:{i}\nTime: {time}'.format(course=i,rm=location,i=inst,time=course_time))
 
dictionary_searcher(user_interface())
