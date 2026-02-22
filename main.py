import argparse
from analyzer import analyzer

def main():
    parser = argparse.ArgumentParser(description="Tool for analizer url suspicious")
    parser.add_argument("url",help="Your url suspicious")
    parser.add_argument("-H",help="look HTML of the page",action="store_true")

    args = parser.parse_args()

    analyzer(args.url,args.H)

main()