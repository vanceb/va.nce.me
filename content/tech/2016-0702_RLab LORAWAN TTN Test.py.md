Title: Micropython code for BBC Microbit TTN reporting
Modified: 2016-06-02 15:00
Tags: python, BBC Microbit, IOT, LoRaWAN
Summary: Code modified at the RLab TTN Workshop

~~~ python

# RN2483 LoRaWAN
from microbit import *

def RN2483_Reset(): # Reset RN2483
    uart.init(57600,tx=pin1,rx=pin2 )
    pin0.write_digital(1)
    pin0.write_digital(0)
    pin0.write_digital(1)
    return RN2483_CheckResponse()

def RN2483_SendCommand(command):
    uart.write(command)
    return RN2483_CheckResponse()

def RN2483_CheckResponse():

    for i in range(100):
        sleep(100)
        if uart.any():
            break
    response_string = uart.readline()
    return response_string.strip()

def RN2483_SendData(data):
    uart.write("mac tx uncnf 1 ")
    for char in data:
        nibble = char >> 4
        if nibble > 9:
            nibble = nibble + 0x37
        else:
            nibble = nibble + 0x30
        uart.write(chr(nibble))
        nibble = char & 0x0f
        if nibble > 9:
            nibble = nibble + 0x37
        else:
            nibble = nibble + 0x30
        uart.write(chr(nibble))
    uart.write("\r\n")
    RN2483_CheckResponse()
    RN2483_CheckResponse()

display.show(Image.NO)

RN2483_Reset()
#RN2483_SendCommand("sys factoryRESET\r\n")
RN2483_SendCommand("mac set appeui 70B3D57ED00005D0\r\n")
RN2483_SendCommand("mac set deveui 0004A30B001B2CD5\r\n")
RN2483_SendCommand("mac set appkey 6AAA3F4A721B088385C3E29CB00C7493\r\n")
#RN2483_SendCommand("mac set adr off\r\n")
#RN2483_SendCommand("mac set rx2 3 869525000\r\n")
join_status = RN2483_SendCommand("mac join otaa\r\n")
if join_status == "accepted":
    display.show(Image.YES)
else:
    display.show(Image.NO)

while True:
    response = RN2483_SendData(b"BBC Micro:Bit Data")
    if (response == "mac_tx_ok"):
        display.show(Image.YES)
    else:
        display.show(Image.NO)
    sleep(60000)

~~~
