class Player:
    # Assuming traits are ordered as [shooting, passing, dribbling, defense, speed]
    TRAIT_NAMES = ['shooting', 'passing', 'dribbling', 'defense', 'speed']
    TRAIT_WEIGHTS = {'shooting': 0.20, 'passing': 0.20, 'dribbling': 0.20, 'defense': 0.20, 'speed': 0.20}
    
    def __init__(self, name, age, height, position, weight, number, traits, salary):
        self.name = name
        self.age = age
        self.height = height
        self.position = position
        self.weight = weight
        self.number = number
        if len(traits) != len(self.TRAIT_NAMES):
            raise ValueError("Traits list must match the length of TRAIT_NAMES.")
        self.traits = traits
        self.overall = self.calculate_overall()

    def calculate_overall(self):
        overall = sum(self.traits[i] * self.TRAIT_WEIGHTS[self.TRAIT_NAMES[i]] for i in range(len(self.traits)))
        return overall
    
    def get_age(self):
        return self.age
    
    def get_height(self):
        return self.height
    
    def get_position(self):
        return self.position
    
    def get_weight(self):
        return self.weight
    
    def get_number(self):
        return self.number
    
    def get_salary(self):
        return self.salary 
    
    def set_age(self, age):
        self.age = age
    
    def set_height(self, height):
        self.height = height
    
    def set_position(self, position):
        self.position = position
    
    def set_weight(self, weight):
        self.weight = weight
    
    def set_number(self, number):
        self.number = number
    
    def set_trait(self, trait_name, value):
        if trait_name in self.TRAIT_NAMES:
            index = self.TRAIT_NAMES.index(trait_name)
            self.traits[index] = value
            self.overall = self.calculate_overall()
        else:
            print(f"Trait {trait_name} does not exist.")

    def set_salary(self, salary):
        self.salary = salary
