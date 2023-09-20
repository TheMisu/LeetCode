def valid_parantheses(s: str) -> bool:
    # make a list with the types of parans 
    open_paran = ["(", "[", "{"]
    close_paran = [")", "]", "}"]

    # create a dict to save the pairs
    pair_dict = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    # init a stack to keep track of the last open param
    stack = []

    # iterate through the input str
    for char in s:
        # push the char to the stack if it is an open paran
        if char in open_paran:
            stack.append(char)
        else:
            # if the stack is empty, that means we have 
            # no open paran to match with
            if len(stack) == 0:
                return False
            
            # check if the last open paran matches the current char
            last_open_paran = stack.pop()
            if pair_dict[last_open_paran] != char:
                return False
            
    # after iterating through the entire string, we will be left with 
    # either an empty stack (all brackets have been matched) or a stack
    # that still has open paran in it (not properly matched)
    if len(stack) == 0:
        return True
    else:
        return False
    
print(valid_parantheses("()"))
print(valid_parantheses("(])"))

    