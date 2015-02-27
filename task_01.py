#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This is my first function docstring.

    Arg:
       wink (str): To be used as a string.
       numwink (int): Arg to be used as an integer. Default=2

    Returns:
       str: Arguments will be used for a sentence.

    Example:
        >>> know_what_i_mean(wink, numwink=2)
        'Know what I mean? winkwink, nudgesnudges'
    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
