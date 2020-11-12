# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring
# pylint: disable=redefined-outer-name
# pylint: disable=no-self-use
#############################################################
# Copyright (c) 2020-2020 Maurice Karrenbrock               #
#                                                           #
# This software is open-source and is distributed under the #
# BSD 3-Clause "New" or "Revised" License                   #
#############################################################

import PythonAuxiliaryFunctions.files_IO.read_file as read_file


class Testread_file():
    def test_works(self, mocker):

        mocked_open = mocker.patch(
            'PythonAuxiliaryFunctions.files_IO.read_file.open')

        read_file.read_file(file_name='DUM')

        mocked_open.assert_called()
