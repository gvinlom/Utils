import random as rd
import string


def fuzz(txt, action=None, k=5):
    """
    input text will be randomly modified according to the specified options
    if no options are selected one will be picked for you
    """
    opts = [
        "insert_str",
        "insert_num",
        "insert_float",
        "insert_space_chars",
        "append_space_char",
        "delete_chars",
        "replace_none",
    ]
    if action == None:
        action = rd.choice(opts)

    # index location to perform action
    i = rd.randint(0, len(txt))

    if action == "insert_str":
        letters = string.ascii_lowercase
        s = "".join(rd.choices(letters, k=k))
        res = txt[:i] + s + txt[i:]

    elif action == "insert_num":
        s = "".join(rd.choices(string.digits, k=k))
        res = txt[:i] + s + txt[i:]

    elif action == "insert_float":
        s = rd.random() + 1
        res = txt[:i] + str(s) + txt[i:]

    elif action == "insert_space_chars":
        s = rd.choice(["\t", "\n", "\r", " "])
        res = txt[:i] + s + txt[i:]

    elif action == "append_space_char":
        s = rd.choice(["\t", "\n", "\r", " "])
        res = txt + s

    elif action == "delete_chars":
        # randomize end of range
        u = rd.randint(i + 1, len(txt))
        res = txt[:i] + "" + txt[u:]

    elif action == "replace_none":
        # ~20% chance to be replaced with none
        if rd.randint(1, 5) == 3:
            s = rd.choice(["", None, " "])
            res = s
        else:
            res = txt

    return res


def get_rand_str(len, alphanumeric=False):
    """
    return random string of length 'len'
    """
    letters = string.ascii_letters
    if alphanumeric:
        letters += string.digits
        return "".join(rd.choices(letters, k=len))
    else:
        return "".join(rd.choices(letters, k=len))


def get_rand_arr(e_len, y, x=0, header=[], alphanumeric=False, usefuzz=False, **kwargs):
    """
    kwargs are keyword arguments passed directly to fuzz
    rand_na will popluate None randomly for ~20% of entries 
    """
    dat = []

    for i in range(y):
        dat.append([])
        for n in range(max(x, len(header))):
            if usefuzz:
                dat[i].append(fuzz(get_rand_str(e_len, alphanumeric), **kwargs))
            else:
                dat[i].append(get_rand_str(e_len, alphanumeric))
    if header:
        dat.insert(0, header)
    return dat
