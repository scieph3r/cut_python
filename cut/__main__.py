import argparse
from sys import stdin

def main():
    # create parser
    parser = argparse.ArgumentParser(description="My version of cut program")
    
    # add arguments
    parser.add_argument("filepath", nargs="?", help="Path to the file")
    parser.add_argument("-f", "--fields", type=str, help="Specify return fields")
    parser.add_argument("-d", "--delimiter", type=str, help="Specify the used  delimiter")    
    
    # parse arguments
    args = parser.parse_args()
    
    data = args.filepath
    read_from_file = True
    # input method
    if not data or data == "-":
        read_from_file = False
        data = stdin.read()

    delimiter = args.delimiter or "\t"
    fields = args.fields
    if fields != None:
        try:
            if "," not in fields:
                fields = fields.split()
            else:    
                fields = fields.split(",")
            fields = [int(x) - 1 for x in fields]
            if min(fields) < 0:
                raise ValueError
        except ValueError:
            print("Invalid field request.")
            return 1

    # splitted lines
    splitted_lines = []
    
    # file specified
    if read_from_file:
        # read the file line by line
        with open(args.filepath, "r") as fh:
            for line in fh:
                splitted_lines.append(line.strip().split(delimiter))
    else:
        # no file specified
        splitted_lines = [x.strip().split(delimiter) for x in data.split("\n")]
    
    # no field specified
    if fields == None:
        for line in splitted_lines:
            for field in line:
                print(field, end="\t")
            print()
        return 0
    # print specified fields
    for line in splitted_lines:
        print_new_line = True
        for i in fields:
            try:
                print(line[i], end="\t")
            except Exception:
                print_new_line = False
                continue
        if print_new_line:
            print()
    return 0
if __name__ == "__main__":
    main()
