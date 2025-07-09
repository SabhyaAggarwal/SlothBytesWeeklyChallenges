def find_broken_keys(txt1, txt2):
    broken_keys_found = []
    min_length = min(len(txt1), len(txt2))

    for i in range(min_length):
        correct_char = txt1[i]
        typed_char = txt2[i]

        if correct_char != typed_char:
            if correct_char not in broken_keys_found:
                broken_keys_found.append(correct_char)

    return broken_keys_found
