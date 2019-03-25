"""
Code takes an formatted string as input
Returns a random possible sentence
Assumption: The String is properly formatted as per the given description i.e. for every opening brace,
there is a valid closing brace.
Error Handling is not performed.
"""
import random


def generate_valid_sentence(string):
    # Stack keeps track of each of the possible options
    i = 0
    stack = []
    while i < (len(string)):
        # Inserting the Index of '{' into the stack
        if string[i] == '{':
            stack.append(i)
        # Popping the Stack when '}' is encountered
        if string[i] == '}':
            prev_start_index = stack.pop()
            # Once we have an opening and closing, manipulate the string to generate a random valid sentence.
            string, offset = manipulate_string(string, prev_start_index, i)
            # After the string is reduced to a valid option, we change the index of i as per the offset
            i -= offset
        i += 1
    return string


# This method updates the current string by replacing a set of possible options by a single random option
def manipulate_string(string, start, end):
    current_block = string[start + 1:end]
    current_block_tokens = current_block.split('|')
    random_index = random.randint(0, len(current_block_tokens) - 1)
    string = string[:start] + current_block_tokens[random_index] + string[end + 1:]
    # Getting the number of characters to be deleted from the original string to perform the manipulation
    offset = len(current_block) - len(current_block_tokens[random_index]) + 2
    return string, offset


string = "{I am|I'm} {working on|starting} this {online |}interview. I hope Cortx thinks I am {{very|extremely} qualified|great|awesome}{!|.}"
print(generate_valid_sentence(string))