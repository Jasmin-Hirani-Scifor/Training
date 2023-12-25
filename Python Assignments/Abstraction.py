#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Abstraction in Python programming involves hiding unnecessary details and showing only the essential features of an object or concept.


# In[ ]:


#1) Basic Abstraction


# In[1]:


def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

numbers = [1, 2, 3, 4, 5]
result = calculate_average(numbers)
print(result)


# In[ ]:


#2) Class Abstraction


# In[2]:


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.area())


# In[ ]:


# Module Abstraction


# In[3]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

add(2,3)


# In[ ]:


class Author:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

class Book:
    def __init__(self, title, author, published_date):
        self.title = title
        self.author = author
        self.published_date = published_date

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f'Title: {book.title}, Author: {book.author.name}, Published Date: {book.published_date}')

# Usage of the Library abstraction

if __name__ == "__main__":
    # Create authors
    author1 = Author("John Doe", "1980-01-01")
    author2 = Author("Jane Smith", "1975-05-12")

    # Create books
    book1 = Book("Introduction to Python", author1, "2022-01-15")
    book2 = Book("Data Science Basics", author2, "2021-08-20")

    # Create a library
    library = Library()

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)

    # List all books in the library
    print("Books in the Library:")
    library.list_books()

