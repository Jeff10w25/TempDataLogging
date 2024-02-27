import serial
import time
import minimalmodbus
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook
from os.path import expanduser as ospath

#RS485 parameters
device_address = 1
di_dev_1 = minimalmodbus.Instrument('/dev/ttyUSB0', device_address)
di_dev_1.serial.baudrate = 57600                #baud
di_dev_1.serial.bytesize = 8
di_dev_1.serial.parity = serial.PARITY_NONE
di_dev_1.serial.stopbits = 1
di_dev_1.serial.timeout = 0.05                  #seconds
di_dev_1.close_port_after_each_call = True
i=1

def ExcelData(file_path,data,sheet):
    writer = pd.ExcelWriter(file_path, engine='openpyxl')
    writer.book = load_workbook(file_path)
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    reader = pd.read_excel(file_path, index_col=None, na_values=['NA'], usecols="A:C")
    data.to_excel(writer, index=False ,header=False, startrow=len(reader)+1 ,sheet_name=sheet)
    writer.close()

while (i<100):
    #Parameters
    data_ch_1_1 = di_dev_1.read_register(0,1)
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    #Excel input of channel 1_1
    excel_path = ospath('~/TempDataLogging/excel/Temperature_logging.xlsx')
    data = pd.DataFrame({"Date":[current_date], "Time":[current_time], "Temperature (C)":[data_ch_1_1]})

    ExcelData(excel_path,data,"Sheet1")

    #Display date and temperature data
    print(str(current_date) + " " + str(current_time) + ", " + "Ch1 of 1st: " + str(data_ch_1_1) + " C")
    time.sleep(10) #Period of data logging
    i+=1

