def next_letters(s: str) -> str:
    if not s:
        print("A")
        return "A"

    chars = list(s)
    n = len(chars)

    carry = True

    for i in range(n - 1, -1, -1):
        if not carry:
            break

        if chars[i] == 'Z':
            chars[i] = 'A'
            carry = True
        else:
            chars[i] = chr(ord(chars[i]) + 1)
            carry = False

    if carry:
        chars.insert(0, 'A')

    result = "".join(chars)
    print(result)
    return result
