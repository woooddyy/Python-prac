# hexrep.py

import re

def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')

print(p.sub(hexrepl, 'Call 2020 for printing, 39393 for user code.'))
