import time
import cv2 as cv
from base_functions_mir4 import wait, move_click, number_keyboard, get_screenshot, check_image, move_farm_spot, close_all
from kb_and_mouse import mouse, move, click, press



#############################################################
# ------------------ small functions ---------------------- # 
#############################################################
 
 
def daily_identify():
    wait()
    press(0x78)   # press F9 to open menu 
    wait()
    move_click(1389,313,random=True)   # forge button on menu   
    move_click(1520,470,random=True)   # indentify button    
    wait()
    move_click(1460,235,random=True)   # third_weapon position    
    move_click(1520,980,random=True)   # enchant button    
    move_click(720,980,random=True)   # identify button   
    move_click(1520,980,random=True)   # apply button
    press(0x1B)   # press esc
    wait() 
    
    
def daily_creation():
    move_click(1525,313,random=True)   # create_button button on menu
    move_click(1380,475,random=True)   # create_button_2 button   
    wait()
    move_click(530,35,random=True)   # create_material button    
    move_click(460,410,random=True)   # great_yang_pill position
    move_click(1630,1000,random=True)   # apply button
    wait()
    press(0x1B)   # press esc
    wait()
    press(0x1B)   # press esc
    wait()    
    
    
def daily_mining():
    wait()
    press(0x79)   # press F10 to open map 
    wait(4)
    move_click(40,25,random=True)   # world_map button   
    move_click(620,380,random=True)   # snake_valley_area position    
    move_click(930,590,random=True)   # snake_valley position    
    move_click(1340,310,random=True)   # close npc_spot list    
    move_click(1340,595,random=True)   # open mining_spot list    
    move_click(1340,685,random=True)   # mining_spot button    
    move_click(1370,1000,random=True)   # teleport button
    wait(10)
    press(0x4E)   # press n to start auto mining
    wait(250)  
    
    
def daily_gather():
    wait()
    press(0x79)   # press F10 to open map 
    wait(4)
    move_click(40,25,random=True)   # world_map button    
    move_click(620,380,random=True)   # snake_valley_area position    
    move_click(930,590,random=True)   # snake_valley position    
    move_click(1340,310,random=True)   # close npc_spot list
    move_click(1340,595,random=True)   # open mining_spot list    
    move_click(1340,830,random=True)   # gather_spot button    
    move_click(1370,1000,random=True)   # teleport button
    wait(10)
    press(0x4E)   # press n to start auto mining
    wait(250)  
    
    
def daily_meditate():
    wait()
    press(0x79)   # press F10 to open map 
    wait(4)
    move_click(40,25,random=True)   # world_map button    
    move_click(620,380,random=True)   # snake_valley_area position    
    move_click(1450,850,random=True)   # viperbeast position    
    move_click(1350,600,random=True)   # close monster_spot list
    move_click(1340,500,random=True)   # open mining_spot list    
    move_click(1340,890,random=True)   # meditate_spot button    
    move_click(1370,1000,random=True)   # teleport button
    wait(10)
    press(0x4E)   # press n to start auto mining
    wait(150)
    
    
def daily_obligations():
    wait()
    daily_identify()
    wait()
    daily_creation()
    wait()
    daily_mining()
    wait()
    daily_gather()
    wait()
    daily_meditate()
    wait()
    press(0x78)   # press F9 to open menu
    wait()
    move_click(1810,490,random=True)   # tasks button
    move_click(1385,655,random=True)   # daily_tasks button
    wait()
    move_click(1650,230,random=True)   # get_all button
    wait(5)
    click(mouse.left)
    wait()
    move_click(920,230,random=True)   # reward 1 position
    wait(10)
    move_click(1450,230,random=True)   # reward 2 position
    wait(10)
    press(0x1B)   # press esc
    wait()
    press(0x1B)   # press esc
    wait()
    move_farm_spot()   # back to farm spot
    wait()
    
 
    
######################################################### 
# ------------------ daily tasks ---------------------- # 
#########################################################    


def magic_square():
    """
    1F: (50,150)   \\   Training_Chamber_I: 2
    2F: (50,380)   \\   Training_Chamber_II: 3
    3F: (50,580)   \\   
    4F: (50,800)   \\   
    """
    wait()
    press(0x78)   # press F9 to open menu 
    wait()
    move_click(1390,670,random=True)   # portal button on menu
    move_click(1390,830,random=True)   # magic_square button   
    move_click(50,580,random=True)   # floor position button    ---- ajustable
    move_click(1300,1000,random=True)   # enter button
    wait(10)
    press(0x77)   # press F8 to open notification
    wait()
    move(1760,140)
    for i in range(8):   # close all notifications 
        time.sleep(0.5)
        click(mouse.left)
    press(0x1B)   # press esc
    move_click(210,139,random=True)   # vigor button
    move_click(540,800,random=True)   # recharge button
    move_click(1020,790,random=True)   # recharge button 2
    move_click(210,139,random=True)   # vigor button
    move_click(540,800,random=True)   # recharge button
    move_click(980,370,random=True)   # 30 min pill position
    move_click(1020,790,random=True)   # recharge button 2
    x,y = check_image(8,get_screenshot(array=True))[1]   
    move_click(x+15,y+15)   # plus button
    move_click(1050,280,random=True)   # auto_extend_time layer
    move_click(1050,450,random=True)   # add_ticket button
    wait()
    click(mouse.left)   # add 1 more ticket
    wait()
    move_click(850,860,random=True)   # confirm button
    move_click(1290,165,random=True)   # close window
    move_click(1845,305)   # move to teleport position
    wait(10)
    while True:
        the_print = get_screenshot(array=True)
        if check_image(3,the_print)[0] >= 0.9:   # choosen room    ---- ajustable
            break
        click(mouse.left)
        wait(10)
        continue
    press(0x42)   # press b to start auto combat
    time.sleep(5400)
    press(0x1B)   # press esc
    wait()
    press(0x42)   # press b to start auto combat
    wait()  
    

def pico():
    """
    1F: (50,150)   \\   
    2F: (50,380)   -->   (650,660)
    3F: (50,580)   -->   (815,490)
    4F: (50,800)   \\   
    """
    wait()
    press(0x78)   # press F9 to open menu 
    wait()
    move_click(1390,670,random=True)   # portal button on menu
    move_click(1530,830,random=True)   # pico button   
    move_click(50,580,random=True)   # floor position button    ---- ajustable 
    move_click(1300,1000,random=True)   # enter button
    wait(10)
    move_click(210,139,random=True)   # vigor button
    move_click(540,800,random=True)   # recharge button
    move_click(1020,790,random=True)   # recharge button 2
    press(0x79)   # press F10 to open map 
    wait(4)
    move_click(815,490)   # spot position    ---- ajustable
    wait()
    click(mouse.left)
    wait(50)
    press(0x42)   # press b to start auto combat
    x,y = check_image(8,get_screenshot(array=True))[1]   
    move_click(x+15,y+15)   # plus button
    move_click(1050,280,random=True)   # auto_extend_time layer
    move_click(1050,450,random=True)   # add_ticket button
    move_click(850,860,random=True)   # confirm button
    move_click(1290,165,random=True)   # close window
    wait(3600) 
    press(0x1B)   # press esc 
    wait()
    press(0x42)   # press b to start auto combat
    wait()


def daily_store(summons=False):
    wait()
    press(0x73)   # press F4 to open store
    wait(4)
    while True:   # check if there's some advertising screen
        the_print = get_screenshot(array=True)
        if check_image(4,the_print)[0] >= 0.62:
            wait()
            press(0x1B)   # press esc
            wait()
            continue
        break
    wait()
    move_click(40,640,random=True)   # intensify layer
    for i in range(3):
        move_click(320,990,random=True)   # daily_scroll position
        move_click(1000,880,random=True)   # buy button
    if summons:
        pass
    press(0x1B)   # press esc
    wait()  


def normal_raid():
    """
    Demon Ruin: (50,150) - power: 50000
    Mine: (50,300) - power: 62000
    Tatoo: (50,510) - power: 72000
    Greed: (50,750) - power: 82000
    Sinner: (50,950) - power: 92000
    """
    wait()
    press(0x78)   # press F9 to open menu 
    wait()
    move_click(1525,660,random=True)   # raids button on menu
    move_click(1385,825,random=True)   # normal_raid button  
    wait()
    move_click(50,1000,random=True)   # ajust raids list position
    move_click(50,300,random=True)   # choose raid    ---- ajustable
    move_click(1500,980,random=True)   # create_raid button  
    x,y = check_image(6,get_screenshot(array=True))[1]   
    move_click(x+200,y+20,random=True)   # power_ajust button
    number_keyboard('62000')   # select power    ---- ajustable
    wait()
    click(mouse.left)
    wait()
    press(0x1B)   # press esc
    wait()
    while True:   # check when raids over
        wait(60)
        the_print_normal = get_screenshot(array=True)
        raid_finished = cv.imread(r'C:\Users\felip\Desktop\Mir4_python\raid_finished.png', cv.IMREAD_UNCHANGED)
        if check_image(the_print_normal,raid_finished)[0] >= 0.5:
            move_click(1320,960,random=True) 
            wait(20)
            break
        continue
    press(0x42)   # press b to start auto combat
    
 
def boss_raid():
    """
    Monk: (50,150) - power: 25000
    Bull: (50,380) - power: 45000
    Sagittarius: (50,590) - power: 65000
    Centipede: (50,850) - power: 75000
    Spectre: (50,1000) - power: 90000
    """
    wait()
    press(0x78)   # press F9 to open menu 
    wait()
    move_click(1525,660,random=True)   # raids button on menu
    move_click(1510,825,random=True)   # boss_raid button
    wait()
    move_click(50,360,random=True)   # choose raid    ---- ajustable
    move_click(1500,980,random=True)   # create_raid button
    x,y = check_image(6,get_screenshot(array=True))[1]   
    move_click(x+200,y+20,random=True)   # power_ajust button
    number_keyboard('45000')   # select power    ---- ajustable
    wait()
    click(mouse.left)
    wait()
    press(0x1B)   # press esc
    wait()
    while True:   # check when raids over
        wait(60)
        the_print_normal = get_screenshot(array=True)
        raid_finished = cv.imread(r'C:\Users\felip\Desktop\Mir4_python\raid_finished.png', cv.IMREAD_UNCHANGED)
        if check_image(the_print_normal,raid_finished)[0] >= 0.5:
            move_click(1320,960,random=True)            
            wait(20)
            break
        continue
    press(0x42)   # press b to start auto combat
    
    
def donate_and_mail(ds=False):
    wait()
    press(0x74)   # press F5 to open clan
    wait(4)
    move_click(1330,880,random=True)   # storage button
    move_click(900,1000,random=True)   # donate button
    move_click(1290,710,random=True)   # max button
    move_click(1250,880,random=True)   # donate_2 button
    move_click(1075,680,random=True)   # donate_3 button
    move_click(550,580,random=True)   # energy button
    move_click(1290,710,random=True)   # max button
    move_click(1250,880,random=True)   # donate_2 button
    move_click(1075,680,random=True)   # donate_3 button
    if ds:
        move_click(550,430,random=True)   # dark_steel button
        move_click(1290,710,random=True)   # max button
        move_click(1250,880,random=True)   # donate_2 button
        move_click(1075,680,random=True)   # donate_3 button
    wait()
    press(0x1B)   # press esc
    wait()
    press(0x1B)   # press esc
    wait()
    press(0x1B)   # press esc
    wait()
    press(0x71)   # press F2 to open mail
    wait()
    move_click(1700,160,random=True)   # read_all button
    click(mouse.left)   # click again
    wait()
    move_click(50,250,random=True)   # system layer
    move_click(1700,160,random=True)   # read_all button
    click(mouse.left)   # click again
    wait()
    move_click(50,360,random=True)   # clan layer
    move_click(1700,160,random=True)   # read_all button
    click(mouse.left)   # click again
    wait()
    press(0x1B)   # press esc
    
 
    
############################################################# 
# ------------------ all daily tasks ---------------------- #
############################################################# 


def all_daily_obligations_1():
    wait(10)
    close_all()
    daily_store()
    close_all()
    donate_and_mail()
    close_all()
    #boss_raid()
    #close_all()
    #normal_raid()
    #close_all()
    pico()
    close_all()
    #normal_raid()
    #close_all()

    
def all_daily_obligations_2():
    wait(10)
    close_all()
    magic_square()
    close_all()
    daily_obligations()
    close_all()
    normal_raid()
    close_all()
    boss_raid()
    close_all()