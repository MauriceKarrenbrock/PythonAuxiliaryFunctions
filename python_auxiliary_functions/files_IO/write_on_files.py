# -*- coding: utf-8 -*-
#############################################################
# Copyright (c) 2020-2020 Maurice Karrenbrock               #
#                                                           #
# This software is open-source and is distributed under the #
# BSD 3-Clause "New" or "Revised" License                   #
#############################################################
"""contains the generic functions needed to write files

contains the generic functions needed to write files
or append lines to a non formatted text file (.txt .pdb .tex ...)
"""


def write_file(lines, file_name='file.txt'):
    """This function writes a new file (or overwrides an existing one)

    The string must be correctly formatted with all the needed newlines when given as input

    Parameters
    -----------
    lines : iterable of strings or str
        anything that supports iteration like lists, tuples etc or a single string
    file_name : str
        default "new_file.txt"
    """

    if isinstance(lines, str):
        lines = [lines]

    with open(file_name, 'w') as f:

        for line in lines:

            f.write(line)


def append_file(lines, file_name='file.txt'):
    """This function appends lines to an existing file

    The string must be correctly formatted with all the needed newlines when given as input

    Parameters
    -----------
    lines : iterable of strings or str
        anything that supports iteration like lists, tuples etc or a single string
    file_name : str
        default "new_file.txt"
    """

    if isinstance(lines, str):
        lines = [lines]

    with open(file_name, 'a') as f:

        for line in lines:

            f.write(line)
