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

import PythonAuxiliaryFunctions.FilesIO.WriteFile as WriteFile


class TestWriteFile():
    @pytest.mark.parametrize('test_type, lines', [('string', 'test'),
                                                  ('list', ['test', 'list'])])
    def test_works(self, mocker, test_type, lines):

        print('Logging test type for visibility: ' + test_type)

        mocked_open = mocker.patch(
            'PythonAuxiliaryFunctions.FilesIO.WriteFile.open')

        WriteFile.write_file(lines, 'file.txt')

        mocked_open.assert_called()


class TestAppendFile():
    @pytest.mark.parametrize('test_type, lines', [('string', 'test'),
                                                  ('list', ['test', 'list'])])
    def test_works(self, mocker, test_type, lines):

        print('Logging test type for visibility: ' + test_type)

        mocked_open = mocker.patch(
            'PythonAuxiliaryFunctions.FilesIO.WriteFile.open')

        WriteFile.append_file(lines, 'file.txt')

        mocked_open.assert_called()
