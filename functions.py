import random
import re
import constants as c


def assign(set_uniq, encoded_str):
    freq = {}
    for i in c.alphabet:
        freq.update({i.upper(): 0})

    order = {}

    for i in set_uniq:
        rand = random.randint(0, len(c.alphabet) - 1)
        new = c.alphabet.pop(rand)
        order.update({new.upper(): find(encoded_str, i)})

    encode_lst = list(encoded_str)

    for new in order:
        freq[new.upper()] = len(order[new])
        for i in order[new]:
            encode_lst = replace(encode_lst, int(i), new)

    final = "".join(encode_lst)
    return final, freq


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def replace(lst, i, ch):
    lst.insert(i, ch)
    lst.pop(i + 1)
    return lst


def hint(answer):
    if not c.hint_taken:
        hint_num = random.randint(1, 3)
        if hint_num == 1:
            print(f"The first word is '{answer.split(' ')[0]}'")
        elif hint_num == 2:
            print(f"The last word is '{answer.split(' ')[-1]}'")
        else:
            print(f"The quote contains the word '{answer.split(' ')[random.randint(0, len(answer.split(' ')) - 1)]}'")
        c.hint_taken = True
    else:
        print("You already took a hint.")


def take_input(og, freq):
    answer = og
    answer = answer.replace("'", "")
    answer = re.sub(r'\W+', ' ', answer.lower()).strip()

    if not c.hint_taken:
        user_ans = input("\nInput your translation (no punctuation required), \"other\""
                         " if you want other options, or \"exit\" to quit the program:\n").lower().strip()
    else:
        user_ans = input("\nInput your translation (no punctuation required):\n").lower().strip()
    while True:
        if user_ans == answer:
            print("\nCorrect!")
            break
        elif user_ans == "other":
            other_inp = input("\nDo you want a hint (type \"hint\"), the frequency table (type \"freq\"), "
                              "to reveal the quote (type \"reveal\"), "
                              "or to cancel (type \"cancel\")?\n").lower().strip()
            if other_inp == "hint":
                hint(answer)
            elif other_inp == "freq":
                print(freq)
            elif other_inp == "reveal":
                print(f"The answer is: \"{og}\"")
                c.revealed = True
                break
            elif other_inp == "cancel":
                take_input(answer, freq)
                break
            else:
                print("That's not a valid option.")
        elif user_ans == "exit" or c.revealed:
            break
        else:
            print("That's not a valid option.")
            take_input(answer, freq)
