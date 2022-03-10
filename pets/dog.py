from pets.pet import Pet


''' Dog subclass of the Pet class '''
class Dog(Pet):
    def __init__(self, name: str) -> None:
        super().__init__(name, ['sit', 'roll over', 'speak'], 100, 100, 100, 100)

    def noise(self):
        print(f'{self.name}: Woof!')
        return self

    # TODO This could be expanded. Put the health and energy check in its own
    # function
    def play(self):
        if self.energy - 10 <= 0:
            print(f'{self.name} is too tired! They need to sleep.')
            return self
        if self.health - 10 <= 0:
            print(f'{self.name} is too hungry! They need food')
            return self

        self.energy -= 10
        self.health -= 10
        print(f'{self.name}: *plays*')
        self.__print_status()
        return self
    
    # TODO Maybe do an energy and health check here too. It would be cool to
    # have the treat increase health.
    def do_trick(self, trick_str: str):
        match trick_str:
            case 'sit':
                print(f'{self.name}: Sits')
            case 'roll over':
                print(f'{self.name}: Rolls over')
            case 'speak':
                self.noise()
            case _:
                print(f"{self.name} doesn't know that that trick!")
                print('They know these tricks:')
                self.list_tricks 
        return self

    def __print_status(self):
        super().print_status()