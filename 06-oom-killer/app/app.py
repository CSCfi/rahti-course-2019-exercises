#!/usr/bin/env python3

# Reserve memory until OOM killer hits

import time

def main(N=100):
  a = []
  for i in range(0,N):
    a.append(bytearray(10000000)) # add 10MB to array
    print("{0}0MB".format(i+1), flush=True)
    time.sleep(2)


if __name__ == "__main__":
  main()
