# -*- coding: utf-8 -*-
import hashlib

def getHash(data):
  png_data = open(data, "rb").read()
  sha256 = hashlib.sha256(png_data).hexdigest()
  return sha256

