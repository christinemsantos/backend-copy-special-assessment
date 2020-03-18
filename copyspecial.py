#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "Christine Santos and Doug(demo)"


def get_special_paths(dir):
    special_paths = []
    files = os.listdir(dir)
    for file in files:
        if re.search(r'__\w+__', file):
            special_paths.append(file)
    return special_paths


def copy_to(path, files):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("Path Exists")

    for file in files:
        shutil.copy(file, path)


def zip_to(paths, zippath):
    paths = list(paths)
    command = "zip -j {} {}".format(zippath, ' '.join(paths))
    print("Command I am going to do: ")
    print(command)
    os.system(command)


def zip_to_two(paths, zippath):
    command = ['zip', '-j', zippath]
    command.extend(paths)
    print("Command I am going to do: {}".format(" ".join(command)))
    subprocess.check_output(command)

# Write functions and modify main() to call them


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fordir', help='src dir to look for local files')
    args = parser.parse_args()

    all_paths = get_special_paths(args.fromdir)

    if args.todir:
        copy_to(args.todir, all_paths)

    if args.tozip:
        zip_to_two(all_paths, args.tozip)

    if not args.todir and not args.tozip:
        print('\n'.join(all_paths))


if __name__ == "__main__":
    main()
