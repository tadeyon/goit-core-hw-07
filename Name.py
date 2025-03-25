from Field import Field

class Name(Field):
    def __init__(self, value):
        if not value or not value.strip():
            raise ValueError("The name has to contain symbols.")
        super().__init__(value)