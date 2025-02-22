def wordle_response(answer, guess):
    bit_string = ""
    for i in range(len(guess)):
        guess_char = guess[i]
        if guess_char == answer[i] and answer.count(guess_char) >= guess[: i + 1].count(
            guess_char
        ):
            bit_string += "2"
        elif guess_char in answer and answer.count(guess_char) >= guess[: i + 1].count(
            guess_char
        ):
            bit_string += "1"
        else:
            bit_string += "0"
    return bit_string