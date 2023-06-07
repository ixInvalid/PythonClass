from pprint import pprint
from customerList import *
from ANSI.prColor import *

# customer variables to be used throughout test
a_customer = Customer('A', 'Letter', '@gmail.com')
b_customer = Customer('B', 'Letter', '@gmail.com')
c_customer = Customer('C', 'Letter', '@gmail.com')
d_customer = Customer('D', 'Letter', '@gmail.com')


def test_constructor():
    c_list = CustomerList()

    print(prRed(f'{"[Testing Constructor]":-^31}'))

    print(prWhite(f'Except Empty List: {prGreen(c_list)}'))
    print(prWhite(f'Except {prBlue("Count"):<5} {"Property":>8} to be 0: {prGreen(c_list.count)}'))
    print(prWhite(f'Except {prBlue("Len"):<5} {"Property":>10} to be 0: {prGreen(c_list.count)}'))


def test_append():
    c_list = CustomerList()

    c_list.append(a_customer)
    c_list.append(b_customer)

    print(prRed(f'{"[Testing Append]":-^26}'))

    print(prWhite(f'Except {prBlue("List"):<5} with 2 Customers:0{prGreen(c_list)}'))
    print(prWhite(f'Except {prBlue("Count"):<5} {"Property":>8} to be 2: {prGreen(c_list.count)}'))
    print(prWhite(f'Except {prBlue("Len"):<5} {"Property":>10} to be 2: {prGreen(c_list.count)}'))


def create_list():
    c_list = CustomerList()

    c_list.append(a_customer)
    c_list.append(b_customer)
    c_list.append(c_customer)
    return c_list


def test_pop():
    c_list = create_list()

    print(prRed(f'{"[Testing Pop]":-^23}'))

    print(f'Before {prBlue("Pop"):<5} Expect List with 3 Customers: {prGreen(c_list)}')
    print(prWhite(f'Except {prBlue("Count"):<5} {"Property":>8} to be 3: {prGreen(c_list.count)}'))
    print(prWhite(f'Except {prBlue("Len"):<5} {"Property":>10} to be 3: {prGreen(c_list.count)}'))
    print()
    c_customer_ = c_list.pop()

    print(f'After {prBlue("Pop"):<5} with No Parameter... Expect First 2 Customers: {prGreen(c_list)}')
    print(f'Expect Popped Customer to be GoodBye: {prGreen(c_customer_)}')
    print(prWhite(f'Except {prBlue("Count"):<5} {"Property":>8} to be 2: {prGreen(c_list.count)}'))
    print(prWhite(f'Except {prBlue("Len"):<5} {"Property":>10} to be 2: {prGreen(c_list.count)}'))
    print()

    a_customer_ = c_list.pop(0)

    print(f'After {prBlue("Pop"):<5} with 0 Parameter... Expect just B: {prGreen(c_list)}')
    print(f'Expect Popped Customers to be A: {prGreen(a_customer_)}')
    print(prWhite(f'Except {prBlue("Count"):<5} {"Property":>8} to be 1: {prGreen(c_list.count)}'))
    print(prWhite(f'Except {prBlue("Len"):<5} {"Property":>10} to be 1: {prGreen(c_list.count)}'))


def test_find():
    c_list = create_list()
    print(prRed(f'{"[Testing Find]":-^24}'))
    print(f'Current List with 3 Customers: {prGreen(c_list)}')

    index = c_list.find("B")
    print(f'Called {prBlue("Find"):} with B {"as":>15} Parameter... Expect Index to be {"1":>2}:  {prGreen(index)}')

    # this will return -1 if __eq__ is not defined on the customer class
    index = c_list.find(b_customer)
    print(
        f'Called {prBlue("Find"):} with Customer Obj B {"as":>2} Parameter... Expect Index to be {"1":>2}:  {prGreen(index)}')

    index = c_list.find("D")
    print(f'Called {prBlue("Find"):} with C {"as":>15} Parameter... Expect Index to be -1: {prGreen(index)}')

    index = c_list.find(d_customer)
    print(
        f'Called {prBlue("Find"):} with Customer Obj D {"as":>2} Parameter... Expect Index to be -1: {prGreen(index)}')


def test_remove():
    c_list = create_list()

    print(prRed(f'{"[Testing Remove]":-^26}'))
    print(f'Current List with 3 Customers: {prGreen(c_list)}')

    c_list.remove(b_customer)
    print(
        f'Called {prBlue("Find")} with Customer Obj B as Parameter... Expect List to Now Have 2 Customers. {prGreen(c_list)}')

    try:
        c_list.remove(d_customer)
        print(
            f'Called {prBlue("Find")} with Customer Obj D as Parameter... An Exception Should Have Been Thrown but Was Not')
    except ValueError:
        print(f'Called {prBlue("Find")} with Customer Obj D as Parameter... An Exception Was Expected and Was Thrown')
        print(f'Expect List to Still Have 2 Customers. {prGreen(c_list)}')


def test_clear():
    c_list = create_list()

    print(prRed(f'{"[Testing Remove]":-^26}'))
    print(f'Current List with 3 Customers: {prGreen(c_list)}')

    c_list.clear()
    print(f'After the Call to {prBlue("Clear")}... Expect List to be Empty: {prGreen(c_list)}')


def test_get_item():
    c_list = create_list()

    print(prRed(f'{"[Testing List Access by Index]":-^40}'))
    print(f'Current List with 3 Customers: {prGreen(c_list)}')

    customer = c_list[1]
    print(f'Element at Index 1... Expect B. {prGreen(customer)}')

    customer = c_list["C"]
    print(f'Element with Key of C... Expect C: {prGreen(customer)}')
    try:
        error_test = c_list[2.5]
    except TypeError:
        print(f'Used [] with Float as Index... An Exception Was Expected and Was Thrown')


def test_set_item():
    c_list = create_list()

    print(prRed(f'{"[Testing Changing a List Element by Index]":-^50}'))
    print(f'Current List with 3 Customers: {prGreen(c_list)}')

    c_list[2] = d_customer
    print(f'Set Element at Index 2 to D... D Should Be at the End of the List: {prGreen(c_list)}')

    try:
        c_list["D"] = d_customer
    except TypeError:
        print(f'Used [] with String as Index... An Exception Was Expected and Was Thrown')
    try:
        c_list[1] = "What"
    except TypeError:
        print(f'Used [] with String Element Rather than a Customers... An Exception Was Expected and Was Thrown')


def test_in():
    c_list = create_list()

    print(prRed(f'{"[Testing In]":-^22}'))
    print(f'Current List with 3 Customers: {prGreen(c_list)}')

    print(f'is B in the List? Expect True:  {b_customer in c_list}')
    print(f'is D in the list? Expect False: {d_customer in c_list}')


def test_for_loop():
    c_list = create_list()

    print(prRed(f'{"[Testing For Loop]":-^22}'))
    print(f'Current List with 3 Customers: {prGreen(c_list)}')

    print(f'Iterating Through the List with {prBlue("For In")}... Expect 3 Individual Customers:')
    for i in c_list:
        print(prGreen(i))


def test_add():
    c_list = create_list()
    c_list2 = create_list()

    print(prRed(f'{"[Testing Add]":-^22}'))

    c_list_combined = c_list + c_list2
    print(f'Testing {prBlue("Adding")} 2 Customers Lists... Expect List with 6 Customers:0{prGreen(c_list_combined)}')
