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

import pytest

import PythonAuxiliaryFunctions.files_IO.write_file as write_file


class Testwrite_file():
    @pytest.mark.parametrize('test_type, lines', [('string', 'test'),
                                                  ('list', ['test', 'list'])])
    def test_works(self, mocker, test_type, lines):

        print('Logging test type for visibility: ' + test_type)

        mocked_open = mocker.patch(
            'PythonAuxiliaryFunctions.files_IO.write_file.open')

        write_file.write_file(lines, 'file.txt')

        mocked_open.assert_called()


class TestAppendFile():
    @pytest.mark.parametrize('test_type, lines', [('string', 'test'),
                                                  ('list', ['test', 'list'])])
    def test_works(self, mocker, test_type, lines):

        print('Logging test type for visibility: ' + test_type)

        mocked_open = mocker.patch(
            'PythonAuxiliaryFunctions.files_IO.write_file.open')

        write_file.append_file(lines, 'file.txt')

        mocked_open.assert_called()
