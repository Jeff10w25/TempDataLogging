import serial
import time
import minimalmodbus
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook

#RS485 
device_address = 1
di_dev_1 = minimalmodbus.Instrument('/dev/ttyUSB0', device_address)
di_dev_1.serial.baudrate = 57600                #baud
di_dev_1.serial.bytesize = 8
di_dev_1.serial.parity = serial.PARITY_NONE
di_dev_1.serial.stopbits = 1
di_dev_1.serial.timeout = 0.05                  #seconds
di_dev_1.close_port_after_each_call = True
i=1

#Excel
while (i<10):
    data_ch_1_1 = di_dev_1.read_register(0,1)
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%Y-%m-%d")
    
   #Excel input of channel 1
    df = pd.DataFrame({"Date":[current_date], "Time":[current_time], "Temperature (C)":[data_ch_1_1]})
    writer = pd.ExcelWriter("Temperature_logging.xlsx", engine='openpyxl')
    writer.book = load_workbook("Temperature_logging.xlsx")
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    reader = pd.read_excel(r'Temperature_logging.xlsx')
    df.to_excel(writer, index=False ,header=False, startrow=len(reader)+1 ,sheet_name="Sheet1")
    writer.close()

    print(str(current_date) + " " + str(current_time) + ", " + "Ch1 of 1st: " + str(data_ch_1_1) + " C")
    time.sleep(1) #Period of data logging
    i+=1

