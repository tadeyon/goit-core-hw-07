from Name import Name
from Phone import Phone
from Birthday import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)
        return self.phones
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return self.birthday

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return self.phones
        raise ValueError('Phone number not in this record.')
    
    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones): # enumerate() to access index and object while iterating through list
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return self.phones
        raise ValueError('Old phone number not found in this record.')
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
