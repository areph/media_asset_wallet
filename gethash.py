# -*- coding: utf-8 -*-
import hashlib

def main():
  data = input('>> ')
  getHash(data)

def getHash(data):
  png_data = open("sample.jpg", "rb").read()
  sha256 = hashlib.sha256(png_data).hexdigest()
  print(sha256)

if __name__ == "__main__":
  main()
