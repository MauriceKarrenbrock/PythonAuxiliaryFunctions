# -*- coding: utf-8 -*-
#############################################################
# Copyright (c) 2020-2020 Maurice Karrenbrock               #
#                                                           #
# This software is open-source and is distributed under the #
# BSD 3-Clause "New" or "Revised" License                   #
#############################################################
"""Contains the function to get an iterable
"""

import collections


def get_iterable(x):
    """Returns an iterable, even if given a single value

    if x is a string returns (string,) even though a string is an iterable

    Parameters
    -------------
    x

    Returns
    ----------
    (`x`,)
        ONLY if the input is not an iterable or if it is a string
        if it is an iterable (not string) returns `x`
    """

    output = x

    if isinstance(x, str) or not isinstance(x, collections.Iterable):

        output = (x, )

    return output
