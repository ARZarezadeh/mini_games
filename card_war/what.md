# card war game
## how the game plays: 
- it has two players
- every player has half of the card dec (26 cards)
- in every turn, every player put down a card.
    - higher card win two cards
    - if cards where even, players, put aside three cards and flip next card, higher wins all the cards includeing first two, three skips and last two
    - if it was tied again. step two repaet again.
- The first player to run out of cards loses.

## components
- players (Class)
- card dec (Class)
- cards (Class)
    - number
    - suit (Hearts, Diamonds, Clubs, Spades)
- play (Function)
    - calculate winner
    - add won cards to winner hands
    - when one player's hands get empty, anounce the winner