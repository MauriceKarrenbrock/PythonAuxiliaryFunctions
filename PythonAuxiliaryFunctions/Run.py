# -*- coding: utf-8 -*-
#############################################################
# Copyright (c) 2020-2020 Maurice Karrenbrock               #
#                                                           #
# This software is open-source and is distributed under the #
# BSD 3-Clause "New" or "Revised" License                   #
#############################################################
"""Contains the functions needed to run external programs
"""

import os
import subprocess


def subprocess_run(commands,
                   shell=False,
                   universal_newlines=True,
                   error_string='error during the call of an external program',
                   cwd=os.getcwd()):
    """runs an external program using subprocess.run

    if it fails will print the standard output, standard error
    and raise RuntimeError

    Parameters
    ----------------
    commands : list
        it is the list of strings containing the command that
        subprocess.run will run
    shell : bool
        default False, if == True the commands will be executed in the shell
    universal_newlines : bool
        default False
    error_string : str
        the sting to give to the RuntimeError as argument
    cwd : str
        default the current working directory, it is the working directory for the child process

    Raises
    ---------------
    RuntimeError
        if the return code of the cild process is != 0
    """

    r = subprocess.run(commands,
                       shell=shell,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       universal_newlines=universal_newlines,
                       cwd=cwd,
                       check=False)

    print(r.stdout)
    print(r.stderr)

    if r.returncode != 0:
        raise RuntimeError(error_string)
