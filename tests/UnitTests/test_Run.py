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

import unittest.mock as mock

import pytest

import PythonAuxiliaryFunctions.Run as Run


class TestSubprocessRun():
    def test_raises(self, mocker):

        return_object = mock.MagicMock()
        return_object.returncode = 1

        mocked_run = mocker.patch(
            'PythonAuxiliaryFunctions.Run.subprocess.run',
            return_value=return_object)

        mocked_print = mocker.patch('PythonAuxiliaryFunctions.Run.print')

        with pytest.raises(RuntimeError):

            Run.subprocess_run(['a', 'b'])

        mocked_run.assert_called_once()

        mocked_print.assert_called()

    def test_works(self, mocker):

        return_object = mock.MagicMock()
        return_object.returncode = 0

        mocked_run = mocker.patch(
            'PythonAuxiliaryFunctions.Run.subprocess.run',
            return_value=return_object)

        mocked_print = mocker.patch('PythonAuxiliaryFunctions.Run.print')

        Run.subprocess_run(['a', 'b'])

        mocked_run.assert_called_once()

        mocked_print.assert_called()
