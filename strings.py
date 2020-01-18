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

