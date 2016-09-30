#!/usr/bin/env python3
import subprocess
import sys

# YOUR CODE GOES here
from sys import argv
import os
from os import path
import re

count_dict = {'dir_count': 0, 'file_count': 0}
folder_dict = {}
indent_count = 0
indent_of_indent_count = 0

def main():
    # check if there are no arguments
    if len(sys.argv) == 1:
        # do tree for entire current directory
        print(".")
        tree(os.getcwd())
    # otherwise, if there is an argument
    else:
        INPUT_DIR = argv[1]
        # check if directory exists
        if not os.path.exists(INPUT_DIR):
            print(INPUT_DIR + " [error opening dir]")
        else:
            # print directory name
            print(INPUT_DIR)
            # call tree function
            tree(INPUT_DIR)
    print('')
    # check for pluralization
    if count_dict['dir_count']!=1:
        if count_dict['file_count']!=1:
            print(count_dict['dir_count'], "directories,", count_dict['file_count'], "files")
        else:
            print(count_dict['dir_count'], "directories,", count_dict['file_count'], "file")
    else:
        if count_dict['file_count']!=1:
            print(count_dict['dir_count'], "directory,", count_dict['file_count'], "files")
        else:
            print(count_dict['dir_count'], "directory,", count_dict['file_count'], "file")

def tree(input_dir):
    (path, input_dir_name) = os.path.split(input_dir)
    if input_dir_name == '':
        (path, input_dir_name) = os.path.split(path)
    for dir_name, sub_dirs, files in os.walk(input_dir):
        # remove hidden folders
        for f in files[:]:
            if f.startswith('.'):
                # sub_dirs.remove(f)
                files.remove(f)
        for s in sub_dirs[:]:
            if s.startswith('.'):
                # sub_dirs.remove(f)
                sub_dirs.remove(s)
        for d in dir_name[:]:
            if d.startswith('.'):
                # sub_dirs.remove(f)
                dir_name.remove(d)
        # add contents and sort
        contents = sub_dirs + files
        # contents = sorted(contents, key=lambda x: x.strip('_').lower()
        contents.sort()
        # folder_dict.update((rootname, contents) for c in contents)
        for c in contents:
            c_dir = os.path.join(dir_name, c)
            (dname, fname) = os.path.split(c_dir)
            (root, rootname) = os.path.split(dname)
            folder_dict.update((rootname, contents) for c in contents)
    # print(folder_dict[input_dir_name])
    print_files(input_dir_name, folder_dict, 0, 0)

def print_files(root_name, dict, indent_count, indent_of_indent_count):
    # the root node should be in the dictionary
    # print(root_name, dict)
    if root_name in dict:
        # for each value in the keys (ie each sub-directory/file under the root node)
        for a in dict[root_name]:
            # check if file by seeing if there is a corresponding key with values (sub-sub-directories/files)
            if a not in dict:
                count_dict['file_count'] += 1
                indent_padding(indent_of_indent_count, indent_count)

                # check to see if it is the last item
                if(a == dict[root_name][-1]):
                    print('`--', a)
                    indent_of_indent_count += 1 # not sure
                    indent_count = 0 # not sure
                else:
                    # indent_padding(indent_of_indent_count, indent_count)
                    # indent_padding(0, 1)
                    print('|--', a)

            # else it's a sub-directory
            elif a in dict:
                if(a == dict[root_name][-1]):
                    indent_padding(indent_of_indent_count, indent_count)
                    print('`--', a)
                    indent_of_indent_count += 1
                    indent_count = 0 # not sure
                else:
                    indent_padding(indent_of_indent_count, indent_count)
                    print('|--', a)
                count_dict['dir_count'] += 1
                print_files(a, dict, indent_count + 1, indent_of_indent_count)
                # for b in dict[a]:
                #     print('yooo', b)
        indent_count = 0

def indent_padding(begin_index, count):
    # need to account for parent indent level (that is the starting base)
    for i in range(begin_index):
        print('    ', end = '')
    for i in range(count-begin_index):
        print('|   ', end = '')

if __name__ == '__main__':
    # just for demo
    # subprocess.run(['tree'] + sys.argv[1:])
    main()
