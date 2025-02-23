# def wordle_response(answer, guess):
#     bit_string = ""
#     for i in range(len(guess)):
#         guess_char = guess[i]
#         if guess_char == answer[i] and answer.count(guess_char) >= guess[: i + 1].count(
#             guess_char
#         ):
#             bit_string += "2"
#         elif guess_char in answer and answer.count(guess_char) >= guess[: i + 1].count(
#             guess_char
#         ):
#             bit_string += "1"
#         else:
#             bit_string += "0"
#     return bit_string

from collections import Counter
def wordle_response(answer, guess):
    bit_string = ["0"] * len(guess)
    answer_char_count = Counter(answer)
    guess_char_count = Counter()

    # First pass: mark correct positions (green)
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            bit_string[i] = "2"
            guess_char_count[guess[i]] += 1

    # Second pass: mark present but incorrect positions (yellow) and incorrect positions (grey)
    for i in range(len(guess)):
        if bit_string[i] == "2":
            continue
        if guess[i] in answer and guess_char_count[guess[i]] < answer_char_count[guess[i]]:
            bit_string[i] = "1"
            guess_char_count[guess[i]] += 1

    return "".join(bit_string)