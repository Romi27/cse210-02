from card import Card
#Class Player represents each game played. It has three attributes: "cards" which are the cards used for the game,
#"score" which is the sum of the points made for each guess and "is_playing" which determines if the game can 
#continue according to the score.
class Captain:

    def __init__(self):
        self.cards = [Card()]
        self.score = 300
        self.is_playing = True
    
    def check_life(self):#Checks if the score is enough to continue playing
        if self.score > 0:
            self.is_playing = True
        elif self.score <= 0:
            self.is_playing = False

    def get_inputs(self):#Gets the input.
        card_guess = str(input("Higher or lower? [h/l] "))
        return card_guess.lower()

#Updates the attirbutes. Creates a new Card object to be the "next card" and adds it to the cards list.
#Gets the guess and updates the score. 
    def do_updates(self):
        previous_card = self.cards[0]
        new_card = Card()
        self.cards.append(new_card)
        guess = self.get_inputs()
        self.score += new_card.get_points(guess, previous_card.card)

#Outputs the cards and the score.
    def do_outputs(self):
        self.do_updates()  
        print(f"Next card was: {self.cards[1].card}")
        print(f"Your score is: {self.score}\n")
        play_again = input('Do you want to keep playing (y/n)? ')
        if  play_again.lower() == "y":
            self.is_playing = True
            self.cards.pop(0)
        else:
            self.is_playing = False
    
    def play(self):
        while self.is_playing:
            current_card = self.cards[0]
            print(f"The card is: {current_card.card_number}\n")
            self.do_outputs()
            if self.is_playing == False:
                print("Good game!")
                break
        
def main():
    new_game = Captain()
    new_game.play()
main()
