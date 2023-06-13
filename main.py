#!/usr/bin/python
# -*- coding:utf-8 -*-

import SH1107
import time
import config
import traceback

from PIL import Image,ImageDraw,ImageFont

try:
    disp = SH1107.SH1107()

    print("1.3inch OLED ")
    disp.Init()
    rmp = 0
    speed = 1
    while(1):
        print ("working on output")
        image1 = Image.new('1', (disp.width, disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)

        font_text = ImageFont.truetype('Font.ttf', 13)
        draw.text((19,0), 'RMP', font = font_text, fill = 0)
        draw.arc((0,17,64,100),0, 360, fill =0 )
        draw.text((18, 43), str(rmp), font= font_text, fill=0)

        draw.text((76, 0), 'Speed', font = font_text, fill = 0)
        draw.arc((64,17,127,100),0, 360, fill =0 )
        draw.text((89, 43), str(speed), font = font_text, fill = 0)

        disp.clear()
        #image1=image1.rotate(180)
        print("new output")
        disp.ShowImage(disp.getbuffer(image1))
        rmp+=100
        speed+=3
        print("Test rmp " + str(rmp) + " Test speed" + str(speed))
        time.sleep(0.5)

except IOError as e:
    print(e)

except KeyboardInterrupt:
    print("ctrl + c:")
    config.module_exit()
    exit()
