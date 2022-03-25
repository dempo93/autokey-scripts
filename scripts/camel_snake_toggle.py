import stringcase
from enum import Enum


def selection_or_exit():
    try:
        return clipboard.get_selection()
    except Exception:
        exit(0)


class Case(Enum):
    UNKNOWN = 0
    PASCAL = 1
    CAMEL = 2
    SNAKE = 3
    SCREAMING_SNAKE = 4


def get_string_case(text):
    is_upper = text.isupper()
    is_lower = text.islower()
    if is_lower:
        return Case.SNAKE
    if is_upper:
        return Case.SCREAMING_SNAKE
    if not is_lower and not is_upper and text.find("_") == -1:
        if text[0].isupper:
            return Case.PASCAL
        else:
            return Case.CAMEL
    return Case.UNKNOWN


def convert(text, case):
    if case is Case.PASCAL:
        return stringcase.camelcase(text)
    if case is Case.CAMEL:
        return stringcase.snakecase(text)
    if case is Case.SNAKE:
        return stringcase.constcase(text)
    return stringcase.pascalcase(text)


def replace_text_and_select(text):
    keyboard.send_keys('<delete>' + text + '<ctrl>+<shift>+<left>')


# Converts in the following order
# (Unknown) -> PascalCase -> camelCase -> snake_case -> SCREAMING_SNAKE_CASE
text_to_convert = selection_or_exit()
text_case = get_string_case(text_to_convert)
converted_text = convert(text_to_convert, text_case)
replace_text_and_select(converted_text)
