import argparse


def test1():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose",
                        help="Show detailed infomation",
                        type=int, choices=[0, 1, 2, 3])
    args = parser.parse_args()
    if args.verbose == 0:
        print(args.verbose)
    elif args.verbose == 1:
        print("verbose =:", args.verbose)
    elif args.verbose == 2:
        print("verbose level is:", args.verbose)
    else:
        print("This is the top verbeosity level 3")
