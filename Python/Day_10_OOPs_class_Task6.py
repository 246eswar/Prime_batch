#Library management system
'''Design a class Library to manage books. Implement the following methods.
add_book(title):Adds a book to the library.
remove_book(title):Removes a book if it exists.
is_available(title):Checks if a book is avalibility
list_books():Lists all books in the library'''
class Library:
    def __init__ (self):
        self.books =[]
    def add(self,title):
        
