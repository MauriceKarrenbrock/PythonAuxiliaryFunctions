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

import PythonAuxiliaryFunctions.get_iterable as get_iterable


class Testget_iterable():
    def test_with_string(self):

        assert get_iterable.get_iterable('string') == ('string', )

    def test_with_empty_list(self):

        assert get_iterable.get_iterable([]) == []

    def test_with_list(self):

        assert get_iterable.get_iterable([1, 2]) == [1, 2]

    def test_with_int(self):

        assert get_iterable.get_iterable(1) == (1, )
