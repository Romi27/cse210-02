README.MD 

The code is called the "Hilo game". The game consists on testing your intuition capacities by guessing if the next card is higher or lower than the open card. If your choice is right you will earn 100 points, but if your choice is wrong you are going to loose 75 points. At the beginning of the game you will receive 300 points, the game will be over, if you run out of points.
In order to run the program you need to download it from the repository and run it on Python 3 or VS Code.


The project structure is:

+Hilo game folder

--+cards.py

--+player.py

-+Readme file


Authors:
Romina Canteros

Crystal Hatsumi Cardenas

Brendon Hamson

Cristian Lopez

Project structure:
 The purpose of this program is to build a solid foundation of knowledge about how abstraction is used.
Our repository contains a branch where it stores two files:  Class Card  and Class Player.
Card's file complies with the logical part of the program, it returns a value true or false, depending on the user's choice and calculates the points during the game.
The Player's file directs the game, through the different functions or rules that make the abstraction of the game. That means that each function is focused on one detail of the player's choice. For example, when the game starts and  asks the user if he wants to continue playing or not, using the "play" function if the player continues the game the function asks him what guess is low o high with " get_inputs". The function " do_updates" call the card's class and check with the user's guess, "do_outputs" returns the value of random value and the total points.


The game starts and the class player initiates by asking the methods if the user is_playing, score and card. It will check if he has the option of playing and from the class Card get the random number. Then the game asks for an input, and according to that answer it will update the information, using the do updates method, where it will verify the guess, calculate the score using the get_point method in class Card and append a new card if the player is still playing. In the do outputs the user will have the opportunity to continue playing until he runs out of points or decides to stop playing.


GIT 
 To download the very latest source off the GIT server do this:
  git clone : https://github.com/Romi27/cse210-02.git
   (you'll get a directory named cse210-02 created, filled with the source code)
