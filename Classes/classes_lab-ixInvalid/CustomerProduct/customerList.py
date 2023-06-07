from customer import *


class CustomerList:
    """ this class represents a list of customer objects """

    # region constructor
    def __init__(self):
        self.__customer = []

    # endregion

    # region properties
    @property
    def count(self):
        return len(self.__customer)

    # endregion

    # region methods that provide functionality similar to the built-in list
    def append(self, item):
        if isinstance(item, Customer):
            self.__customer.append(item)
        else:
            raise TypeError(f'object must be a valid product object {type(item)}  {item}')

    def pop(self, index=None):
        if index is None:
            return self.__customer.pop()
        else:
            return self.__customer.pop(index)

    def find(self, item):
        if isinstance(item, Customer):
            index = 0
            for customer in self.__customer:
                if customer == item:
                    return index
                index += 1
            return -1
        elif isinstance(item, str):
            index = 0
            for customer in self.__customer:
                if customer.first_name == item:
                    return index
                index += 1
            return -1
        else:
            return -1

    def remove(self, item):
        index = self.find(item)
        if index == -1:
            raise ValueError(f'{item} is not in the product list')
        else:
            self.pop(index)

    def clear(self):
        self.__customer = []

    # endregion

    # region magic or dunder methods
    def __str__(self):
        output = f'\nCustomerList['
        for customer in self.__customer:
            if customer != self.__customer[-1]:
                output += customer.__str__() + '\n' + f'{"":>13}'
            else:
                output += customer.__str__()
        output += ']'
        return output

    def __len__(self):
        """ allows a programmer to use the len function to get the length of a product list """

        return len(self.__customer)

    def __getitem__(self, item):
        """ allows a programmer to [] to get an element in a product list """
        if isinstance(item, int):
            return self.__customer[item]
        elif isinstance(item, str):
            return self.__customer[self.find(item)]
        else:
            raise TypeError(f'index must an int or a 4 character string {type(item)}  {item}')

    def __setitem__(self, key, value):
        """ allows a programmer to [] to mutate an element in a product list """
        if isinstance(key, int) and isinstance(value, Customer):
            self.__customer[key] = value
        elif not isinstance(key, int):
            raise TypeError(f'index must an int {type(key)}  {key}')
        elif not isinstance(value, Customer):
            raise TypeError(f'item must a Product object {type(value)}  {value}')

    def __delitem__(self, key):
        """ allows a programmer to use del to delete an element from a product list """
        if isinstance(key, int):
            del self.__customer[key]
        else:
            raise TypeError(f"Index must an int {type(key)}  {key}")

    def __add__(self, other):
        """ allows concatenation of product lists.  Does not make a copy of the individual products """
        if isinstance(other, CustomerList):
            new_list = CustomerList()
            for i in self.__customer:
                new_list.append(i)
            for i in other.__customer:
                new_list.append(i)
            return new_list
        else:
            raise TypeError(f'other must a customer list {type(other)}  {other}')

    def __eq__(self, other):
        return self.__customer == other.value

    '''
        documentation suggests these are necessary to use in operator and for loop but testing indicates they are NOT necessary.
        I assume that's because we have written __eq__ in thee Product class and __getItem__ in ProductList
            def __contains__(self, item):
                if isinstance(item, Product):
                    return self.find(item) != -1
                else:
                    return False

            def __iter__(self):
                return self.__products.__iter__()

            def __next__(self):
                return self.__products.__next__()
        '''

    # endregion
