# Blotto algorithm 

Python algorithm to optimise solution for blotto game. Read about the idea of the game here: https://en.wikipedia.org/wiki/Blotto_game 

## Strategy:
- Create a strategy that is optimal against other relatively optimal algorithms
- Computationally simulate the blotto game where I would generate strategies that would be very good at playing other good strategies through an evolutionary method
- Start with random strategies and then pitting them against each other 
- Produced ‘offspring’ from these top strategies by performing random and slight permutations on them
- Repeating this process on the offspring of the strategy I can iteratively improve both my top strategies and the overall strategy quality of the group they are competing against
- Simlulate speciation which evolved 4 different groups of strategies 
- The 4 species then combined and pitted against each other, simulating a survival of the best environment and in the end gave an ‘alpha species’ survivor. 

## Weaknesses:
- Overlook the quantity of human - “poorly generated” (not designed necessarily to win against a large number of entries but are unpredictable)
- Overfitting of strategies where there is homogeneity in the algorithm towards higher permutations, as it only played against other winners which mainly had similar strategies. This means the top strategies are very good at playing against a very narrow definition of a ‘good strategy’.

## Improvements to be made: 
- Inputting more randomized entries throughout my permutations and used a larger database to simulate a more realistic game.
- Incorporate probabilities and compare the differentiation of strategies between different runs of finding optimal solutions, as well as the number of wins.
