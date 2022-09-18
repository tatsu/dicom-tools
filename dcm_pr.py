#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Print DICOM file.

"""

import os

import pydicom


def __check_file(filepath):
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        print('%s file not found.' % filepath, file=sys.stderr)
        return False
    return True


def dcm_pr(filepath):
    """Print DICOM file.

    """

    if not __check_file(filepath):
        return

    with pydicom.dcmread(filepath) as ds:
        print(ds)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        dcm_pr(sys.argv[1])
    else:
        print('Usage: dcm_pr.py filepath')
