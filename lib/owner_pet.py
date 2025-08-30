# lib/owner.py
class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner name must be a string")
        self.name = name

    def pets(self):
        """Return a list of all pets belonging to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign an existing Pet to this owner."""
        if not isinstance(pet, Pet):
            raise Exception("Must pass a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        """Return owner's pets sorted by pet name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


# lib/pet.py
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of: {Pet.PET_TYPES}")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet {self.name} ({self.pet_type}) owned by {self.owner.name if self.owner else 'No Owner'}>"
