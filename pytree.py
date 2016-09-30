#!/usr/bin/env python3
import subprocess
import sys

# YOUR CODE GOES here
from sys import argv
import os
from os import path
import glob

count_dict = {'dir_count': 0, 'file_count':0}

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
    for dir_name, sub_dirs, files in os.walk(input_dir):
        # remove later, this is duplicate from print directory name above
        print('YOOOOOO ', dir_name, sub_dirs, files)
        contents = sub_dirs+files
        contents.sort()
        for c in contents:
            c_dir = os.path.join(dir_name, c)
            (dname, fname) = os.path.split(c_dir)
            indent_count = dname.count("/")
            if os.path.isdir(c_dir):
                for i in range(indent_count-1):
                    print('|   ',end="")
                print('|--',end="")
                print(c)
                # tree(c_dir)
                count_dict['dir_count']+=1
            elif c.count('.')>0:
                for i in range(indent_count-1):
                    print('|   ',end="")
                # if file, print it like a file
                print('`-- ',end="")
                print(c)
                count_dict['file_count']+=1
            else:
                print('|--',end="")
                print(c)

def indents(dir):
    (dname, fname) = os.path.split(c_dir)
    indent_count = dname.count("/")
    return(indent_count)

        # (dname, fname) = os.path.split(dir_name)
        # indent_count = dname.count("/")
        # # check if it's a file
        # if os.path.isfile(input_dir):
        #     # if file, print it like a file
        #     print('`-- ',input_dir)
        #     count_dict['file_count']+=1
        # # if the argument is not a file, then run the dir thing on it
        # else:
        #     if os.path.isdir(input_dir):
        #         print('|-- ', input_dir)
        #         for i in range(indent_count):
        #             print('|  ', end='')
        #         count_dict['dir_count']+=1
                    # tree(sub_dirs)

        # # Make the subdirectory names stand out with /
        # sub_dirs = [ '%s/' % n for n in sub_dirs ]
        # # Mix the directory contents together
        # contents = sub_dirs + files
        # contents.sort()
        # # Show the contents
        # tree_files(dir_name)

# def tree_files(directory):
#     if os.path.isdir(directory):
#         # indent = indent + '    ' if i == len(items) - 1 else indent + '|   '
#         # indent = indent[:-4]
#         count_dict['file_count']+=1
#     else:
#         count_dict['file_count']+=1

        # for sub in sub_directory_name:
        #     print(sub)
        # contents.sort()
        # for item in contents:
        #     subname = os.path.join(item)
        #     # print(contents, sub_directory_name, file_name)
        #     if os.path.isdir(subname):
        #         print("|", subname)
        #     else:
        #         print("yo")
        # count_dict['dir_count']+=1
        # for sub_directory in sub_directory_name:
        #     if os.path.isdir(directory_name):
        #         print('`-- ', end='')
        #         print(sub_directory_name)
        #         count_dict['dir_count']+=1
        #         for files in file_name:
        #             print('  %s' % files)
        #             count_dict['file_count']+=1


# def treee(input_dir):
#     for directory_name, sub_directory_name, files in os.walk(input_dir):
#         # print directory name
#         print(directory_name)
#         # (dirname, filename) = os.path.split(directory_name)
#         # print(dirname)
#         for i in range(count_dict['file_count']):
#             print('    ', end='')
#         sub_directory_name = [ '|--%s' % n for n in sub_directory_name]
#         # Mix the directory contents together
#         contents = files
#         # Show the contents
#         for c in contents:
#             count_dict['file_count']+=1
#             (dirname, filename) = os.path.split(c)
#             print('`--',filename)
#             # print('\t%s' % filename)
#         count_dict['dir_count']+=1


# def treee(input_dir):
#     for directory_name, sub_directory_name, files in os.walk(input_dir):
#         print(directory_name)
#         # Make the subdirectory names stand out with /
#         sub_directory_name = [ '%s/' % n for n in sub_directory_name ]
#         # Mix the directory contents together
#         contents = sub_directory_name + files
#         contents.sort()
#         # Show the contents
#         for c in contents:
#             count_dict['file_count']+=1
#             print('\t%s' % c)
#         count_dict['dir_count']+=1

def printfiles(directory):
    # if folder contains files
    print(glob.glob('*.py'))

    if not glob.glob(directory):
        for x in ['a', 'b', 'c']:
            # os.chdir(argv[0])
            # glob.glob('examples/*.xml')
            # (dirname, filename) = os.path.split(pathname)
            # print filename
            # print os.path.split(argv[1])
            print(x)
            for y in['x','y','z']:
                print(y)
                count_dict['file_count']+=1
            count_dict['dir_count']+=1


# check for folders
# if file

# print "input directory"
    # print(argv[1])
    # # loop through directories
    # if directory exists:
    #     print directory
    #     for directory in argv[1]:
    #         print("|--"+"directory")
    #         for folder in directory:
    #             print("|--" + "folder")

if __name__ == '__main__':
    # just for demo
    # subprocess.run(['tree'] + sys.argv[1:])
    main()
