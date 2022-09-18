#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Set a DICOM element.

"""

import os
import shutil

import pydicom

from dcm_pr_elem import dcm_pr_elem


def __check_file(filepath):
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        print('%s file not found.' % filepath, file=sys.stderr)
        return False
    return True


def dcm_set_elem(filepath, element, vfilepath):
    """Set a DICOM element.

    """

    if not __check_file(filepath):
        return

    if not __check_file(vfilepath):
        return

    with pydicom.dcmread(filepath) as ds:
        shutil.copy2(filepath, filepath + '.old')
        tag = pydicom.tag.Tag(element)
        e = ds[tag]
        with open(vfilepath, mode='rb') as vf:
            value = vf.read()
        e.value = value
        ds.save_as(filepath)
        dcm_pr_elem(filepath, element)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 4:
        dcm_set_elem(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print('Usage: dcm_set_str_elem.py filepath element value')
