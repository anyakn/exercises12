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

    @staticmethod
    def normal_date(date):
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


class Meeting:
    """
    Class representing a work meeting.
    Class attributes:
    - lst_meeting: List to store all meeting objects.
    Atributes:
    - id: id of the meeting
    - date: date of the meeting
    - title: name of the meeting
    - employees: people that take part in the meeting
    Methods:
    - __init__(self, id, date, title, employees): Initializes a meeting object with the given values.
    - add_person(self, person): Adds a person to the list of employees attending the meeting.
    - count(self): Returns the number of employees attending the meeting.
    - count_meeting(cls, date): Counts the number of meetings happening on a specific date.
    - total(cls): Counts the total number of employees attending all meetings.
    - __str__(self): Returns a string representation of the meeting.
    """
    lst_meeting = []

    def __init__(self, id, date, title, employees):
        """
        Initializes a meeting object with the given values.
        Args:
        - id (int): The ID of the meeting.
        - date (str): The date of the meeting in the format "dd.mm.yyyy".
        - title (str): The title of the meeting.
        - employees (list): A list of employees attending the meeting.
        """
        self.id = id
        self.date = Date(date)
        self.title = title
        self.employees = employees
        self.lst_meeting.append(self)

    def add_person(self, person):
        """
        Adds a person to the list of employees attending the meeting.
        Args:
        - person: The person to add to the meeting.
        """
        self.employees.append(person)

    def count(self):
        """
        Returns the number of employees attending the meeting.
        """
        return len(self.employees)

    @classmethod
    def count_meeting(cls, date):
        """
        Counts the number of meetings happening on a specific date.
        Args:
        - date (str): The date to count meetings for in the format "dd.mm.yyyy".
        Returns:
        - int: The number of meetings happening on the specified date.
        """
        k = 0
        day, month, year = map(int, date._date.split('.'))
        for meeting in cls.lst_meeting:
            meeting_day, meeting_month, meeting_year = map(int, meeting.date._date.split('.'))
            if meeting_day == day and meeting_month == month and meeting_year == year:
                k += 1
        return k

    @classmethod
    def total(cls):
        """
        Counts the total number of employees attending all meetings.
        Returns:
        - int: The total number of employees attending all meetings.
        """
        k = 0
        for meeting in Meeting.lst_meeting:
            k += meeting.count()
        return k

    def __str__(self):
        """
        Returns a string representation of the meeting.
        Returns:
        - str: A string representation of the meeting object.
        """
        people = f"\n".join(f"{i}" for i in self.employees)
        return f"Рабочая встреча {self.id}\n{self.date} {self.title}\n{people}\n"


class Load:
    """
    Class for loading data about meetings from files and creating Meeting objects.
    Attributes:
    - data: List to store created Meeting objects.
    Methods:
    - write(cls, file_meetings, file_persons, file_pers_meetings): Reads data from files and creates Meeting objects.
    """
    data = []

    @classmethod
    def write(cls, file_meetings, file_persons, file_pers_meetings):
        """
        Reads data from files and creates Meeting objects.
        Args:
        - file_meetings (str): The file path for the meetings data.
        - file_persons (str): The file path for the persons data.
        - file_pers_meetings (str): The file path for the persons-meetings data.
        Returns:
        - list: A list of created Meeting objects.
        """
        with open(file_meetings, encoding='utf-8') as f_m:
            inf_m = f_m.readline().split(';')
            data_meetings = []
            for lm in f_m:
                m_inf = lm.split(';')[:-1]
                data_persons = []

                with open(file_pers_meetings, encoding='utf-8') as f_pm:
                    inf_pm = f_pm.readline().split(';')
                    for lpm in f_pm:
                        pm_inf = lpm.split(';')[:-1]
                        if pm_inf[0] == m_inf[0]:

                            with open(file_persons, encoding='utf-8') as f_p:
                                inf_p = f_p.readline().split(';')

                                for lp in f_p:
                                    p_inf = lp.split(';')[:-1]
                                    if p_inf[0] == pm_inf[1]:
                                        if p_inf[5]:
                                            prs_inf = (f"ID: {p_inf[0]} LOGIN: {p_inf[1]} NAME: {p_inf[2]} {p_inf[3]} "
                                                       f"{p_inf[4]} GENDER: {p_inf[5]}")
                                        else:
                                            prs_inf = (f"ID: {p_inf[0]} LOGIN: {p_inf[1]} NAME: {p_inf[2]} {p_inf[3]} "
                                                       f"{p_inf[4]}")
                                        data_persons.append(prs_inf)
                meeting = Meeting(*m_inf, employees=data_persons)
                data_meetings.append(meeting)
        return data_meetings


Load.write('meetings.txt', 'persons.txt', 'pers_meetings.txt')
for item in Meeting.lst_meeting:
    print(item)
print(Meeting.total())
print(Meeting.count_meeting(Date('21.04.2020')))
