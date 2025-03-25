from collections import UserDict
from Record import Record
from datetime import date,timedelta

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
    
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError('Instance must be a Record type object.')
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if not self.data.pop(name, None):
            raise ValueError('Record not found.')
        
    def get_upcoming_birthdays(self) -> list:
        upcoming_bdays = []
        today = date.today()

        def adjust_to_weekday(date):
            if date.weekday() >= 5:
                return date + timedelta(days=(7 - date.weekday()))
            return date

        for record in self.data.values():
            if record.birthday is None:
                continue

            bday_this_year = record.birthday.value.replace(year=today.year)

            if bday_this_year < today:
                bday_this_year = bday_this_year.replace(year=today.year + 1)

            days_until_bday = (bday_this_year - today).days

            if 0 <= days_until_bday <= 7:
                congrats_date = adjust_to_weekday(bday_this_year).strftime("%d.%m.%Y")
                upcoming_bdays.append({"name": record.name.value, "birthday": congrats_date})

        return upcoming_bdays


            
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())