# -*- coding: utf-8 -*-
#############################################################
# Copyright (c) 2020-2020 Maurice Karrenbrock               #
#                                                           #
# This software is open-source and is distributed under the #
# BSD 3-Clause "New" or "Revised" License                   #
#############################################################
"""contains the functions needed to get absolute paths for files and executables
"""

import os.path
import pathlib
import shutil


def absolute_filepath(path):
    """Takes a string or a pathlib.Path and returns the absolute path of the file

    If the file does not exist raises a FileNotFoundError

    Parameters
    --------------
    path : str or pathlib.Path

    Returns
    ------------------
    absolute_path : pathlib.Path
        all ambient variables are resolved
        user variables (~ in linux) are resolved
        the path is absolute

    Raises
    ---------------
    FileNotFoundError
        if the file is not found
    """

    if not isinstance(path, str):

        path = str(path)

    path = os.path.expandvars(path)

    absolute_path = pathlib.Path(path)

    absolute_path = absolute_path.expanduser()

    absolute_path = absolute_path.resolve()

    if not absolute_path.exists():
        raise FileNotFoundError(f'{absolute_path}')

    return absolute_path


def which(program):
    """get the absolute path of an executable that is in $path

    If you don't know if the program is in $path or not use absolute_programpath(program)
    Uses shutil.which
    example: path = which("python"), path = /usr/bin/python
    If the executable doesn't exist raises a OSError

    Parameters
    ---------------------
    program : str
        the name of the program you have in $path and that you want
        to have the absolute path of

    Returns
    ------------
    absolute_path : pathlib.Path

    Raises
    ---------
    OSError
        if the input is not in path
    """

    absolute_path = shutil.which(program)

    if absolute_path is None:
        raise OSError(f'{program} is not in $path')

    return pathlib.Path(absolute_path)


def absolute_programpath(program):
    """It returns the absolute path to an executable both if it is in $path or not

    if the executable doesn't exist raises an OSError
    it is a handy wrapper of `which` and `absolute_filepath`

    Parameters
    ------------------
    program : str
        can be the name of the executable in $path
        or a relative path to it

    Returns
    ------------
    absolute_path : pathlib.Path

    Raises
    --------------
    OSError
        if the executable doesn't exist both in $path nor in the
        relative path given as input
    """

    try:

        try:

            absolute_path = which(program=program)

        except OSError:

            absolute_path = absolute_filepath(path=program)

    except FileNotFoundError:

        raise OSError(  # pylint:disable=raise-missing-from
            f"{program} doesn't exist both in path and in the normal directories"
        )

    return absolute_path
