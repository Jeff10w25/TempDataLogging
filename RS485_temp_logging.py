import serial
import time
import minimalmodbus
import openpyxl as xl

#RS485 
device_address = 1
di_dev_1 = minimalmodbus.Instrument('/dev/ttyUSB0', device_address)
di_dev_1.serial.baudrate = 57600                #baud
di_dev_1.serial.bytesize = 8
di_dev_1.serial.parity = serial.PARITY_NONE
di_dev_1.serial.stopbits = 1
di_dev_1.serial.timeout = 0.05                  #seconds
di_dev_1.close_port_after_each_call = True

#Excel
time_column = 1
temp_column = 2
time_row = 2
temp_row = 2
file = xl.Workbook()
namesheet = file.worksheets[0]
namesheet['A1'] = 'Date and Time'
namesheet['B1'] = 'Temperature (C)'
namesheet.column_dimensions['A'].width = 25
namesheet.column_dimensions['B'].width = 15
file.save('Temperature_logging.xlsx')

while 1:
    data_ch_1_1 = di_dev_1.read_register(0,1)
    seconds = time.time()
    local_time = time.ctime(seconds)
    namesheet.cell(time_row,time_column).value = str(local_time)
    namesheet.cell(temp_row,temp_column).value = str(data_ch_1_1)
    time_row += 1
    temp_row += 1
    file.save('Temperature_logging.xlsx')

    print(str(local_time) + ", " + "Ch1 of 1st: " + str(data_ch_1_1) + " C")

    time.sleep(60) #Period of data collection

