# Anthony Almanza
# Chapter 11


class InfoTaker:
    user_input = str()
    first_word = str()
    second_word = str()

    def __init__(self, user_input="none", first_word="none", second_word="none"):
        self.user_input = user_input
        self.first_word = first_word
        self.second_word = second_word
        return

    def process_info(self, user_input, first_word, second_word):
        try:
            if user_input == 'input1.txt':
                try:
                    while first_word > second_word:
                       print('''\nwrong order of words,
                            \nplease re-enter your selection''')
                       break
                       
                    else:    
                        
                        x = open('input1.txt', 'r')
                        print('\nThe words between {} and {} are:\n'.format(
                            first_word, second_word))
                        for word in x:
                            if first_word < word and second_word > word:
                               print(word)
                        print(second_word, '\n')
                except (ValueError,TypeError,IOError):
                    print('incorrect file')
         
        finally:
            print('\nThank You for using line reader!\n')


def processer():
    proc1 = InfoTaker()

    user = input('Enter the path and name of the input file:\n')
    proc1.user_input = user
    first_entry = input('Enter the first word:\n')
    proc1.first_word = first_entry
    second_entry = input(
        'Enter the second word (it must come alphabetically after the first word):\n')
    proc1.second_word = second_entry
    proc1.process_info(proc1.user_input, proc1.first_word, proc1.second_word)


processer()
