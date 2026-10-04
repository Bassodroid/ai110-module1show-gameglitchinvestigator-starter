# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The first time I ran it, the game displayed a Streamlit guessing-game interface with a difficulty selector, number range, attempt counter, guess box, submit button, and developer debug information. It looked playable at first, but the behavior did not match the interface: the secret number could change after submitting a guess, and the hints pointed in the wrong direction. I also found that guesses outside the displayed range were accepted and that starting a new game did not clear the previous input or reset all of the game state.

- List at least two concrete bugs you noticed at the start  

Guesses outside the displayed range were accepted and the hints pointed in the wrong direction. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60 with secret 50 | Report that the guess is too high and tell the player to go lower. | Reported "Too High" but incorrectly said to go higher. | None; incorrect behavior appeared in the UI. |
| Guess 101 on Normal difficulty | Reject the guess because the valid range is 1 to 100. | Accepted the out-of-range guess and compared it with the secret. | None; no exception was raised. |
| Submit a guess, then submit another guess | Keep the same secret number for the entire round. | The secret number could change between submissions. | None; the state bug appeared after Streamlit reran the app. |
| Select **New Game** after entering a guess | Clear the old input and reset the score, attempts, history, and status. | The old guess and some previous game state remained. | None; the issue was visible in the UI. |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 

I used Copilot within VSCode.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 

The suggestion for fixing the high or low hints were correct. I used it both to fix and refactor the check_guess function and the test cases. 

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I found that all the suggestions were valid suggestions. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I tested the game and made sure the changes matched what I expected. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  I used the debugger to manually test that the hints made sense after fixing the guess_check function. 

- Did AI help you design or understand any tests? How?

Yes, I used AI to refractor the pytests to match the changes that were made in logic_utils. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the Python script from top to bottom whenever a user interacts with a widget, such as clicking a button or changing a selection. Without session state, regular variables are recreated during each rerun, which can make a game's secret number or score reset unexpectedly. `st.session_state` acts like a small memory for the current user session, allowing values such as the secret number, attempts, score, and game status to persist between interactions. The New Game button can then deliberately reset those stored values when a fresh round is requested.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? 

Giving consise prompts to the Copilot agent. I believe this helped achieve the results I needed. 
  
- What is one thing you would do differently next time you work with AI on a coding task?

I would ask it to break down and describe the code instead of googling things I didn't understand. 

- In one or two sentences, describe how this project changed the way you think about AI generated code. 

I think AI generated code is useful when you understand the features and backbone of the project. Having an understanding helps validate the changes that the AI agent will make. Also, it is important to use consise language to steer the AI agent into developing the results that you expect. 
