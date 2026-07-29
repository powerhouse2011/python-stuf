import ctypes

text ='Using WS_EX_TOPMOST'
title ='Some Title'
ctypes.windll.user32.MessageBoxExW(0,text,title,0x40000)
