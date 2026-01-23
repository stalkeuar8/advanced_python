from datetime import datetime

class Library:

    def __init__(self, lib_name: str, books: list, members: list):
        self.lib_name = lib_name
        self._books = []
        self._members = []


    @property
    def lib_name(self):
        return self._lib_name
    

    @lib_name.setter
    def lib_name(self, lib_name):
        if not lib_name:
            raise ValueError("Library name cant be empty.")
        self._lib_name = lib_name

    
    @property
    def books(self):
        return self._books[:]

    @property
    def members(self):
        return self._members[:]
    

    @property
    def books(self):
        return len(self._books)
    

    @property
    def books(self):
        return self._books[:]


    def __str__(self):
        return f"Library {self._lib_name}"



class Member:
    
    def __init__(self):
        pass
        

    

class Book:

    def __init__(self, title, author, isbn, year, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self._available = available
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not title:
            raise ValueError("Book title cant be empty.")
        self._title = title

    @property
    def author(self):
        return self._author 
    
    @author.setter
    def author(self, author):
        if not author:
            raise ValueError("Book author cant be empty.")
        self._author = author

    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, isbn):
        if not isbn:
            raise ValueError("Book ISBN cant be empty.")
        self._isbn = isbn

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        if year <= 0:
            raise ValueError("Book year cant be lower than 0 or equal to 0.")
        self._year = year
    
    @property
    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.year


    @property
    def available(self):
        return self._available
    
    
    def borrow_book(self, member_name: Member):
        if self._available:
            self._available = False

        else:
            return f"Book is not available."


    
    def __str__(self):
        return f"Book '{self._title}' by {self._author} (ISBN: {self._isbn}, Year: {self._year})"
    
    def __repr__(self):
        return f"Book '{self._title}' by {self._author} (ISBN: {self._isbn}, Year: {self._year})"


try:
    book1 = Book("Garry Potter", "Htos", "sdf123", 1999, True)

except Exception as e:
    print(e)

    