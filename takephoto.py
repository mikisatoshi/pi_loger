# -*- coding: utf-8 -*-
import json, time, datetime
import picamera


class PiLoger():
  def __init__(self):
    pass

  def get_dummy_data(self):
    pass

def main():
  with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('/../strage/photo/'+str(datetime.datetime.now())+'my_picture.jpg')


if __name__ == '__main__':
  main()