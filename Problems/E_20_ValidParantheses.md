# Task
Given a string _s_ containing just the characters _'('_, _')'_, _'{'_, _'}'_, _'['_ and _']'_, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

# Examples:
- Input: s = "()"
- Output: true

- Input: s = "(]"
- Output: false

# Constraints:
- 1 <= s.length <= 10^4
- _s_ consists of parantheses only