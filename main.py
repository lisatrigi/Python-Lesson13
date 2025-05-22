from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property 
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self,value):
        if value<0:
            raise ValueError("Weight can't be lower than 0")
        

    @property 
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        if value<0:
            raise ValueError("Height can't be lower than 0")


@abstractmethod
def calculate_bmi(self):
    pass

@abstractmethod
def get_bmi_category(self):
    pass

def print_info(self):

    print(
        f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}, Height: {self.height}"
        f"BMI:{self.calculate_bmi(), {self.get_bmi_category()}}"
        )

class Adult(Person):
    def calculate_bmi(self):
        return self.weight/(self.height ** 2) 
    
    def get_bmi_category(self):
        bmi = self.calculate_bmi()

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 24.9 < bmi < 29.9:
        return "Overweight"
    else: 
        return "Obese"
    

class Child(Person):
    def calculate_bmi(self):
        return (self.weight/(self.height ** 2) *1.3)
    
    def get_bmi_category(self):
        bmi = self.calculate_bmi()

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 24.9 < bmi < 29.9:
        return "Overweight"
    else: 
        return "Obese"