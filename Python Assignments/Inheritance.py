#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Single Inheritance


# In[1]:


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak() 
dog.bark()   


# In[2]:


#2 Multiple Inheritance

class Flyable:
    def fly(self):
        print("Can fly")

class Swimmable:
    def swim(self):
        print("Can swim")

class FlyingFish(Flyable, Swimmable):
    pass

fish = FlyingFish()
fish.fly()  
fish.swim()  


# In[ ]:


#3 Multilevel Inheritance


# In[3]:


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Labrador(Dog):
    def color(self):
        print("Labrador is brown")

labrador = Labrador()
labrador.speak() 
labrador.bark()   
labrador.color() 


# In[ ]:


#4 Hierarchical Inheritance


# In[4]:


class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def draw(self):
        print("Drawing circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing rectangle")

circle = Circle()
circle.draw()  

rectangle = Rectangle()
rectangle.draw()  


# In[ ]:


#5 HYbrid Inheritance


# In[5]:


class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass


# In[ ]:




