from dataclasses import dataclass

@dataclass
class BirthDate:
    day: int
    month: int
    year: int
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

@dataclass 
class Contact:
    email: str
    phone: str

    def __str__(self):
        return f"{self.email} - {self.phone}"

@dataclass 
class Address:
    street: str
    city: str
    postalCode: str

    def __str__(self):
        return f"{self.street} - {self.postalCode} - {self.city}"

@dataclass
class Personne:
    lastName: str
    firstName: str
    birthDate: BirthDate
    contact: Contact
    address: Address
    def __str__(self):
        string = f"_________________________\n| Name : {self.firstName} {self.lastName}\n| born on : {self.birthDate}\n| living at : {self.address}\n| contact : {self.contact}"
        return string

@dataclass  
class Repertoire :
    def __init__(self) :
        self.list = []

    def addPerson(self, person) :
        self.list.append(person)
    def __str__(self):
        string =""
        for person in self.list:
            string +=person.__str__()+"\n"
        return string

rep = Repertoire ()
person = Personne("Doe", "John", BirthDate(1,1,2000), Contact("a@a.com", "0606060606"), Address("1 rue de la paix", "Paris", "75000"))
rep.addPerson(person)
person = Personne("Double", "JB", BirthDate(1,1,2000), Contact("a@a.com", "0606060606"), Address("1 rue de la paix", "Paris", "75000"))
rep.addPerson(person)

print(rep)