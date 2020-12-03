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

import pathlib

import pytest

import PythonAuxiliaryFunctions.path as path


class TestAbsoluteFilepath():
    def test_raises(self, mocker):

        mocker.patch('os.path.exists', return_value=False)

        with pytest.raises(FileNotFoundError):

            path.absolute_filepath('DUM')

    def test_works(self, mocker):

        mocker.patch.object(pathlib.Path, 'exists', return_value=True)

        mocker.patch.object(pathlib.Path,
                            'resolve',
                            return_value=pathlib.Path('true_path'))
        mocker.patch.object(pathlib.Path,
                            'expanduser',
                            return_value=pathlib.Path)
        mocker.patch('os.path.expandvars', return_value='DUM')

        assert path.absolute_filepath('DUM') == pathlib.Path('true_path')


class TestWhich():
    def test_raises(self, mocker):

        mocker.patch('shutil.which', return_value=None)

        with pytest.raises(OSError):

            path.which('DUM')

    def test_works(self, mocker):

        mocked_which = mocker.patch('shutil.which', return_value='true_path')

        assert path.which('DUM') == pathlib.Path('true_path')

        mocked_which.assert_called_once()


class TestAbsoluteProgrampath():
    def test_raises(self, mocker):

        mocker.patch('PythonAuxiliaryFunctions.path.absolute_filepath',
                     side_effect=FileNotFoundError)

        mocker.patch('PythonAuxiliaryFunctions.path.which',
                     side_effect=OSError)

        with pytest.raises(OSError):

            path.absolute_programpath('DUM')

    def test_which(self, mocker):

        mocked_wich = mocker.patch('PythonAuxiliaryFunctions.path.which',
                                   return_value='true_path')

        assert path.which('DUM') == 'true_path'

        mocked_wich.assert_called_once_with('DUM')

    def test_absolute_filepath(self, mocker):

        mocker.patch('PythonAuxiliaryFunctions.path.which',
                     side_effect=OSError)

        mocked_path = mocker.patch(
            'PythonAuxiliaryFunctions.path.absolute_filepath',
            return_value='true_path')

        assert path.absolute_filepath('DUM') == 'true_path'

        mocked_path.assert_called_once_with('DUM')
