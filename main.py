#!/usr/bin/python
# -*- coding:utf-8 -*-

import SH1107
import time
import config
import traceback
import obd
from obd import OBDStatus
from PIL import Image,ImageDraw,ImageFont

try:
    disp = SH1107.SH1107()
    disp.Init()
    
    rpm = 0
    speed = 0
    
    connection = obd.OBD("/dev/ttyUSB0")
    while(1):
        if(connection.status() == OBDStatus.CAR_CONNECTED):
            print ("working on output")
            cmd_speed = obd.commands.SPEED
            response_speed = connection.query(cmd)

            cmd_rpm = obd.commands.SPEED
            response_rpm = connection.query(cmd)
            image1 = Image.new('1', (disp.width, disp.height), "WHITE")
            draw = ImageDraw.Draw(image1)

            font_text = ImageFont.truetype('Font.ttf', 13)
            draw.text((19,0), 'RPM', font = font_text, fill = 0)
            draw.arc((0,17,64,100),0, 360, fill =0 )
            draw.text((18, 43), str(response_rpm.value), font= font_text, fill=0)

            draw.text((76, 0), 'Speed', font = font_text, fill = 0)
            draw.arc((64,17,127,100),0, 360, fill =0 )
            draw.text((89, 43), str(response_speed.value), font = font_text, fill = 0)

            disp.clear()
            image1=image1.rotate(180)
            print("new output")
            disp.ShowImage(disp.getbuffer(image1))
            print("Rmp " + str(rpm) + " Speed" + str(speed))
            time.sleep(0.5)
        else:
            image1 = Image.new('1', (disp.width, disp.height), "WHITE")
            draw = ImageDraw.Draw(image1)

            font_text = ImageFont.truetype('Font.ttf', 13)
            draw.text((1,0), 'CAR NOT CONNECTED', font = font_text, fill = 0)
            draw.arc((0,17,64,100),0, 360, fill =0 )
            draw.text((18, 43), str(rpm), font= font_text, fill=0)

            draw.arc((64,17,127,100),0, 360, fill =0 )
            draw.text((89, 43), str(speed), font = font_text, fill = 0)

            disp.clear()
            image1=image1.rotate(180)
            print("new output")
            disp.ShowImage(disp.getbuffer(image1))
            print("Rmp " + str(rpm) + " Speed" + str(speed))
            time.sleep(0.5)

except IOError as e:
    print(e)

except KeyboardInterrupt:
    print("ctrl + c:")
    config.module_exit()
    exit()
