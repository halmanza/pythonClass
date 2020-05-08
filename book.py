# Anthony Almanza
# Chapter 12



class Book:
    def __init__(self, title, author, publisher, publication_date):
        self.title = title                  #When not using inheritance all need to be initialized
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
   
    def print_info(self):
        print('Book Information:','\n')
        print('   Book Title:', self.title,'\n')
        print('   Author:', self.author,'\n')
        print('   Publisher:', self.publisher,'\n')
        print('   Publication Date:', self.publication_date,'\n')
        

class Encyclopedia(Book):
    def __init__(self,title,author,publisher,publication_date,edition,num_volumes):
        Book.__init__(self,title,author,publisher,publication_date) #Example of inheritance
        self.edition=edition                                        #Only 2 new args had to be initialized
        self.num_volumes=num_volumes
        

    def print_info(self):
        print('Encyclopedia Information','\n')
        print('   Book Title:', self.title,'\n')
        print('   Author:', self.author,'\n')
        print('   Publisher:', self.publisher,'\n')
        print('   Publication Date:', self.publication_date,'\n')
        print('   Edition', self.edition,'\n')
        print('   Number of Volumes:',self.num_volumes,'\n')
        

        

if __name__ == "__main__":
    print('Enter Book Information')
    title = input('Enter title: ')
    author = input('Enter author: ')
    publisher = input('Enter publisher: ')
    publication_date = input('Enter publication date: ')
    print('\nEnter Encyclopedia Information')
    e_title = input('Enter title: ')
    e_author = input('Enter author: ')
    e_publisher = input('Enter publisher: ')
    e_publication_date = input('Enter publication date: ')
    edition = input('Enter edition: ')
    num_volumes = int(input('Enter number of volumes: '))

book1= Book(title,author, publisher,publication_date) 
en_book=Encyclopedia(e_title, e_author, e_publisher, e_publication_date,edition,num_volumes)

book1.print_info()
en_book.print_info()
    
