#creates a class for a card. Card object has a card number (self.card) and the points for each right guess
class Card:
        def __init__(self):
                self.card = random.randint(1, 13)
                self.points = 0
#Method check_guess takes two parameters "guess" and "previous_card". The last is what it will be compared to.
        def check_guess(self, guess, previous_card):
                if guess == "h":
                        if previous_card < self.card:
                                return True
                        elif previous_card > self.card:
                                return False
                elif guess == "l":
                        if previous_card < self.card:
                                return False
                        elif previous_card > self.card:
                                return True
#Method get_points gets the points made according to the success of the guess.
        def get_points(self, guess, previous_card):
                if self.check_guess(guess, previous_card) == True:
                        self.points += 100
                        return self.points
                elif self.check_guess(guess, previous_card) == False:
                        self.points -= 75     
                        return self.points
