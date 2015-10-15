#!/usr/bin/env python3

import argparse
import subprocess
import clipboard
import os

# Configuration Variables
HOST = "example.com"
USER = "www"
DIR = "/var/www/uploads/"
URL_PREFIX = "http://example.com/uploads/"

def upload_file(filename, destname=None):
    dest_str = USER + '@' + HOST + ':' + DIR
    if destname is not None:
        dest_str += destname
        
    subprocess.Popen(["scp", filename, dest_str]).wait()

def main():
    # parse args
    parser = argparse.ArgumentParser(description='Quick upload a file.')
    parser.add_argument('file_name', metavar='File', type=str,
                help='File to upload')
    parser.add_argument('-n', dest='dest_name', metavar='Filename', type=str,
                help='Destination filename', default=None)
    parser.add_argument('-c', dest='copy', action='store_true',
                help="Copy the URL to the clipboard")
    parser.set_defaults(copy=False)
    args = parser.parse_args()

    # does file exist?
    if not os.path.isfile(args.file_name):
        return print("Error: File does not exist")
    # upload the file
    upload_file(args.file_name, args.dest_name)

    if args.dest_name is not None:
        result = URL_PREFIX + args.dest_name
    else:
        result = URL_PREFIX + os.path.basename(args.file_name)
    

    if args.copy:
        clipboard.copy(result)
        print('Copied to clipboard!')

    print(result)



if __name__ == '__main__':
    main()


