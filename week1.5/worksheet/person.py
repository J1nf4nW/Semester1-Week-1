# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Introduces the two variables name and birth and through not isinstance we check whether they are of the correct format, if not we raise the corresponding error
        """
        if not isinstance(name, str):
            raise TypeError(f"{name}is not a string")
        if name == "":
            raise ValueError("Test Failed: name must not be empty")
        if not isinstance(birth, date):
            raise TypeError(f"{birth} is not in a valid date format")
        self.name = name
        self.birth = birth
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def is_birthday(self):
        """
        Check whether today's date is that of the user's birthday
        """
        today = date.today()
        if today.day == self.birth.day and today.month == self.birth.month:
            return True
        else:
            return False

    def initials(self):
        """
        Split the user's full name and take the first letter for every word in their name, capitalise and concatenate to make their initial
        """
        split_up = self.name.split()
        initials = ""
        for i in split_up:
            initials += i[0].upper()
        return initials
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
