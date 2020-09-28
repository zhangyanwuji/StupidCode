def file_read():
    with open("test.txt") as f:
        read_data = f.read()
        return read_data


def file_readline():
    with open("test.txt") as f:
        read_data = f.readline()
        return read_data


def dump_file():
    with open("test.txt") as f:
        for line in f:
            print(line, end='')


def file_to_list():
    with open("test.txt") as f:
        conten_list = list(f)
        return conten_list
