# -*- coding: utf-8 -*-
import json
import numpy as np
import access as acc
import pandas as pd
import datetime
from math import sin

class PiLoger():
  def __init__(self, ch = 8):
    self.ch = ch

  def get_dummy_data(self):
    dt_now = datetime.datetime.now()
    value = dt_now.hour * 60 + dt_now.minute
    values = ["-",str(datetime.datetime.now()), value, sin(value/100), 9999, 9999 ,0 ,0, 0, 0, "test"]
    return values

  def get_data(self):
    pass

def main():
  try:
    with open("./../certification/unique_name.json") as f:
      para = json.load(f)
  except:
    with open("./certification/unique_name.json") as f:
      para = json.load(f)
  print(para)
  PA = acc.PiAccess(para["bookname"],para["sheetname"],para["keyname"])

  PL = PiLoger(ch = 8)
  PA.append(PL.get_dummy_data())


if __name__ == '__main__':
  main()