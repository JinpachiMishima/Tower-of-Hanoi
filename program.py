import logging
import os
logging.basicConfig(filename="logging.log",level=logging.DEBUG,filemode="w")



def main():
    number_of_disks = 5
    first_tower = [i for i in range(number_of_disks,0,-1)]
    second_tower = []
    last_tower = []
    towers = [first_tower,second_tower,last_tower]
    logging.debug("Main fuction is started")
    while True:
        getASCIITowers(towers=towers,number_of_disks=number_of_disks)
        choose_towers = input('выберите башни:')
        
        if checkMove(towers=towers,
                     selected_towers=choose_towers) == False:
            logging.debug(f'{choose_towers} is not correct')
            continue
        else:
            logging.debug(f'{choose_towers} is correct')
            makeMove(towers=towers,
                     selected_towers=choose_towers)


# Функция сохраняет удаленный из донора элемент 
# и добавляет его в акцептор
def makeMove(towers,selected_towers):
    donor_tower = int(selected_towers[0]) - 1
    acceptor_tower = int(selected_towers[-1]) - 1
    deleted_element = towers[donor_tower].pop()
    towers[acceptor_tower].append(deleted_element)


#   FIXME
# Для этой функции необходимо составить нормальное описание
def checkMove(towers,selected_towers):

    # это условие нужно  FIXME сократить так как оно слишком длинное
    if selected_towers[0] not in ['1','2','3'] and selected_towers[-1] not in ['1','2','3']:
        return False
    
    donor_tower = int(selected_towers[0]) - 1
    acceptor_tower = int(selected_towers[-1]) - 1
    
    if len(towers[donor_tower]) == 0:
        logging.debug('lenght donor is a zero')
        # Если донор это пустой массив то проверку не проходит
        # далее пустого донара просто не будут пропускать
        return False
    
    if len(towers[acceptor_tower]) == 0:
        logging.debug('lenght acceptor is a zero, but donor is not zero')
        # если акцептор пустой значит перенос возможен
        return True
    
    if towers[donor_tower][-1] >= towers[acceptor_tower][-1]:
        logging.debug('donor >= acceptor')
        # донор больше или равенакцептора, значит перенос невозможен
        return False
    if towers[donor_tower][-1] < towers[acceptor_tower][-1]:
        logging.debug('donor < acceptor')
        # перенос возможен, так как донор меньше акцептора
        return True


# FIXME
# Выглядит очень непонятно исправляй, дружок

def getASCIITowers(towers,number_of_disks):
    try:
        os.system('cls')
    except:
        os.system('clear')

    towers = towers.copy()
    for i,tower in enumerate(towers):
        towers[i] = tower + [0] * (number_of_disks - len(tower))
    
    tower_elements = {0: "         ||         ",
                      1: "        =||=        ",
                      2: "       ==||==       ",
                      3: "      ===||===      ",
                      4: "     ====||====     ",
                      5: "    =====||=====    "
        }
    
    print("         /\         "*3)
    for i in range(number_of_disks-1,-1,-1):
        print(f"{tower_elements[towers[0][i]]}{tower_elements[towers[1][i]]}{tower_elements[towers[2][i]]}")
    print((" "*9 + "/\\" + " "*9) * 3)
    print(towers)

main()
