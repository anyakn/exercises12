class AirTicket:
    """
    Represents an air ticket with passenger details and flight information.
    Args:
        passenger_name (str): Name of the passenger.
        _from (str): Departure location.
        to (str): Destination location.
        date_time (str): Date and time of the flight.
        flight (str): Flight number.
        seat (str): Seat number.
        _class (str): Class of the ticket.
        gate (str): Boarding gate.
    """

    def __init__(self, passenger_name, _from, to, date_time, flight, seat, _class, gate):
        """
        Initializes an AirTicket object with the provided details.
        Args:
            passenger_name (str): Name of the passenger.
            _from (str): Departure location.
            to (str): Destination location.
            date_time (str): Date and time of the flight.
            flight (str): Flight number.
            seat (str): Seat number.
            _class (str): Class of the ticket.
            gate (str): Boarding gate.
        """
        self.passenger_name = passenger_name
        self._from = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate

    def __str__(self):
        """
        Returns a formatted string representing the AirTicket object.
        """
        return (f"|{self.passenger_name:<16}|{self._from:<4}|{self.to:<3}|{self.date_time}|{self.flight:<20}|"
                f"{self.seat:<4}|{self._class:<3}|{self.gate:<4}|")


class Load:
    """
    A class for loading ticket information from a file and creating AirTicket objects.
    """
    data = []

    @classmethod
    def write(cls, file):
        """
        Reads ticket information from a file and creates AirTicket objects for each entry.
        Args:
            file (str): Path to the file containing ticket information.
        Returns:
            list: A list of AirTicket objects created from the file data.
        """
        with open(file) as f:
            inf = f.readline().strip().split(';')
            for line in f:
                data_ticket = line.strip().split(';')[:-1]
                ticket = AirTicket(*data_ticket)
                cls.data.append(ticket)
        return cls.data


tickets = Load.write('tickets.txt')
print('-' * 79)
print('|     NAME       |FROM|TO |   DATE/TIME    |       FLIGHT       |SEAT|CLS|GATE|')
print('=' * 79)
for item in Load.data:
    print(item)
print('-' * 79)
