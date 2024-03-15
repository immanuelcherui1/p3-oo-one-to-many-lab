class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"{pet_type} is not a valid pet type")
        self.owner = owner
        if owner:
            owner.add_pet(self) 
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise ValueError(f"{pet} is not a valid pet")
        self.pet = pet
        self.pets_list.append(pet)
        pet.owner=self

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda x: x.name)

