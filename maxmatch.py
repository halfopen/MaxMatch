# encode:utf-8

import argparse


class MaxMatch:
    """

    """

    def __init__(self):
        pass

    def read_corpus(self):
        pass

    def match(self):
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c",   default="./data/corpus",
                        dest="corpus",
                        help="corpus file path")
    parser.add_argument("text")
    parser.add_argument("-o", dest="output_path", help="output file path")
    args = parser.parse_args()

    print(args)

