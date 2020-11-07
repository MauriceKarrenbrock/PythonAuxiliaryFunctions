# -*- coding: utf-8 -*-
#############################################################
# Copyright (c) 2020-2020 Maurice Karrenbrock               #
#                                                           #
# This software is open-source and is distributed under the #
# BSD 3-Clause "New" or "Revised" License                   #
#############################################################
"""Contains the function to read a standard .txt file
"""


def read_file(file_name):
    """Reads the given text file, returns list containing the lines

    Parameters
    -----------------
    file : str

    Reurns
    ---------
    list of strings

    Notes
    -------------
    It saves the whole file in memory, therefore can have problems with very big files"""

    with open(file_name, 'r') as f:

        lines = f.readlines()

    return lines
