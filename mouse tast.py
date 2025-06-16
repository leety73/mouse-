import pyautogui as pg
import time

"""
# 마우스의 위치를 2초 있다가 출력 x, y
time.sleep(2)
print(pg.position())
"""


#마우스의 이동
"""
pg.moveTo(100, 200) # x 100, y 200 위치로 바로 이동
time.sleep(1)
pg.moveTo(600, 800, 2) # x 100, y 200 위치로 2초동안 이동
"""

pg.click()
pg.click(button='right')
pg.doubleClick()
pg.click(clicks=3, interval=1) # 3번 클릭할건데 1초마다
