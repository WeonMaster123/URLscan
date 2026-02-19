import argparse
from analyzer import analyzer

def main():
    parser = argparse.ArgumentParser(description="Tool for analizer url suspicious")
    parser.add_argument("url",help="Your url suspicious")

    args = parser.parse_args()

    analyzer(args.url)

main()