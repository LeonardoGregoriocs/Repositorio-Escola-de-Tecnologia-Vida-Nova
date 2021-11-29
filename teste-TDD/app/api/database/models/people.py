import datetime 

class Person:
    def __init__(self, id_Person: int, name: str, surname: str, address: str, phoneNumber: int, birthDate: datetime.date) -> None:
        self.id_Person: int = id_Person
        self.name: str = name
        self.surname: str = surname
        self.address: str = address
        self.phoneNumber: int = phoneNumber
        self.birthDate: datetime.date = birthDate

    def setName(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def getName(self) -> str:
        return self.name + " " + self.surname

    def setAddress(self, address: str) -> None:
        self.address = address
    
    def getAddress(self) -> str:
        return self.address

    def setPhoneNumber(self, phoneNumber: int) -> None:
        self.phoneNumber = phoneNumber

    def getPhoneNumber(self) -> str:
        return self.phoneNumber

    def setBirthDate(self, birthDate: datetime.date) -> None: 
        self.birthDate = birthDate
    
    def getBirthDate(self) -> datetime.date:
        return self.birthDate
    
class Customer(Person): 
    def __init__(self, id_Person: int, name: str, surname: str, address: str, phoneNumber: int, birthDate: datetime.date , ID_Customer: int, RegisterDate: datetime.date) -> None:
        super (). __init__ (id_Person, name, surname, address, phoneNumber, birthDate)
        self.ID_Customer: int = ID_Customer
        self.RegisterDate: datetime.date = RegisterDate

    def setRegisterDate(self, RegisterDate: datetime.date) -> None:
        self.RegisterDate = RegisterDate

    def getRegisterDate(self) -> datetime.date:
        return self.RegisterDate

class Seller(Person):
    def __init__(self, id_Person: int, name: str, surname: str, address: str, phoneNumber: int, birthDate: datetime.date , ID_Seller: int, AdmissionDate: datetime.date) -> None:
        super (). __init__ (id_Person, name, surname, address, phoneNumber, birthDate)
        self.ID_Seller: int = ID_Seller
        self.AdmissionDate: datetime.date = AdmissionDate

    def setAdmissionDate(self, AdmissionDate: datetime.date) -> None:
        self.AdmissionDate = AdmissionDate

    def getAdmissionDate(self) -> datetime.date:
        return self.AdmissionDate


    


    

