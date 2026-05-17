import argparse
from analyzer import analyzer

def main():
    parser = argparse.ArgumentParser(description="Tool for analizer url suspicious (educative)")
    parser.add_argument("url",help="Your url suspicious")
    parser.add_argument("-H",help="Look HTML of the page",action="store_true")
    parser.add_argument("-ss",help="Validate ssl certificate",action="store_true")
    parser.add_argument("-r",help="An educational report",action="store_true")

    args = parser.parse_args()

    analyzer(args.url,args.H,args.ss,args.r)


main()