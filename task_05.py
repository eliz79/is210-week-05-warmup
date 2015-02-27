#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setting a default value."""


def defaults(my_required, my_optional=True):
    """Defining default values to parameters.

    Arg:
        my_optional(bool): boolean representing True by default
        my_required(mixed): no default value

    Return:
        A logical comparison between two parameters.

    Example:
        >>>defaults(True)
        True
        >>>defaults(True, False)
        False
        >>>(False, False)
        True


    """

    return my_optional is my_required
