#Anthony Almanza
#Chapter 7 

def name_formatter():
    entire_name= input('Enter your first name middle name(optional) last name:\n')
    collector= entire_name.split()
    # If entry of name is 3 names long (First,Middle,Almanza)
    if len(collector) == 3:
      for x in range(0,1):
        for x in range(2,len(collector)):
          last_name=collector[x].capitalize()
        for y in collector[0],collector[0]:
          initials= y[0].capitalize()
        for z in collector[1],collector[1]:
          middle= z[0].capitalize()
      print('\n{last}, {first_inital}.{middle_initial}'.format(last=last_name, first_inital=initials, middle_initial=middle))
    # If entry of name is 2 names long(first,last)
    elif len(collector) == 2:
        for name in collector[1]:
          first= name.capitalize()
        print('\n{}, {}.'.format(collector[1].capitalize(),first))      
     
    else:
      if len(collector) > 3 or len(collector) <= 1:
        print('Please try again, minimum is a first and last name.\n')
        

name_formatter()
       

    
        
         
        
            
      

  


