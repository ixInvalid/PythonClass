class Customer:
    def __init__(self, first_name="", last_name="", email=""):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and len(first_name.strip()) > 0:
            self.__first_name = first_name.strip()
        else:
            raise ValueError(f"first name must a non-empty character string {type(first_name)}  {first_name}")

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and len(last_name.strip()) > 0:
            self.__last_name = last_name.strip()
        else:
            raise ValueError(f"last name must a non-empty character string {type(last_name)}  {last_name}")

    @email.setter
    def email(self, email):
        if isinstance(email, str) and len(email.strip()) > 0:
            self.__email = email.strip()
        else:
            raise ValueError(f"email must a non-empty character string {type(email)}  {email}")

    def __str__(self):
        return f'Customer(First Name: {self.__first_name}, Last Name: {self.__last_name}, Email: {self.__email})'

    def __eq__(self, other):
        if isinstance(other, Customer):
            return self.__first_name == other.first_name and self.last_name == other.last_name \
                and self.email == other.email
        else:
            return False
