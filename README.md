# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game purpose:** The game challenges the player to guess a randomly generated secret number within a difficulty-specific range and attempt limit. It provides hints and tracks the player's score.
- [x] **Bugs found:** The secret number and game state could reset unexpectedly, the higher/lower hints pointed in the wrong direction, guesses outside the selected range were accepted, and starting a new game kept old input and state. The tests also expected a string even though `check_guess` returns an outcome and message tuple.
- [x] **Fixes applied:** Game state is stored and reset explicitly with Streamlit session state, hints now correctly say **Go LOWER!** or **Go HIGHER!**, invalid guesses are rejected, and the New Game button clears the input and resets the round. Game logic was moved into `logic_utils.py`, and the tests were updated to check the returned outcome value.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Open the game and review the displayed difficulty, range, attempt limit, and current game status.
2. Select a difficulty level. The game displays the number range and the number of attempts available.
3. Enter a whole-number guess within the displayed range and select **Submit Guess**. Invalid or out-of-range guesses receive an error message.
4. Use the feedback to adjust the next guess. A guess above the secret number says **Go LOWER!**, while a guess below it says **Go HIGHER!**.
5. Continue guessing until you find the secret number or run out of attempts. The game displays the final score when the game ends.
6. Select **New Game** to clear the previous guess and game history, reset the score and attempts, and start a new round.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
tests/test_game_logic.py ...                           [100%]

===================== 3 passed in 0.01s ======================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
