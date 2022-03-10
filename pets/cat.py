from pets.pet import Pet


''' Cat subclass of the Pet class '''
class Cat(Pet):
    def __init__(self, name: str) -> None:
        super().__init__(name, ['exist'], 50, 50, 50, 50)

    def noise(self):
        print(f'{self.name}: Woof!')
        return self

    def play(self):
        if self.energy - 10 <= 0:
            print(f'{self.name} is too tired! They need to sleep.')
            return self
        if self.health - 10 <= 0:
            print(f'{self.name} is too hungry! They need food')
            return self

        self.energy -= 10
        self.health -= 10
        print(f'{self.name}: *just sorta walks around*')
        super().__print_status()
        return self

    def do_trick(self, trick_str: str):
        match trick_str:
            case 'exist':
                print(f'{self.name}: Exists. You are happier because of it')
            case _:
                print(f"{self.name} doesn't know that that trick!")
                print('They know these tricks:')
                self.list_tricks()
        return self