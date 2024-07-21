import argparse

def main():
    # create parser
    parser = argparse.ArgumentParser(description="My version of cut program")
    
    # add arguments
    parser.add_argument("filepath", help="Path to the file")
    parser.add_argument("-f", "--fields", type=str, help="Specify return fields")
    parser.add_argument("-d", "--delimiter", type=str, help="Specify the used  delimiter")    
    
    # parse arguments
    args = parser.parse_args()

    delimiters = args.delimiter or "\t"
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

    # read the file line by line
    with open(args.filepath, "r") as fh:
        for line in fh:
            splitted_lines.append(line.strip().split(delimiters))
    
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
