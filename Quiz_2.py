#* Quiz_2.py
#*
#* ANLY 555 2023 Spring
#* Quiz 2
#*
#* Due on: 2/12/23
#* Author(s): Katie Mead
#*
#*
#* In accordance with the class policies and Georgetown's
#* Honor Code, I certify that, with the exception of the
#* class resources and those items noted below, I have neither
#* given nor received any assistance on this project other than
#* the TAs, professor, textbook and teammates.
#*

class Customer:
    # Constructor
    def __init__(self, name, age, address, payment_method):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__payment_method = payment_method
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_address(self):
        return self.__address
    def get_payment_method(self):
        return self.__payment_method
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def set_address(self, address):
        self.__address = address
    def set_payment_method(self, payment_method):
        self.__payment_method = payment_method

class VIPCustomer(Customer):
    # Constructor
    def __init__(self, name, age, address, payment_method, vipID):
        super().__init__(name, age, address, payment_method)
        self.__vipID = vipID
    # Inherited methods
    def get_name(self):
        super().get_name()
    def get_age(self):
        super().get_age()
    def get_address(self):
        super().get_address()
    def get_payment_method(self):
        super().get_payment_method()
    def set_name(self, name):
        super().set_name(name)
    def set_age(self, age):
        super().set_age(age)
    def set_address(self, address):
        super().set_address(address)
    def set_payment_method(self, payment_method):
        super().set_payment_method(payment_method)
    # New methods
    def get_vipID(self):
        return self.__vipID
    def set_vipID(self, vipID):
        self.__vipID = vipID
