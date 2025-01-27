# Backgammon Game  

A simplified version of the classic **Backgammon game**, implemented in Python with a graphical interface using the `graphics` library.

---

## How to Play  
1. **Setup**:  
   - Two players take turns rolling dice and moving checkers on a board.
   - Each player moves checkers in opposite directions to their home quarter.  

2. **Player Turn**:  
   - Dice are rolled automatically.  
   - Players can select which dice value they want to use first.  
   - Click on a checker to move it based on the dice value.  
   - A checker can only move to:
     - An empty location.
     - A location where the player already has checkers.  

3. **Movement Rules**:  
   - Moves are valid only if the destination is within the board limits and adheres to the rules.  
   - **Hitting (capturing opponent checkers)** is not allowed in this version.  
   - Doubles (rolling the same value on both dice) are not part of the game.  

4. **Winning the Game**:  
   - The first player to move all their checkers to their home quarter wins.  
   - Unlike traditional Backgammon, there is **no bearing off** after moving checkers to the home quarter.

---

## Features  
- **Graphical Interface**:  
  - A visually interactive board created using the Python `graphics` library.  
  - Players click on the board to make their moves, and the game updates in real-time.  

- **Simplified Rules**:  
  - The game focuses on movement mechanics without complex features like doubling, hitting, or bearing off.  

- **Automated Dice Rolls**:  
  - Dice rolls are handled automatically, ensuring fairness and simplicity.  

---

## Controls  
1. **Rolling Dice**:  
   - Dice are rolled automatically at the start of each turn.  
   - The dice values are displayed on the screen.

2. **Moving Checkers**:  
   - Click on a checker you wish to move.  
   - The destination will depend on the dice value you selected.  
   - The board will update after each move.  

3. **Valid Moves**:  
   - A move is valid if:  
     - The checker belongs to the player.  
     - The destination is either empty or occupied by the player’s own checkers.  

---

## Known Issues  
- Resizing the game window may cause visual artifacts.  



