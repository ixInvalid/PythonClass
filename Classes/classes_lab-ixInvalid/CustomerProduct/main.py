import productTests as p
import customerTests as c
import productListTests as pl
import customerListTest as cl
import inheritanceTests as i


def product_test():
    p.testConstructor()
    print()
    # testGetters()
    print()
    p.testPropertyGetters()
    print()
    # testSetters()
    print()
    p.testPropertySetters()
    print()
    p.testPropertySettersWithValidation()
    print()
    p.testEncapsulation()


def customer_test():
    c.test_constructor()
    print()
    c.test_property_getters()
    print()
    c.test_property_setters()
    print()
    c.test_property_setters_with_validation()
    print()
    c.test_encapsulation()


def product_list_test():
    pl.testConstructor()
    print()
    pl.testAppend()
    print()
    pl.testPop()
    print()
    pl.testFind()
    print()
    pl.testRemove()
    print()
    pl.testClear()
    print()
    pl.testGetItem()
    print()
    pl.testSetItem()
    print()
    pl.testIn()
    print()
    pl.testForLoop()
    print()
    pl.testAdd()


def customer_list_test():
    cl.test_constructor()
    print()
    cl.test_append()
    print()
    cl.test_pop()
    print()
    cl.test_find()
    print()
    cl.test_remove()
    print()
    cl.test_clear()
    print()
    cl.test_get_item()
    print()
    cl.test_set_item()
    print()
    cl.test_in()
    print()
    cl.test_for_loop()
    print()
    cl.test_add()


def inheritance_test():
    i.testGearConstructor()
    print()
    i.testClothingConstructor()
    print()
    i.testEqWithInheritance()
    print()
    i.testProductListWithInheritance()
    print()


def main():
    """ this is main and it runs the program """
    # product_test()
    # customer_test()
    # product_list_test()
    # customer_list_test()
    # inheritance_test()


if __name__ == '__main__':
    main()
