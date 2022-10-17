import time
from base_functions_mir4 import wait, move_click, slide_click, choose_clan_tech, number_keyboard
from kb_and_mouse import mouse, move, click, press
    


##############################################################
# ------------------ repeatable tasks ---------------------- # 
##############################################################    


def break_seal():
    wait()
    press(0x78)   # press F9 to open menu 
    wait()
    move_click(1525,313,random=True)   # create_button button on menu
    move_click(1680,475,random=True)   # break_seal button   
    wait()
    move_click(900,150,random=True)   # get_all button   
    wait(5)
    click(mouse.left)
    wait()
    move(1200,300)
    for i in range(8):
        wait(0.5)
        click(mouse.left)
    press(0x1B)   # press esc
    wait()
    press(0x1B)   # press esc
    

def combine():
    pass


def sell_equip():
    pass


def buy_potions():
    'need to finish'
    def ajust_position():
        pass    
    time.sleep(4)  # wait to start
    press(0x79)   # press F10 to open map 
    time.sleep(2)
    move_click(40,25,random=True)   # world_map button   
    move_click(620,380,random=True)   # snake_valley_area position    
    move_click(930,590,random=True)   # snake_valley position    
    move_click(1340,480,random=True)   # pot_npc position    
    move_click(1370,1000,random=True)   # teleport button
    time.sleep(10)
    move_click(855,480)   # start chat npc
    #ajust_position()   # ajust potions position
    time.sleep(2)
    move_click(1650,930,random=True)   # great mana potion position
    move_click(1260,570,random=True)   # set amount
    number_keyboard('3000')
    move_click(1050,730,random=True)   # buy button
    move_click(1650,250,random=True)   # medium health potion position
    move_click(1260,570,random=True)   # set amount
    number_keyboard('100')
    move_click(1050,730,random=True)   # buy button
    time.sleep(2)
    press(0x1B)   # press esc
    time.sleep(2)



##################################################
# ------------------ clan ---------------------- # 
##################################################
    

def support():
    move_click(1120,630,random=True)   # support button
    wait(4)
    move_click(1640,980,random=True)   # support button 2
    press(0x1B)   # press esc to back to clan menu
    wait() 
    
def tech():
    move_click(1530,630,random=True)   # tech button
    wait(4)
    move_click(40,230,random=True)   # clan_skills button 
    slide_click(600,350,1200,350)   # ajust skills position
    choose_clan_tech()   # choose skill position
    wait()
    click(mouse.left)
    wait()
    move(1000,970)
    wait()
    for i in range(26):   # click more then 24x
        click(mouse.left) 
        time.sleep(0.75)   
    press(0x1B)   # press esc
    wait()
    press(0x1B)   # press esc
    wait()
    press(0x1B)   # press esc to back to clan menu
    wait()
    
def resource():
    move_click(1330,630,random=True)   # resource button
    wait(4)
    move_click(1700,1000,random=True)   # general_report button
    move_click(30,240,random=True)   # clan_gift button
    move_click(1710,1000,random=True)   # get_all button
    wait(15)
    click(mouse.left)
    wait(2)
    click(mouse.left)
    wait()
    move_click(500,980,random=True)   # gift button
    wait(10)
    click(mouse.left)
    wait()
    press(0x1B)   # press esc
    wait()
    press(0x1B)   # press esc
    wait()
    press(0x1B)   # press esc
    wait()
    
def clan_obligations():
    wait()
    press(0x74)   # press F5 to open clan
    wait(4)
    support()
    wait()
    #tech()
    #wait()
    resource()
    wait()
    press(0x1B)   # press esc to quit clan screen
    wait()