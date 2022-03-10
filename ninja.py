from pets.pet import Pet


class Ninja:
    def __init__(
            self, first_name: str, last_name: str,
            num_treats: int,num_pet_food: int, pet) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.num_treats = num_treats
        self.num_pet_food = num_pet_food
        self.pet = pet
        self.happiness = 1
    
    ''' 
    Calls the pets eat() function. If the pet doesn't eat it all for
    whatever reason, it is added back to the num_food.
    '''
    def feed_pet(self, amount_of_food: int):
        if amount_of_food <= 0:
            print('The amount of food must be more than 0!')
            return self
        if amount_of_food > self.num_pet_food:
            print("You don't have enough food to feed them that much!")
            return self
        self.num_pet_food -= amount_of_food
        self.num_pet_food += self.pet.eat(amount_of_food)
        self.__increase_happiness()
        return self

    ''' 
    Calls the pets trick function. A string is passed to determine what trick
    is performed and the number of treats decreases by 1.
    '''
    def ask_for_trick(self, trick_str: str):
        if self.num_treats <= 0:
            print(f"You don't have any treats to give {self.pet.name}!")
            return self
        self.num_treats -= 1
        self.pet.do_trick(trick_str)
        self.__increase_happiness()
        return self

    # TODO Expand this to actually do something
    def walk_pet(self):
        print(f'{self.first_name} {self.last_name}: *walking*')
        self.__increase_happiness()
        return self

    def play_with_pet(self):
        print(f'{self.first_name} {self.last_name}: *playing*')
        self.pet.play()

    # TODO Expand this to actually do something
    def bathe_pet(self):
        print(f'{self.first_name} {self.last_name}: *bathing*')
        return self

    '''
    Happiness is increased by interacting with the pet! Private method, only
    called other Ninja methods
    '''
    def __increase_happiness(self):
        self.happiness += 1
        print('Your happiness has increased!')
        print(f'New happiness: {self.happiness}')
