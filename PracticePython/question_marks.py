"""
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks,
and check if there are exactly 3 question marks between every pair of two numbers that add up to 10.
If so, then your program should return the string true, otherwise it should return the string false.
If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

Input:"aa6?9"
Output:"false"

Input:"acc?7??sss?3rr1??????5"
Output:"true"
"""


def QuestionsMarks(input: str):
    start = end = -1
    question_marks = 0
    for c in input:
        if c.isdigit():
            if start < 0:
                start = int(c)
            elif end < 0:
                end = int(c)
        else:
            if start < 0:  # string not started
                continue
            elif end < 0:  # end of string not reached yet
                if c == '?':
                    question_marks += 1
            else:  # end of string
                if start + end == 10 and question_marks == 3:
                    return True
                else:
                    start, end, question_marks = 0, 0, 0
    return False


# keep this function call here
print(QuestionsMarks('aa6?9'))
print(QuestionsMarks('acc?7??sss?3rr1??????5'))