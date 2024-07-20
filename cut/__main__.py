import argparse

def main():
    # create parser
    parser = argparse.ArgumentParser(description="my version of cut program")
    
    # add arguments
    parser.add_argument("filepath", help="path to the file")
    parser.add_argument("-f", "--fields", type=str, help="specify return fields")
    
    # parse arguments
    args = parser.parse_args()

    delimiters = ["\t"]
    fields = args.fields
    if fields != None:
        fields = fields.split(",")
        try:
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
            splitted_lines.append(line.strip().split(*delimiters))
    
    # no field specified
    if fields == None:
        for line in splitted_lines:
            for field in line:
                print(field, end="\t")
            print()
        return 0
    # print specified fields
    for line in splitted_lines:
        for i in fields:
            try:
                print(line[i], end="\t")
            except IndexError:
                continue
        print()
    return 0
if __name__ == "__main__":
    main()
