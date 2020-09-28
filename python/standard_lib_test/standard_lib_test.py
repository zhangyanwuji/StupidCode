import shutil
import sys
import random


def standard_lib_test():
    dir(shutil)


def print_args():
    print(sys.argv)


def print_a_random_number():
    print(random.choice(['alvin', 'bob', 'Carl', "Dell"]))
