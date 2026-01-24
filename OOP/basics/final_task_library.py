from datetime import datetime
import random

class Name:

    def __set_name__(self, obj_type, name):
        self.name = name
        self.private_name = '_' + name
    
    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self
        
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        if len(value) <= 0:
            raise ValueError(f"Value '{self.private_name}' cant be empty.")
        if not isinstance(value, str):
            raise TypeError(f"Value '{self.private_name}' must be 'str', got '{type(value)}' instead.")
        setattr(obj, self.private_name, value)



class Library:

    lib_name = Name()

    def __init__(self, lib_name: str):
        self.lib_name = lib_name
        
        b1 = Book("Garry Potter", "Joanne Rowling", "sdf123", 1997)
        b2 = Book("The Silent Sea", "A. Rivers", "ts12345", 2010)
        
        self._books = {
            b1.isbn: b1,
            b2.isbn: b2
        }

        self._members = {
            "Alice Johnson": {"member_id": 23423},
            "Bob Smith": {"member_id": 1111},
            "Catherine Zeta": {"member_id": 777},
            "David Lee": {"member_id": 456},
            "Eva Green": {"member_id": 567},
        }
        
        self._borrowing_journal = {
            "dlb987" : 23423,
            "ds31415" : 567,
        }


    
    @property
    def books(self):
        temp = self._books.copy()
        return temp


    @property
    def members(self):
        temp = self._members.copy()
        return temp

    @property
    def members_qty(self):
        qty = len(self._members.keys())
        return qty

    @property
    def total_books(self):
        qty = len(self._books.keys())
        return qty


    @property 
    def available_books(self):
        counter = 0
        for v in self.books.values():
            if v['available']: counter += 1
        return counter


    @property 
    def borrowed_books(self):
        counter = 0
        for v in self.books.values():
            if not v['available']: counter += 1
        return counter


    def add_book(self, title, author, isbn, year):
        self._books[title] = {"author" : author, "isbn" : isbn, "year" : year, "available" : True}


    def add_member(self, member: Member):
        self._members[member.member_name] = {"member_id" : member.member_id}



    def find_book_by_isbn(self, isbn):
        for k, v in self._books.items():
            if isbn in v['isbn']:
                return k
        return None

    def find_member_by_id(self, member_id):
        return [k for k, v in self._members.items() if v['member_id'] == member_id]

        
    def lend_book(self, isbn, member_id):
        book_name = self.find_book_by_isbn(isbn)
        if not book_name:
            raise KeyError("Book does not exists.")
        if not self.find_member_by_id(member_id):
            raise KeyError("Member does not exists.")
        if self._books[book_name]['available']:
            self._borrowing_journal[isbn] = member_id
        else: raise KeyError("Book is already borrowed.")

    def return_book(self, isbn):
        if not isbn in self._borrowing_journal.keys():
            raise KeyError("Book is not borrowd or does not exists.")
        del self._borrowing_journal[isbn]
        book_name = self.find_book_by_isbn(isbn)
        self._books[book_name]['available'] = True
        return True

    def get_member_books(self, member_id):
        member_books = (k for k, v in self._borrowing_journal.items() if v == member_id)
        if not member_books:
            raise KeyError("This member does not have books.")
        book_list = (self.find_book_by_isbn(isbn) for isbn in member_books)
        return book_list

    def __str__(self):
        return f"Library '{self._lib_name}'.\nTotal books qty: {self.total_books}.\nAvailable books qty: {self.available_books}.\nBorrowed books qty: {self.borrowed_books}."





class Member:
    _members = {
            "Alice Johnson": {"member_id": 23423},
            "Bob Smith": {"member_id": 1111},
            "Catherine Zeta": {"member_id": 777},
            "David Lee": {"member_id": 456},
            "Eva Green": {"member_id": 567},
        }
    
    member_name = Name()


    def __init__(self, member_name, member_id, email, max_books=3):
        self.member_name = member_name
        self.is_id_set = False
        self.member_id = member_id
        self.email = email
        self.max_books = max_books


        

    def __str__(self):
        return f"Member '{self._member_name}' (ID: {self._member_id}, Email: {self._email})"


    @property
    def email(self):
        return self._email
    

    @email.setter
    def email(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email address.")
        self._email = email


    @property
    def max_books(self):
        return self._max_books
    
    @max_books.setter
    def max_books(self, max_books):
        if max_books <= 0:
            raise ValueError("Max books must be a positive integer.")
        if not isinstance(max_books, int):
            raise TypeError(f"Max books must be 'int', got '{type(max_books)}' instead.")
        self._max_books = max_books


    @property
    def borrowed_books(self):
        # logic of taking data from database
        pass
    
    @property
    def member_id(self):
        return self._member_id
    
    @member_id.setter
    def member_id(self, member_id):
        if self.is_id_set:
            raise AttributeError("Member ID is read-only and cannot be modified.")
        if not isinstance(member_id, int):
            raise TypeError(f"Member ID must be 'int', got '{type(member_id)}' instead.")
        if member_id <= 0:
            raise ValueError("Member ID must be a positive integer.")
        if member_id in [v['member_id'] for v in Member._members.values()]:
            raise ValueError("Member ID must be unique. This ID is already taken.")
        self.is_id_set = True    
        self._member_id = member_id

    @property
    def can_borrow(self):
        if len(list(self.borrowed_books)) < self.max_books:
            return True
        return False
    
    
    @property
    def books_count(self):
        return len(list(self.borrowed_books))
    

    


    def borrow_book(self, book: Book, library: Library):
        if not self.can_borrow:
            raise ValueError("Member has reached the maximum number of borrowed books.")
        if not book.available:
            raise ValueError("Book is not available for borrowing.")
        library.borrow_book(book.isbn, self._member_id)



class Book:

    title = Name()
    author = Name()

    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self._available = True


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
        if not isinstance(year, int):
            raise TypeError(f"Book year must be 'int', got '{type(year)}' instead.")
        self._year = year
    
    @property
    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.year


    @property
    def available(self):
        return self._available
    


    
    def __str__(self):
        return f"Book '{self._title}' by {self._author} (ISBN: {self._isbn}, Year: {self._year})"
    
    def __repr__(self):
        return f"Book '{self._title}' by {self._author} (ISBN: {self._isbn}, Year: {self._year})"





try:
    book1 = Book("Garry Potter", "Htos", "sdf123", 1999)
    library = Library("City Library")
except Exception as e:
    print(e)

    