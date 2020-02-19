import re


def extract_re(text, *expressions):

    """Extract regex-captured fragments from text as comma-separated string"""

    output_str = ''

    for expression in expressions:
        found = re.findall(expression, text)
        if found:
            sep = ''
            if output_str:
                sep = ', '
            output_str += sep + ', '.join(found)

    return output_str.strip()


def from_last_upper(text):
    r"""
    Return a slice of a given text starting from last upper case.
    Return input text if upper case is not present.
    """
    for index, char in enumerate(text[::-1]):
        if char.isupper():
            return text[-index-1:]
    return text


def is_any_lowercase(text):

    """Return True if any lowercase character is found"""

    return bool([char for char in text if char.islower()])


def remove_re(text, *expressions):

    """Remove regex-captured fragments from text"""

    for expression in expressions:
        found = re.findall(expression, text)
        if found:
            removed = text

            for hit in found:
                removed = re.sub(expression, '', removed)

            text = removed

    return text.strip()

