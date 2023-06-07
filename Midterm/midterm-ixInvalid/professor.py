# Solomon Batenhorst
class Professor:
    def __init__(self, first_name=" ", last_name=" ", l_number="L00000000", department="N/A"):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__l_number = l_number
        self.__department = department

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def l_number(self):
        return self.__l_number

    @property
    def department(self):
        return self.__department

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

    @l_number.setter
    def l_number(self, l_number):
        if isinstance(l_number, str) and len(l_number.strip()) == 9 and l_number[0] == 'L':
            self.__l_number = l_number.strip()
        else:
            raise ValueError(f"lnumber must be a non-empty, start with L, and 9 characters string"
                             f"{type(l_number)}  {l_number}")

    @department.setter
    def department(self, department):
        if isinstance(department, str) and len(department.strip()) > 0:
            self.__department = department.strip()
        else:
            raise ValueError(f"department must a non-empty character string {type(department)}  {department}")

    def __str__(self):
        return f'Professor(First Name: {self.__first_name}, Last Name: {self.__last_name}, ' \
               f'L Number: {self.__l_number}, Department: {self.__department})'
