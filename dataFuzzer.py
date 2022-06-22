import random as rd
import string


def fuzz(
    txt,
    insert_str=False,
    insert_num=False,
    insert_float=False,
    insert_space_chars=False,
    append_space_char=False,
    delete_chars=False,
    replace_none=False,
):
    """
    input text will be randomly modified according to the specified options
    if no options are selected one will be picked for you
    """
    opts = [
        insert_str,
        insert_num,
        insert_float,
        insert_space_chars,
        append_space_char,
        delete_chars,
        replace_none,
    ]
    action = None
    if not any(opts):
        action = rd.randrange(0, len(opts))

    # index location to perform action
    i = rd.randint(0, len(txt))

    if insert_str or action == 0:
        letters = string.ascii_lowercase
        s = "".join(rd.choices(letters, k=5))
        res = txt[:i] + s + txt[i:]

    elif insert_num or action == 1:
        s = rd.randint(0, 10)
        res = txt[:i] + str(s) + txt[i:]

    elif insert_float or action == 2:
        s = rd.random() + 1
        res = txt[:i] + str(s) + txt[i:]

    elif insert_space_chars or action == 3:
        s = rd.choice(["\t", "\n", "\r", " "])
        res = txt[:i] + s + txt[i:]

    elif append_space_char or action == 4:
        s = rd.choice(["\t", "\n", "\r", " "])
        res = txt + s

    elif delete_chars or action == 5:
        # randomize end of range
        u = rd.randint(i + 1, len(txt))
        res = txt[:i] + "" + txt[u:]

    elif replace_none or action == 6:
        # ~20% chance to be replaced with none
        if rd.randint(1, 5) == 3:
            s = rd.choice(["", None, " "])
            res = txt + s
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
