from pets.dog import Dog
from pets.cat import Cat
from ninja import Ninja


maverick = Dog('Maverick')
ben = Ninja('Ben', 'Rosenberg', 100, 10, maverick)
ben.play_with_pet()
ben.play_with_pet()
ben.feed_pet(10).ask_for_trick('sit').walk_pet()


# python main.py