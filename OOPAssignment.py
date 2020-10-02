# OOP Assignment // Group 3-12
from datetime import datetime

class Customer :
    company_name = "Critter Watch"

    def __init__(self, first_name, last_name, address1, address2, city, state, sZip):
        self.cust_id = self.gen_id(first_name, last_name, address1)
        self.first_name = first_name
        self.last_name = last_name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zip = sZip
        self.balance = 0.0
        self.cust_pet = None

    def gen_id(self, fName, lName, address):
        sCustID = ""
        firstName = fName.replace(" ", "")
        lastName = lName.replace(" ", "")
        address = address.replace(" ", "")

        sCustID = firstName[0:3] + lastName[0:3] + address[0:5]

        return sCustID

    def return_bill(self):
        return('Customer ' + self.cust_id + ' with name ' + self.first_name + ' ' + self.last_name + \
                " owes " + str("${:,.2f}".format(self.balance)) + " for " + self.cust_pet.pet_name + \
                    "'s stay from " + self.cust_pet.appointment.begin_date.strftime("%m/%d/%Y") + " to " + self.cust_pet.appointment.end_date.strftime("%m/%d/%Y"))

    def make_payment(self, paymentAmount):
        self.balance = self.balance - paymentAmount


class Pet :

    def __init__(self, pet_name, breed, age, owner):
        self.pet_name = pet_name
        self.breed = breed
        self.age = age
        self.appointment = Appointment(owner)


class Appointment :

    def __init__(self, owner):
        self.begin_date = ""
        self.end_date = ""
        self.day_rate = 0.0
        self.total_days = 0
        self.total_cost = 0.0
        self.owner = owner

    def set_appointment(self, begin_date, end_date, day_rate):
        self.begin_date = begin_date
        self.end_date = end_date
        self.day_rate = day_rate

        self.calc_days()

        self.owner.balance = self.total_cost

    def calc_days(self):
        self.total_days = (self.end_date - self.begin_date).days

        if (self.total_days <= 0) :
            self.total_days = 1
        
        self.total_cost = self.total_days * self.day_rate


numCustomers = int(input("Enter the number of customers: "))

for iCount in range(numCustomers) :
    sFirstName = input("What is the customers first name: ")
    sLastName = input("What is " + sFirstName + "'s last name: ")
    sAddress1 = input("What is " + sFirstName + "'s address 1: ")
    sAddress2 = input("What is " + sFirstName + "'s address 2: ")
    sCity = input("what city does " + sFirstName + " live in: ")
    sState = input("what state does " + sFirstName + " live in: ")
    sZip = input("what is " + sFirstName + "'s zip code: ")
    oCustomer = Customer(sFirstName, sLastName, sAddress1, sAddress2, sCity, sState, sZip)

    sPetName = input("What is " + sFirstName + "'s pet named: ")
    sPetBreed = input("What is " + sPetName + "'s breed: ")
    iPetAge = int(input("How old is " + sPetName + ": "))

    oCustomer.cust_pet = Pet(sPetName, sPetBreed, iPetAge, oCustomer)

    dBeginDate = datetime.strptime(input("Enter the Start date in the format m/d/y: "), "%m/%d/%Y")
    dEndDate = datetime.strptime(input("Enter the End date in the format m/d/y: "), "%m/%d/%Y")
    fDayRate = float(input("Enter the day rate: "))

    oCustomer.cust_pet.appointment.set_appointment(dBeginDate, dEndDate, fDayRate)

    print(oCustomer.return_bill())
    fPayAmount = float(input("Enter your Payment here: "))
    oCustomer.make_payment(fPayAmount)
    print(oCustomer.return_bill())







