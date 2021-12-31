# -------------- Object Oriented Programming Assessment

# Ouestion 1: Inventory Class
class Inventory:
    def __init__(self, max_capacity):
        # Write your code here.
        self.max_capacity = max_capacity
        self.name = []
        self.price = []
        self.quantity = []

    def add_item(self, name, price, quantity):
        # Don't add product if already in the inventory
        if name in self.name or quantity > self.max_capacity:
            return False

        total_quantity = (sum(self.quantity)) + quantity

        if total_quantity > self.max_capacity:
            return False

        self.name.append(name)
        self.price.append(price)
        self.quantity.append(quantity)

        return True

    def delete_item(self, name):
        # If found remove product from inventory
        for x in range(len(self.name)):
            if name == self.name[x]:
                del self.name[x]
                del self.price[x]
                del self.quantity[x]
                return True

        return False

    def get_items_in_price_range(self, min_price, max_price):
        items_in_price_range = []
        for x, element in enumerate(self.price):
            if element >= min_price and element <= max_price:
                items_in_price_range.append(self.name[x])

        return items_in_price_range

    def get_most_stocked_item(self):
        # Checks if inventory is empty
        if self.name == []:
            return None

        most_stocked_items = ""
        max_amount = max(self.quantity)

        for x in range(len(self.quantity)):
            if self.quantity[x] == max_amount:
                most_stocked_items = self.name[x]

        return most_stocked_items


# Question 2: Student Class
# Using a list
class Student:
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        self.all_students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("New grade not in the accepted range of [0-100].")

        self._grade = grade

    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1

        total_avg = 0
        for student in students:
            total_avg += student.grade
        return total_avg / len(students)

    @classmethod
    def get_average_grade(cls):
        avg = cls.calculate_average_grade(cls.all_students)
        return avg

    @classmethod
    def get_best_student(cls):
        best_student = None

        for student in cls.all_students:
            if best_student == None or best_student.grade < student.grade:
                best_student = student

        return best_student


# Sample using a dictionary
class Student:
    all_students = {}

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        self.all_students[name] = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("New grade not in the accepted range of [0-100]")

        self._grade = grade

    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1

        return sum(students.value()) / len(students)

    @classmethod
    def get_average_grade(cls):
        avg = cls.calculate_average_grade(cls.all_students)
        return avg

    @classmethod
    def get_best_student(cls):
        if len(cls.all_students) == 0:
            return None

        return max(cls.all_students, key=cls.all_students.get)


# Question 3: Geometry Inheritance
import math


class Polygon:
    def get_area(self):
        raise NotImplementedError("get_area was not implemented")

    def get_sides(self):
        raise NotImplementedError("get_area was not implemented")

    def get_perimeter(self):
        raise NotImplementedError("get_perimeter was not implemented")


class Triangle(Polygon):
    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def get_area(self):
        return get_triangle_area(self.first_side, self.second_side, self.third_side)

    def get_sides(self):
        return [self.first_side, self.second_side, self.third_side]

    def get_perimeter(self):
        return self.first_side + self.second_side + self.third_side


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return get_rectangle_area(self.width, self.height)

    def get_sides(self):
        return [self.width, self.height] * 2

    def get_perimeter(self):
        return (self.width + self.height) * 2


class Square(Rectangle):
    def __init__(self, one_side):
        super().__init__(one_side, one_side)


# Use this function in your solution.
def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter
        * (semi_perimeter - side1)
        * (semi_perimeter - side2)
        * (semi_perimeter - side3)
    )


# Use this function in your solution.
def get_rectangle_area(width, height):
    return width * height


# Question 4: Deck Class
import random


class Deck:
    def __init__(self):
        self.card_values = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
            "A",
        ]
        self.card_suits = ["H", "D", "C", "S"]
        self.full_deck = [
            f"{value}{suit}" for suit in self.card_suits for value in self.card_values
        ]

    def shuffle(self):
        random.shuffle(self.full_deck)

    def deal(self, amt):
        if amt > len(self.full_deck):
            return self.full_deck

        deal_request = self.full_deck[-amt:]
        del self.full_deck[-amt:]

        return deal_request

    def sort_by_suit(self):
        cards_by_suit = {"H": [], "D": [], "C": [], "S": []}

        for card in self.full_deck:
            suit = card[-1]
            cards_by_suit[suit].append(card)

        self.full_deck = (
            cards_by_suit["H"]
            + cards_by_suit["D"]
            + cards_by_suit["C"]
            + cards_by_suit["S"]
        )

    def contains(self, card):
        if card in self.full_deck:
            return True

        return False

    def copy(self):
        new_deck = Deck()
        new_deck.full_deck = self.full_deck[:]
        return new_deck

    def get_cards(self):
        deck_copy = self.full_deck[:]
        return deck_copy

    def __len__(self):
        return len(self.full_deck)


# Question 5: FileSystem Implementation
