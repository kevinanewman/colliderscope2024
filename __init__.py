import pandas as pd

print('\n--- Colliderscope executable launching, this may take a few moments ---\n')

code_version = '0.0.17'


def print_dict(dict_in, num_tabs=0, to_string=False):
    """
    Attempt to pretty-print a dictionary to the Python console.

    Args:
        dict_in (dict): dictionary to print
        num_tabs (int): optional argument, used to indent subsequent layers of the dictionary
        to_string (Bool): if True then result will be returned as a printable string, instead of printed to the console

    Returns:
        print_dict string if to_string==True

    """
    s = ''

    if num_tabs == 0:
        s += '\n'
        if type(dict_in) is pd.Series:
            dict_in = dict_in.to_dict()

    if type(dict_in) is list or type(dict_in) is not dict:
        s += '\t' * num_tabs + str(dict_in) + '\n'
    else:
        try:
            keys = sorted(dict_in.keys())
        except:
            keys = dict_in.keys()

        for k in keys:
            if type(dict_in[k]) is list:
                if dict_in[k]:
                    s += '\t' * num_tabs + str(k) + ':' + str(dict_in[k]) + '\n'
                else:
                    s += '\t' * num_tabs + str(k) + '\n'
            else:
                s += '\t' * num_tabs + str(k) + '\n'
                s += print_dict(dict_in[k], num_tabs + 1, to_string=True)

    if num_tabs == 0:
        s += '\n'

    if not to_string:
        print(s[:-1])

    if to_string:
        return s
