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

    return output_str

