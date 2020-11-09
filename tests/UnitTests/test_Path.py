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

import PythonAuxiliaryFunctions.Path as Path


class TestAbsoluteFilepath():
    def test_raises(self, mocker):

        mocker.patch('os.path.exists', return_value=False)

        with pytest.raises(FileNotFoundError):

            Path.absolute_filepath('DUM')

    def test_works(self, mocker):

        mocker.patch('os.path.exists', return_value=True)

        mocker.patch('os.path.abspath', return_value='true_path')
        mocker.patch('os.path.expanduser')
        mocker.patch('os.path.expandvars')

        assert Path.absolute_filepath('DUM') == 'true_path'


class TestWhich():
    def test_raises(self, mocker):

        mocker.patch('shutil.which', return_value=None)

        with pytest.raises(OSError):

            Path.which('DUM')

    def test_works(self, mocker):

        mocked_which = mocker.patch('shutil.which', return_value='true_path')

        assert Path.which('DUM') == 'true_path'

        mocked_which.assert_called_once()


class TestAbsoluteProgrampath():
    def test_raises(self, mocker):

        mocker.patch('PythonAuxiliaryFunctions.Path.absolute_filepath',
                     side_effect=FileNotFoundError)

        mocker.patch('PythonAuxiliaryFunctions.Path.which',
                     side_effect=OSError)

        with pytest.raises(OSError):

            Path.absolute_programpath('DUM')

    def test_which(self, mocker):

        mocked_wich = mocker.patch('PythonAuxiliaryFunctions.Path.which',
                                   return_value='true_path')

        assert Path.which('DUM') == 'true_path'

        mocked_wich.assert_called_once_with('DUM')

    def test_absolute_filepath(self, mocker):

        mocker.patch('PythonAuxiliaryFunctions.Path.which',
                     side_effect=OSError)

        mocked_path = mocker.patch(
            'PythonAuxiliaryFunctions.Path.absolute_filepath',
            return_value='true_path')

        assert Path.absolute_filepath('DUM') == 'true_path'

        mocked_path.assert_called_once_with('DUM')
