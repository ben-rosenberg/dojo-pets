'''
A superclass for pets. It's important to note that the "health" attribute
is more like nourishment. It is affected by feeding and playing. But I wanted
to match the attribute name to what was asked for in the assignment to avoid
confusion
'''
# TODO Walk function
class Pet:
    def __init__(
            self, name: str, tricks: list, 
            health: int = 100, energy: int = 100, 
            max_health: int = 100, max_energy: int = 100) -> None:
        self.name = name
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.max_health = max_health
        self.max_energy = max_energy

    # Do I specify Pet as a return value? Like: -> Pet
    ''' Sleep increases energy value '''
    def sleep(self):
        if self.energy >= self.max_energy:
            print(f"{self.name}'s Energy is already 100%! Maybe play with them!")
            self.noise()
            return self

        self.energy = self.max_energy
        self.__print_status()
        return self
    
    # TODO There's gotta be a better way to do this
    '''
    Food from the pet instance's Ninja instance is turned into health.
    Uneatened food is returned to the Ninja instance
    '''
    def eat(self, num_food: int) -> int:
        if (num_food <= 0):
            print('Amount of food must be more than 0!')
            return num_food
        if self.health >= self.max_health:
            self.noise()
            print(f"{self.name} isn't hungry!")
            return num_food

        health_increase_amount = num_food
        print(f'{self.name}: *eating...*')
        if self.health + num_food > self.max_health:
            health_increase_amount = self.max_health - self.health
            print(f"{self.name} ate all but {num_food - health_increase_amount}")
        else:
            print(f'{self.name} ate all the food!')
        self.health += health_increase_amount
        self.noise()
        print(f'+{health_increase_amount}: {self.health} ({self.health * 100 / self.max_health}%)')
        return num_food - health_increase_amount

    ''' Prints the pet's tricks '''
    def list_tricks(self):
        print(f'{self.name} knows these tricks:')
        for trick in self.tricks:
            print(trick)

    ''' Play function. Pure virtual, overrided by subclasses '''
    def play(self):
        raise NotImplementedError

    ''' Trick function. Pure virtual, overrided by subclasses '''
    def do_trick(self, trick_str):
        raise NotImplementedError

    ''' Noise function. Pure virtual, overrided by subclasses '''
    def noise(self):
        raise NotImplementedError

    def print_status(self):
        print(f"{self.name}'s Health: {self.health}")
        print(f"{self.name}'s Energy: {self.energy}")
        
        
        