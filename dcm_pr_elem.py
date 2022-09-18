#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Print a DICOM element.

"""

import os

import pydicom


def __check_file(filepath):
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        print('%s file not found.' % filepath, file=sys.stderr)
        return False
    return True


def dcm_pr_elem(filepath, element):
    """Print a DICOM element.

    """

    if not __check_file(filepath):
        return

    with pydicom.dcmread(filepath) as ds:
        tag = pydicom.tag.Tag(element)
        e = ds.get_item(tag)
        print(f"{e.tag} {e.VR} {e.length} bytes: {e.value}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 3:
        dcm_pr_elem(sys.argv[1], sys.argv[2])
    else:
        print('Usage: dcm_pr_elem.py filepath element')
