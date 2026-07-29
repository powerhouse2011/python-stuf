import ctypes


text ='error opening nani'
title ='nani'
def box():
    ctypes.windll.user32.MessageBoxExW(0,text,title,0x40000)
