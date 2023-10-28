import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of time to meow", type=int)
args = parser.parse_args() #Inside args we have all the command arguments

for _ in range(args.n):
	print("meow")
#Run with python meows5_argparse.py -h to check all arguments
