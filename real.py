import re
# TODO Handle what gets written when special characters are used within a character class
# TODO Error out/return an error if the closing bracket is missing

# Convert from REAL to regex
re_dict = {
    "anything":".",
    "alphaNum":"\w",
    "nonAlphaNum":"\W",
    "digit":"\d",
    "nonDigit":"\D",
    "whitespaceChar":"\s",
    "nonWhitespaceChar":"\S",
    "characterClass":"[",
    "characterClassEnd":"]",
    "not":"^",
}

def toRegex(expression): # To regex
    regex_list = []
    slash_before = False
    list_of_words = expression.split(" ")
    for word in list_of_words:
        regex_list.append(re_dict.get(word, word)) # If the expression is not found, return the expression
    return "".join(regex_list)

# Convert from regex to REAL
real_dict = {
    ".":"anything",
    "\w":"alphaNum",
    "\W":"nonAlphaNum",
    "\d":"digit",
    "\D":"nonDigit",
    "\s":"whitespaceChar",
    "\S":"nonWhitespaceChar",
    "[":"characterClass",
    "]":"characterClassEnd",
    "^":"not",
}

def toReal(expression): # To REAL 
    real_list = []
    slash_before = False
    for character in expression:

        ### Handle backslashes(\)
        if character == "\\" and slash_before: # If this character is a slash and the one before was also a slash
            transmuted = real_dict.get("\\\\", "\\\\")
            slash_before = False

        elif character == "\\": # If only the previous character is a slash
            slash_before = True
            
        else:
            if slash_before:
                transmuted = real_dict.get("\\" + character, "\\" + character)
                real_list.append(transmuted)
                slash_before = False

            else:
                transmuted = real_dict.get(character, character) # If the expression is not found, return the expression
                real_list.append(transmuted)

    return_string = " ".join(real_list)
    return return_string

if __name__ == "__main__":
    # Test the functionality of the functions
    reg_exp = "[A-Z^$.]"
    print(reg_exp)
    test_string = r"""
    This is a simple test for regular2#
    expressions 435^985ab t3 (*($$*#%(**
    W%(U$*(%U(*#@'''""WU%(!!@))))))).
    still a number 443-551
    """
    matched = re.findall(reg_exp, test_string)
    print(matched)

    real_string = toReal(reg_exp)
    print(real_string)
    regex_string = toRegex(real_string)
    print(regex_string)

    assert(regex_string == reg_exp)

    print("\n")
    my_regex = toRegex("digit digit nonDigit")
    matched_strings = re.findall(my_regex, test_string)
    print(matched_strings)