import subprocess
import time
import pyautogui as pg

subprocess.Popen('/usr/bin/firefox')

time.sleep(2)

pg.write('soft98.ir')
pg.press('enter')
pg.moveTo(395,146, duration=5)
pg.click()

pg.moveTo(891, 282, duration=3)
pg.click()
pg.write('sahandp2012')


pg.moveTo(914, 376, duration=1)
pg.click()
pg.write('thisisatest1234')

pg.moveTo(965, 425)
pg.click()
