#!/usr/bin/env python3
import subprocess
import sys

# YOUR CODE GOES here
from sys import argv
import os
from os import path

count_dict = {'dir_count': 0, 'file_count':0}
folder_dict = {}
indent_count = 0

def main():
    # check if there are no arguments
    if len(sys.argv) == 1:
        # do tree for entire current directory
        print(".")
        tree(os.getcwd())
        # print("current directory tree")
    else:
        INPUT_DIR = argv[1]
        # check if directory exists
        if not os.path.exists(INPUT_DIR):
            print(INPUT_DIR + " [error opening dir]")
        else:
            # print directory name
            print(INPUT_DIR)
            # print out directory and sub-directory contents
            tree(INPUT_DIR)
    print('')
    print(count_dict['dir_count'], "directories,", count_dict['file_count'], "files")

def tree(input_dir):
    (path, input_dir_name) = os.path.split(input_dir)
    if input_dir_name == '':
        (path, input_dir_name) = os.path.split(path)
    for dir_name, sub_dirs, files in os.walk(input_dir):
        # remove later, this is duplicate from print directory name above
        contents = sub_dirs+files
        contents.sort()
        # folder_dict.update((rootname, contents) for c in contents)
        for c in contents:
            c_dir = os.path.join(dir_name, c)
            (dname, fname) = os.path.split(c_dir)
            (root, rootname) = os.path.split(dname)
            folder_dict.update((rootname, contents) for c in contents)
    # print(folder_dict[input_dir_name])
    print_files(input_dir_name, folder_dict, 0)


def print_files(root_name, dict, indent_count):
    # the root node should be in the dictionary
    # print(root_name, dict)
    if root_name in dict:
        # for each value in the keys (ie each sub-directory/file under the root node)
        for a in dict[root_name]:
            # check if file by seeing if there is a corresponding key with values (sub-sub-directories/files)
            if a not in dict:
                count_dict['file_count']+=1
                indent_padding(indent_count)
                indent_count = 0
                # check to see if it is the last item
                if(a==dict[root_name][-1]):
                    print('`--', a)
                else:
                    print('|--', a)

            # else it's a sub-directory
            elif a in dict:
                indent_padding(indent_count)
                print('|--', a)
                count_dict['dir_count']+=1
                print_files(a, dict, indent_count+1)
                # for b in dict[a]:
                #     print('yooo', b)

def indent_padding(count):
    for i in range(count):
        print('|   ',end='')

if __name__ == '__main__':
    # just for demo
    # subprocess.run(['tree'] + sys.argv[1:])
    main()
