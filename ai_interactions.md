# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

-- Add a test case for invalid input value such as the guess is not within the selected range.

-- Add a test case for invalid input value such as the guess is a negative number.

-- Add a test case for invalid input value such as the guess is not an integer.

**What did the agent do?**

The agent added tests to check for the out of bound guesses, negatives and non-integer guesses. The agent also added a test for floats/decimals.

**What did you have to verify or fix manually?**

I followed up by testing the input limitations in the game to see how they were handled. 

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Guess above the selected range | "Add a test for a guess outside the selected range." | Call `parse_guess("101", 1, 100)` and assert it returns `False` with a range error. | Yes | This confirms guesses above the Normal difficulty maximum are rejected. |
| Negative guess | "Add a test for a negative guess." | Call `parse_guess("-5", 1, 100)` and assert it returns `False` with a range error. | Yes | Negative values are outside the game's valid positive-number range. |
| Non-integer text | "Add a test for a guess that is not an integer." | Call `parse_guess("not-an-integer", 1, 100)` and assert it returns `False` with a number error. | Yes | This confirms non-numeric input cannot reach the guess comparison logic. |
| Decimal guess | "Check whether decimal input such as 1.1 should be allowed." | Call `parse_guess("1.1", 1, 100)` and assert it returns `False` with a number error. | Yes | This caught a bug where converting through `float` silently truncated decimals to integers. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
