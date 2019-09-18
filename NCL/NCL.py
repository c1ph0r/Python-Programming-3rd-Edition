#!/usr/bin/env python

import sys

def verify(guess):
  vals = [
		130,
		154,
		136,
		252,
		131,
		157,
		155,
		137,
		252,
		231,
		231,
		225,
		226
  ]

  if len(guess) != 13:
    return False

  for i, c in enumerate(guess):
    if (ord(c) ^ 209) != vals[i]:
      return False
  return True


if len(sys.argv) != 1:
  print('Usage: python check.pyc')
  exit(1)

guess = input("Enter your guess for the flag: ");

if verify(guess):
  print("That's the correct flag!")
else:
  print("Wrong flag.")