#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Print DICOM pixel data.

"""

import os

import matplotlib.pyplot as plt
import pydicom


def __check_file(filepath):
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        print('%s file not found.' % filepath, file=sys.stderr)
        return False
    return True


def dcm_pr_image(filepath):
    """Print DICOM pixel data.

    """

    if not __check_file(filepath):
        return

    with pydicom.dcmread(filepath) as ds:
        plt.imshow(ds.pixel_array)
        plt.show()


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        dcm_pr_image(sys.argv[1])
    else:
        print('Usage: dcm_pr_image.py filepath')
