#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("quadrado", help="Quadrado de um número", type=int)
args = parser.parse_args()

print(args.quadrado**2)
