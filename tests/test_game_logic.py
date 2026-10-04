from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_guess_outside_selected_range():
    # A Normal difficulty guess must be between 1 and 100.
    result = parse_guess("101", 1, 100)
    assert result[0] is False
    assert result[2] == "Guess must be between 1 and 100."

def test_negative_guess_is_invalid():
    # Negative guesses are outside the valid range.
    result = parse_guess("-5", 1, 100)
    assert result[0] is False
    assert result[2] == "Guess must be between 1 and 100."

def test_non_integer_guess_is_invalid():
    # Non-numeric input cannot be parsed as an integer guess.
    result = parse_guess("not-an-integer", 1, 100)
    assert result[0] is False
    assert result[2] == "That is not a number."

def test_decimal_guess_is_invalid():
    # Decimal values are not valid whole-number guesses.
    result = parse_guess("1.1", 1, 100)
    assert result[0] is False
    assert result[2] == "That is not a number."
