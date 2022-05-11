from gamehilo.card import card


class player:
    def __init__(self):
        self.card = []
        self.is_playing = True
        self.score = 300

    def results(self):
        print("Your score is" + self.score)



    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):

        card_guess = str(input("HIGUER OR LOWER? [H/L] "))
        self.is_playing= (card_guess=="y")


    def do_updates(self):

        while self.is_playing == True:
            if self.cardcard==True:
                self.score+=  100
            else:
                self.score-= 75
        self.is_playing==False


    def do_outputs(self):
        if not self.is_playing:
            return
       
        print(f"Your score is: {self.score}\n")
        if self.score > 0:
            self.is_playing== True
        else:
            print("game over ")
