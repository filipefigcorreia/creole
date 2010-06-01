#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import doctest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import creole.genshi_emitter

if __name__ == "__main__":
    doctest.testmod(creole.genshi_emitter)
