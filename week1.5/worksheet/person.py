# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        if not isinstance(name, str):
            raise TypeError(f"{name}is not a string")
        if name == " ":
            raise TypeError("name must not be empty")
        if not isinstance(birth, date):
            raise TypeError(f"{birth} is not in a valid date format")
        self.name = name
        self.birth = birth
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def is_birthday(self):
        today = date.today()
        if today.day == self.birth.day and today.month == self.birth.month:
            return True
        else:
            return False

    def initials(self):
        split_up = self.name.split()
        initials = ""
        for i in split_up:
            initials += i[0].upper()
        return initials

n = Person("Jinfan Wang", date(2008,5,12))
print(n.is_birthday())
print(n.initials())

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
