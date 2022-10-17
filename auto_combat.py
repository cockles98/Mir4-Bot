from kb_and_mouse import press
from base_functions_mir4 import wait, get_screenshot, time_now, get_ult_button_sum, get_life_bar_sum, get_life, dash_ult
from repeatable_tasks_mir4 import break_seal, combine, sell_equip, clan_obligations
from daily_tasks_mir4 import all_daily_obligations_1, all_daily_obligations_2
from base_functions_mir4 import save_img
import numpy as np
import telegram_send
import cv2 as cv

#######################################################
# ------------------ auto play ---------------------- #
#######################################################

        
def auto_play(max_life_difference=8.5, min_life=40, waiting_time=2):
    wait()
    last_life = 75   # just to start the function
    obligations_1 = 0
    obligations_2 = 0
    repeatable_tasks_hour = 24
    saved_print = 0

    while True:
        ult_available = False           
        my_print = get_screenshot()
        ult_button_sum = get_ult_button_sum(my_print)
        ult_available = ult_button_sum < 4000
        life_bar_sum = get_life_bar_sum(my_print)
        life = get_life(life_bar_sum)
        
        now = time_now()
        hour = int(now[0:2])
        minutes = int(now[3:5])
        seconds = int(now[6:8])

        if life <= 0:   # check if there's another screen above
            save_img(np.array(my_print),'another_screen.png')
            telegram_send.send(messages=["Another screen!"])
            wait()
            with open(r'C:\Users\felip\Desktop\Mir4_python\another_screen.png', "rb") as f:
                telegram_send.send(images=[f])
            wait(300)
            continue
        
        if not ult_available and life <= 35:   # low life combo without ult
            last_life = life
            print(f"low life and no ult, {now}")
            press(0x32)   # press 2 to furtive mode
            wait(90)
            press(0x42)   # press b to start auto combat
            continue

        if ult_available:
            life_difference = round(life - last_life, 2)
            if -75 <= life_difference <= -max_life_difference:
                last_life = life
                print(f"Perdeu muita vida, {life=}%, {life_difference=}%, {now}")
                dash_ult()   
                continue
            if life <= min_life:
                last_life = life
                print(f"Vida baixa, {life=}%, {life_difference=}%, {now}")
                dash_ult()
                continue
        last_life = life
            
        if abs(repeatable_tasks_hour - hour) == 8 or abs(repeatable_tasks_hour - hour) == 16:
            repeatable_tasks_hour = hour
            clan_obligations()
            break_seal()
            combine()
            sell_equip()
            
        if obligations_1 == 1 and hour == 13 and minutes >= 10:
            obligations_1 = 0
            
        if obligations_1 == 0:
            obligations_1 += 1
            all_daily_obligations_1()
            
        if obligations_2 == 1 and hour == 1:
            obligations_2 = 0
            
        if obligations_2 == 0:
            obligations_2 += 1
            all_daily_obligations_2()
             
        wait(waiting_time)    
        
        
    