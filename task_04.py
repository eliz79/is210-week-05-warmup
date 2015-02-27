#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defining parameters."""


def too_many_kittens(kittens, litterboxes, catfood):
    """Defining a function with parameters and boolean.

    Args:
        kittens(int): the number of kittens
        litterboxes(int): the number of litterboxes available
        catfood(bool): boolean representing if catfood exist or not

    Returns:
        A bool value to see wheather or not there is enough catfood.

    Example:
        >>>too_many_kittens(12, 12, False)
        True

        >>>too_many_kittens(13, 12, True)
        True

        >>>too_many_kittens(12, 13, True)
        False

    """

    return not (litterboxes >= kittens and catfood)

