from typing import List


def parse_csv_line(line: str, quotechar: str = "'", delim: str = ",") -> List[str]:
    """A simple CSV parser that parse one line of csv without newline symbol"""
    field = ""
    fields = []
    in_quote = False
    prev_char = None

    for char in line:
        if char == delim:
            if in_quote:
                field += char
            elif prev_char == quotechar:
                pass
            else:
                fields.append(field)
                field = ''
        elif char == quotechar:
            if in_quote:
                fields.append(field)
                field = ""
                in_quote = False
            else:
                in_quote = True
        else:
            field += char

        prev_char = char

    fields.append(field)
    return fields


def test():
    lines = [
        (",,", ["", "", ""]),
        ("csv,parser", ["csv", "parser"]),
        ("'a','b,cd,ef',g,h,'a',", ['a', 'b,cd,ef', 'g', 'h', 'a', ''])
    ]

    for line, parsed_lin in lines:
        assert parse_csv_line(line) == parsed_lin

test()