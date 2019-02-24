import argparse
import glob

parser = argparse.ArgumentParser()

parser.add_argument('directory')
parser.add_argument('-name')
parser.add_argument('-type')
parser.add_argument('-prnt', action='store_true')

args = parser.parse_args()

#print(args)

if args.prnt:

    for result in glob.glob(args.directory + '/' + args.name,
	            recursive=True):
	    print(result)
