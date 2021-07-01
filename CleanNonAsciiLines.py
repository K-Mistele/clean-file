import argparse
import io

# CHECK IF A STRING IS IN ASCII
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

# RUN AND PARSE ARGUMENTS
def main():
    parser = argparse.ArgumentParser(description='A simple tool to read files one line at a time, and remove lines that have non-ascii characters')
    parser.add_argument('--in', required=True, dest='in_file', help='Specify the input text file - if you want to clean an excel file export to CSV first.')
    parser.add_argument('--out', required=True, dest='out_file', help='Specify the output text file')
    args = vars(parser.parse_args())

    print(f'[+] Reading in {args["in_file"]}')
    lines = []
    with io.open(args["in_file"],'r',encoding='utf-8',errors='ignore') as infile, \
        io.open(args["out_file"],'w',encoding='ascii',errors='ignore') as outfile:
        print(f'[+] Converting lines to ascii')
        for line in infile:
            if not is_ascii(line):
                print('Skipping a line!')
                continue
            print(*line.split(), file=outfile)
    print(f'[+] Conversion finished; results written to {args["out_file"]}')

if __name__ == '__main__':
    main()