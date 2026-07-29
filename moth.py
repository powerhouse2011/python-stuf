Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
print (time.localtime())
print (time.strftime("\n%Y%B%D%A %I:%M%p"))
gettime = lambda:  time.strftime("\n%Y%B%D%A %I:%M%p")
if time.strftime("%B") == "December":
    print("It's December! That Means Christmas Soon!")
if time.strftime("%B") == "January":
    print("It's Janurary! That Means Martin L. King Junior Day")
print("{} Days Till Christmas".format(359-int(time.strftime("%j"))))
print("{} Days Till Martin L. King's Brithday".format(15-int(time.strftime("%j"))))
print("{} Days Till Oreo Cookie Day".format(65-int(time.strftime("%j"))))
print("{} Days Till Valentines Day".format(45-int(time.strftime("%j"))))
print("{} Days Till April Foll's Day".format(91-int(time.strftime("%j"))))
































print (time.localtime())