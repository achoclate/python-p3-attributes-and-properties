# Define the Dog class
class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name="Mutt", breed="Mutt"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in Dog.APPROVED_BREEDS or value == "Mutt":
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

# Example 
if __name__ == "__main__":
    # Creating a dog with valid name and breed
    dog1 = Dog(name="Buddy", breed="Beagle")
    print(f"Dog1 Name: {dog1.name}, Breed: {dog1.breed}")

    # Creating a dog with an invalid name
    dog2 = Dog(name="A very very long name that is invalid")
    print(f"Dog2 Name: {dog2.name}, Breed: {dog2.breed}")

    # Creating a dog with an invalid breed
    dog3 = Dog(name="Max", breed="Unknown")
    print(f"Dog3 Name: {dog3.name}, Breed: {dog3.breed}")

    # Creating a dog with default values
    dog4 = Dog()
    print(f"Dog4 Name: {dog4.name}, Breed: {dog4.breed}")
