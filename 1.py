class Date:
    """
        A class for working with dates in the format 'dd.mm.yyyy'.
        Attributes
        ----------
        - _date: Stores the date in the format 'dd.mm.yyyy'.
        Class attributes
        ----------
        - _months: List of abbreviated month names.
        Methods
        -------
        - __init__(date): Initializes the Date object with the given date string.
        - _normal_date(date): Validates the input date string.
        - date: property, Returns a formatted string of the date.
        - date.setter: Sets a new date for the Date object.
        - to_timestamp(): Converts the Date object to a UNIX timestamp.
        - __eq__(other): Checks if two Date objects are equal.
        - __lt__(other): Checks if the Date object is less than the other Date object.
        - __le__(other): Checks if the Date object is less than or equal to the other Date object.
        - __gt__(other): Checks if the Date object is greater than the other Date object.
        - __ge__(other): Checks if the Date object is greater than or equal to the other Date object.
        - __str__(): Returns a string representation of the Date object.
        __repr__(): Returns a string representation of the Date object.
        """
    months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

    def __init__(self, date):
        """
        Initializes an object of the Date class.
        Args:
        date (str): A string representing the date in the format 'dd.mm.yyyy'.
        """
        self._date = self.normal_date(date)

    def normal_date(self, date):
        """
        Checks and normalizes the given date.
        Returns:
        str: The normalized date or None in case of an error.
        """
        if len(date) == 10:
            if date[2] == '.' and date[5] == '.':
                if all(date[x].isdigit() for x in (0, 1, 3, 4, 6, 7, 8, 9)):
                    day, month, year = map(int, date.split('.'))
                    if 1 <= month <= 12 and year > 0:
                        if (month == 4 or month == 6 or month == 9 or month == 11) and 0 < day <= 30:
                            return date
                        elif month != 2 and 0 < day <= 31:
                            return date
                        elif month == 2:
                            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                                if 0 < day <= 29:
                                    return date
                            elif 0 < day <= 28:
                                return date
        print('Ошибка!')
        return None

    @property
    def date(self):
        """
        Returns the date in the format 'dd MMM yyyy'.
        Returns:
        str: The date in the format 'dd MMM yyyy' or None if the date is not set.
        """
        if self._date:
            day, month, year = map(int, self._date.split('.'))
            return f'{day} {self.months[month - 1]} {year} г.'
        return None

    @date.setter
    def date(self, new_value):
        """
        Sets a new value for the date.
        Args:
        new_value (str): The new date in the format 'dd.mm.yyyy'.
        """
        self._date = self.normal_date(new_value)

    def to_timestamp(self):
        """
        Converts the date to the number of seconds since the epoch (01.01.1970).
        Returns:
        int: The number of seconds since the epoch or None if the date is not set.
        """
        if self._date:
            day, month, year = map(int, self._date.split('.'))
            count_days = 0
            if year > 1970:
                count_days += day - 1
                for i in range(1970, year):
                    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
                        count_days += 366
                    else:
                        count_days += 365
                if month > 1:
                    for j in range(1, month):
                        if j == 4 or j == 6 or j == 9 or j == 11:
                            count_days += 30
                        elif j != 2:
                            count_days += 31
                        elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                            count_days += 29
                        else:
                            count_days += 28
            elif year == 1970 and month > 1:
                count_days += day - 1
                for j in range(1, month):
                    if j == 4 or j == 6 or j == 9 or j == 11:
                        count_days += 30
                    elif j != 2:
                        count_days += 31
                    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                        count_days += 29
                    else:
                        count_days += 28
            elif year == 1970 and month == 1 and day > 1:
                count_days += day - 1
            seconds = count_days * 24 * 60 * 60
            return seconds

    def __lt__(self, date_2):
        """
        Checks if the current date is less than the given date.
        Parameters:
         - date_2: Another date object to compare with.
        Returns:
        bool: True if the current date is less than the given date, else False.
        """
        return self.to_timestamp() < date_2.to_timestamp()

    def __le__(self, date_2):
        """
        Checks if the current date is less than or equals to the given date.
        Parameters:
         - date_2: Another date object to compare with.
        Returns:
        bool: True if the current date is less than or equals to the given date, else False.
        """
        return self.to_timestamp() <= date_2.to_timestamp()

    def __eq__(self, date_2):
        """
        Checks if the current date equals to the given date.
        Parameters:
         - date_2: Another date object to compare with.
        Returns:
        bool: True if the current date equals to the given date, else False.
        """
        return self.to_timestamp() == date_2.to_timestamp()

    def __ne__(self, date_2):
        """
        Checks if the current date is not equal to the given date.
        Parameters:
        - date_2: Another date object to compare with.
        Returns:
        bool: True if the current date is not equal to the given date, else False.
        """
        return self.to_timestamp() != date_2.to_timestamp()

    def __gt__(self, date_2):
        """
        Checks if the current date is greater than the given date.
        Parameters:
         - date_2: Another date object to compare with.
        Returns:
        bool: True if the current date is greater than the given date, else False.
        """
        return self.to_timestamp() > date_2.to_timestamp()

    def __ge__(self, date_2):
        """
        Checks if the current date is greater than or equals to the given date.
        Parameters:
        - date_2: Another date object to compare with.
        Returns:
        bool: True if the current date is greater than or equals to the given date, else False.
        """
        return self.to_timestamp() >= date_2.to_timestamp()

    def __str__(self):
        """
        Returns a string representation of the date.
        Returns:
        str: A string representation of the date or 'None' if the date is not set.
        """
        if self._date:
            day, month, year = map(int, self._date.split('.'))
            return f'{day} {self.months[month - 1]} {year} г.'
        return 'Nonе'

    def __repr__(self):
        """
        Returns a string representation of the object.
        Returns:
        str: A string representation of the object.
        """
        return self.__str__()


d1 = Date('07.12.2021')
print(d1.date)
d1.date = '14.02.2022'
print(d1.date)
print(d1.to_timestamp())
d2 = Date('32.14.2020')
print(d2.date)
d2.date = '29.02.2021'
print(d2)
d2.date = '29.02.2020'
print(d2.date)
if d1 < d2:
    print('YES')
else:
    print('NO')
print(d1 >= d2)
print(d1 != Date('01.01.2023'))
print(d1 <= d2)
