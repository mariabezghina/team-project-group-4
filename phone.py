from field import Field

class PhoneFormatError(Exception):
    def __init__(self):
        super().__init__('''Phone number must have 10 numbers and must contain just numbers!''')

class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise PhoneFormatError()
        super().__init__(value)

    def validate_phone(self, value):
        return value.isdigit() and len(value) == 10