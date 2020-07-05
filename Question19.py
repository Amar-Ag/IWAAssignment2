"""
19.Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
"""


class py_solution:
    def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for bracket in str1:
            if bracket in pchar:  # Check if the given bracket is an open bracket
                stack.append(bracket)
                # If there is no opening bracket in stack or the last entered bracket
                # does not match the current closing bracket.
            elif len(stack) == 0 or pchar[stack.pop()] != bracket:
                return "Invalid"
        return "Valid" if len(stack) == 0 else "Invalid"


print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("({[)]"))
print(py_solution().is_valid_parenthese("()()"))
