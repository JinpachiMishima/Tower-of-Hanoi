# -*- coding: utf-8 -*-
import logging
logging.basicConfig(filename="logging.log",level=logging.DEBUG,filemode="w")



def main():
    number_of_disks = 5
    first_tower = [0] + [i for i in range(number_of_disks,0,-1)]
    second_tower = [0]
    last_tower = [0]
    towers = [first_tower,second_tower,last_tower]
    logging.debug("Main fuction is started")
    while True:
        getASCIITowers(towers=towers)
        choose_towers = input('выберите башни:')
        
        if checkMove(towers=towers,
                     selected_towers=choose_towers) == False:
            continue
        else:
            logging.debug(f'{choose_towers} is correct')
            makeMove(towers=towers,
                     selected_towers=choose_towers)


#   TODO
# Необходимо сделать функцию, которая будет брать знание  из
# донорского массива и добавлять его в в акцепторский, пред-
# варительно удалив из донорского

def makeMove(towers,selected_towers):
    pass    


#   TODO
# Необходимо сделать функцию, который будет принимать на вход
# два значения донорской башни и  акцепторской башни и прове-
# рять возможность переноса диска 

def checkMove(towers,selected_towers):
    
    if selected_towers[0] not in ['1','2','3'] and selected_towers[-1] not in ['1','2','3']:
        # это условие нужно  FIXME сократить
        logging.debug('Insert choose is not correct')
        return False
    
    donor_tower = int(selected_towers[0]) - 1
    acceptor_tower = int(selected_towers[-1]) - 1
    
    if len(towers[donor_tower]) == 0:
        logging.debug('donor is a zero')
        return False
    if len(towers[donor_tower]) != 0 and len(towers[acceptor_tower]) == 0:
        logging.debug('donor is not zero and acceptor is a zero')
        return True
    if towers[donor_tower][-1] > towers[acceptor_tower][-1]:
        return False
    if towers[donor_tower][-1] < towers[acceptor_tower][-1]:
        logging.debug('donor is larger than the acceptor')
        return True
    
    

#   TODO
# Необходимо сделать функцию, который будет принимать на вход
# три массива и выдавать строку с тремя башнями в ASCII стиле

def getASCIITowers(towers):
    print(towers)

main()
