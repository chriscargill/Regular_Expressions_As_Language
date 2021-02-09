import re

reg_exp = "\D.a\w"
test_string = r"""This is a simple test for regular expressoins 435985ab t3 (*(*#%(**W%(U*(%U(*#@'''""WU%(!!@)))))))."""
matched = re.findall(reg_exp, test_string)
print(matched)

# If the expression is not found, return the expression




# convert from REAL to regex
re_dict = {
    "anything":".",
    "alphaNum":"\w",

}

def regex(expression): # To regex
    return re_dict.get(expression, expression)



###### ######



# convert from regex to REAL
real_dict = {
    ".":"anything",
    "\w":"alphaNum",
    "\d":"digit",
    "\D":"nonDigit",


}

def real(expression): # To real 
    real_list = []
    slash_before = False
    for character in expression:
        ### Handle backslashes(\)
        if character == "\\":
            slash_before = True
        else:
            if slash_before:
                transmuted = real_dict.get("\\" + character, "\\" + character)
                real_list.append(transmuted)
                slash_before = False
            else:
                transmuted = real_dict.get(character, character)
                real_list.append(transmuted)
    return_string = " ".join(real_list)
    return return_string

test_string = r"""This is a simple test for regular expressoins 435985 t3 (*(*#%(**W%(U*(%U(*#@'''""WU%(!!@)))))))."""

real_string = real(reg_exp)
print(real_string)