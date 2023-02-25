"""
try:

    try:
        xxx
    except XXError:
        xxx
except Error:
    xxx
"""

try:
    try:
        try:
            num = int(input('num:'))
            result = num / 0
        except NameError as e:
            print(e)
    except ValueError as e:
        print(e)
except ZeroDivisionError as e:
    print(e)
