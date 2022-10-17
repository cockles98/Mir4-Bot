import time
from datetime import datetime
import numpy as np
import pyautogui
import cv2 as cv
import os
from kb_and_mouse import mouse, move, click, holdclick, releaseclick, press



####################################################
# -------------- base functions ------------------ #
####################################################


def wait(delay=2.5):
    r_delay = np.random.uniform(low=delay,high=delay+1)
    time.sleep(r_delay)


def move_click(x,y,delay=2.5,random=False):
    if random == True:
        x = np.random.randint(x,x+20)
        y = np.random.randint(y,y+20)
    r_delay = np.random.uniform(low=delay,high=delay+1.5)
    move(x,y)
    wait(0.75)
    click(mouse.left)
    time.sleep(r_delay)


def move_farm_spot():
    """
    bicheon_area: (740,750)            \\   Death_gorge: (50,380) --> Soul_spot: (965,670)                       
    snake_valley_area: (620,380)       \\   Abandoned_mine: (660,285) --> 2F: (660,130) --> Ant_spot: (770,490)   
    spiritual_center_area: (220,360)   \\                
    """
    wait()
    press(0x79)   # press F10 to open map 
    wait(4)
    move_click(40,25,random=True)   # world_map button   
    move_click(620,380,random=True)   # snake_valley_area position    ---- ajustable
    move_click(660,285,random=True)   # location position    ---- ajustable
    move_click(660,130,random=True)   # floor position if needed    ---- ajustable
    move_click(770,490)   # spot position    ---- ajustable
    wait(0.3)
    click(mouse.left)
    move_click(1400,620,random=True)   # teleport button
    move_click(1000,775,random=True)   # confirm teleport
    wait(120)
    press(0x42)   # press b to start auto combat


def dash_ult():
    press(0xC0)   # press ' (dash button - edited in game)
    wait(0.75)
    press(0x52)  # press r (ult button)


def time_now():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def get_screenshot(array=False):
    my_print = pyautogui.screenshot()
    if array == True:
        return np.array(my_print)
    return my_print


def get_ult_button_sum(image):
    ult_button = image.crop((1680, 810, 1695, 825))
    px_ult_button = np.array(ult_button)
    ult_button_sum = (
    px_ult_button[:, :, 0] & px_ult_button[:, :, 1] & px_ult_button[:, :, 2]
    ).sum()
    return ult_button_sum


def get_life_bar_sum(image):
    life_bar = image.crop((24, 55, 440, 80))
    px_life_bar = np.array(life_bar)
    life_bar_sum = (
        (px_life_bar[:, :, 0] > 120)
        & (px_life_bar[:, :, 1] < 100)
        & (px_life_bar[:, :, 2] < 100)
    ).sum()
    return life_bar_sum


def get_target_sum(image):
    # take pixels from life bar position of 7th furthest monster
    monster_target = image.crop((1310, 312, 1515, 320))
    px_target = np.array(monster_target)
    target_sum = (
        (px_target[:, :, 0] > 120)
        & (px_target[:, :, 1] < 100)
        & (px_target[:, :, 2] < 100)
    ).sum()   # check if there's a 7th furthest monster alive, by the sum of red pixels
    return target_sum


def get_life(life_bar_sum):
    life = round((life_bar_sum / 9800) * 100, 2)

    if 4880 < life_bar_sum < 9690:
        return life + 4.5
    elif life_bar_sum > 9690:
        return 100
    return life - 4.5

    
def number_keyboard(number):
    for i in number:
        if int(i) == 1:
            move_click(715,555,random=True) 
        if int(i) == 2:
            move_click(850,555,random=True)
        if int(i) == 3:
            move_click(982,555,random=True) 
        if int(i) == 4:
            move_click(715,422,random=True)    
        if int(i) == 5:
            move_click(850,422,random=True)
        if int(i) == 6:
            move_click(982,422,random=True)            
        if int(i) == 7:
            move_click(715,289,random=True)     
        if int(i) == 8:
            move_click(850,289,random=True)
        if int(i) == 9:
            move_click(982,289,random=True)        
        if int(i) == 0:
            move_click(850,688,random=True)
    wait()
    move_click(988,915)
    wait()
    
    
def slide_click(x_initial,y_initial,x_final,y_final):
    move(x_initial,y_initial)
    click(mouse.left)
    wait()
    holdclick(mouse.left)    
    wait()
    move(x_initial+10,y_initial)
    move(x_initial+20,y_initial)
    move(x_initial+30,y_initial)
    move(x_initial+40,y_initial)
    wait()
    move(x_final,y_final)
    wait()
    releaseclick(mouse.left)
    wait()
    
    
def choose_clan_tech():
    wait()
    sum = 0
    x,y = 229,24   # bar size
    my_print = get_screenshot()
    
    bar_1 = my_print.crop((435,275,435+x,275+y))
    bar_2 = my_print.crop((435,475,435+x,475+y))
    bar_3 = my_print.crop((435,676,435+x,676+y))
    bar_4 = my_print.crop((435,875,435+x,875+y))
    bar_5 = my_print.crop((940,275,940+x,275+y))
    bar_6 = my_print.crop((940,475,940+x,475+y))
    bar_7 = my_print.crop((940,676,940+x,676+y))
    bar_8 = my_print.crop((940,875,940+x,875+y))
    list = [np.array(bar_1), np.array(bar_2), np.array(bar_3), np.array(bar_4), np.array(bar_5), np.array(bar_6), np.array(bar_7), np.array(bar_8)]
    sum_list = []
    
    for i in list:
        sum = 0
        for j in i[0]:
            if j[1] > 180 and j[2] > 200:
                sum += 1
        sum_list.append(sum)
    
    if sum_list[0] < 190:
        return move(435,275)
    if sum_list[1] < 190:
        return move(435,475)
    if sum_list[2] < 190:
        return move(435,676)
    if sum_list[3] < 190:
        return move(435,875)
    if sum_list[4] < 190:
        return move(940,275)
    if sum_list[5] < 190:
        return move(940,475)
    if sum_list[6] < 190:
        return move(940,676)
    if sum_list[7] < 190:
        return move(940,875)
    

def black_and_white(image):
    px_image = np.array(image)
    for i in px_image:
        for j in i:
            if int(j[0]) < 245 or int(j[1]) < 245 or int(j[2]) < 245:
                j[0],j[1],j[2] = 0,0,0            
    return px_image    

template = cv.imread(r'C:\Users\felip\Desktop\Mir4_python\pico.png', cv.IMREAD_UNCHANGED)
pt_cross = cv.imread(r'C:\Users\felip\Desktop\Mir4_python\pt_cross.png', cv.IMREAD_UNCHANGED)
room_training_1 = cv.imread(r'C:\Users\felip\Desktop\Mir4_python\room_training_1.png', cv.IMREAD_UNCHANGED)
room_training_2 = cv.imread(r'C:\Users\felip\Desktop\Mir4_python\room_training_2.png', cv.IMREAD_UNCHANGED)
store = cv.imread(r'C:\Users\felip\Desktop\Mir4_python\store_bar.png', cv.IMREAD_UNCHANGED)
raid_finished_button = cv.imread(r'C:\Users\felip\Desktop\Mir4_python\raid_finished_ok_button.png', cv.IMREAD_UNCHANGED)
raid_ajust_power = cv.imread(r'C:\Users\felip\Desktop\Mir4_python\ajust_power.png', cv.IMREAD_UNCHANGED)
raid_create_button = cv.imread(r'C:\Users\felip\Desktop\Mir4_python\raid_create_button.png', cv.IMREAD_UNCHANGED)
plus_button = cv.imread(r'C:\Users\felip\Desktop\Mir4_python\plus_button.png', cv.IMREAD_UNCHANGED)

def check_image(image,template,black=False):
    while isinstance(image, int):
        if image == 1:
            image = pt_cross
            break
        if image == 2:
            image = room_training_1
            break
        if image == 3:
            image = room_training_2
            break
        if image == 4:
            image = store
            break
        if image == 5:
            image = raid_finished_button
            break
        if image == 6:
            image = raid_ajust_power
            break
        if image == 7:
            image = raid_create_button
            break
        if image == 8:
            image = plus_button
            break
        if black == True:
            new_image = black_and_white(image)
            new_template = black_and_white(template)
            result = cv.matchTemplate(new_image,new_template, cv.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            return max_val, max_loc            
    result = cv.matchTemplate(image,template, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    return max_val, max_loc

def save_img(img,name='saved_image.png'):
    path = 'C:/Users/felip/Desktop/Mir4_python'
    cv.imwrite(os.path.join(path,name),img)
    
    
def close_all():
    for i in range(7):
        wait(0.5)
        press(0x1B)   # press esc
    
    
    
    
    