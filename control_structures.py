#!/usr/bin/env python

import sys # used for the sys.exit function

int_condition = 7

if int_condition < 6:
    sys.exit("int_condition must be >= 6")
else:
    print("int_condition was >= 6 - continuing")