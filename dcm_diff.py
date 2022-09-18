#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Analyse differences between DICOM files.

"""

import difflib
import os

import pydicom


def __check_file(filepath):
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        print('%s file not found.' % filepath, file=sys.stderr)
        return False
    return True


def dcm_diff(filepath1, filepath2):
    """Analyse differences between DICOM files.

    """

    if not __check_file(filepath1):
        return

    if not __check_file(filepath2):
        return

    datasets = tuple([pydicom.dcmread(filename, force=True) for filename in
                      (filepath1, filepath2)])

    rep = []
    for dataset in datasets:
        lines = str(dataset).split("\n")
        # lines = [line + "\n" for line in lines]  # add the newline to end
        rep.append(lines)

    diff = difflib.Differ()
    for line in diff.compare(rep[0], rep[1]):
        if line[0] != "?" and line[0] != " ":
            print(line)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 3:
        dcm_diff(sys.argv[1], sys.argv[2])
    else:
        print('Usage: dcm_diff.py filepath1 filepath2')
