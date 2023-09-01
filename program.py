import os

# Функция в которой происходит основная логика игры
def main():
    """
    Игра будет  работать в несколько  ходов. Сначала создаются  три массива
    символизирующие три башни.  В первую башню  добавляются 5  элементов от
    5 до 1 (это важно). Основываясь на  этих массивах создается изображение
    башень. На вход  будет подаваться страка из двух номеров  башень. После
    ввода происходит  проверка на корректность  ввода. По  выбранным башням
    происходит  перенос диска с  одной башни  на  другую.  Как  только  все 
    элементы оказываются на одной из двух оставшихся башень, игра завершена
    """
    number_of_disks = 7
    move_number = 0
    first_tower = [i for i in range(number_of_disks,0,-1)]
    second_tower = []
    last_tower = []
    towers = [first_tower,second_tower,last_tower]
    
    while True:
        PrintASCIITowers(towers=towers,number_of_disks=number_of_disks,
                         move_number=move_number)
        
        choose_towers = input("выберите башни:") 
        # Условие корректности ввода
        if checkMove(towers=towers,
                     selected_towers=choose_towers) == False:  
            
            continue
        else:
            
            makeMove(towers=towers,
                     selected_towers=choose_towers)
            move_number += 1
        
        # Подедное условие
        if (len(second_tower) == number_of_disks) or (len(last_tower) == number_of_disks):
            try:
                os.system("cls")
            except:
                os.system("clear")
            print(f"Поздравляю! Вы победили за {move_number} ходов")
            break

# Функция сохраняет удаленный из донора элемент  и добавляет его в акцептор
def makeMove(towers,selected_towers):
    """
    Функция предназначена для того, чтобы переместить диск с одной башни на
    другую.    Донорской  считается  башня,  с  которой  заимстуется  диск,
    акцепторной-ту на которую будет перекладываться диск. Последний элемент
    с донорского массива  удаляется, и присваивается  акцепторному массиву.
    """
    donor_tower = int(selected_towers[0]) - 1
    acceptor_tower = int(selected_towers[-1]) - 1
    deleted_element = towers[donor_tower].pop()
    towers[acceptor_tower].append(deleted_element)

# Функция проверяет введенный пользователем значения башень
def checkMove(towers,selected_towers):
    """
    Функция предназначена для проверки выбранных  пользователем  башень. На
    выбор пользователя три значения для  башень. И в зависсимости от  того,
    какой будет  выбор-будет соответствующий вывод. Если введенное значение
    не подпадает под correct_input,  то возвращатся будет False.  В  случае
    если donor_tower будет пуста,  возвращаться  будет  False,  потому  что
    перенос элемента из пустого  массива  не  возможен.  Если  акцепторская
    башня пуста (при действительности предыдущего условия) перенос возможен
    Если последний диск донорской башни больше диска акцепторской башни, то
    перенос не возможен по условию игры. В случае  если  последний  элемент
    донорской башни чем акцепторской, то перенос возможен.
    """
    correct_input = ["1","2","3"]
    donor_tower = selected_towers[0]
    acceptor_tower = selected_towers[-1]
    if donor_tower not in correct_input and acceptor_tower not in correct_input:
        return False
    
    # действительные индексы массивов на 1 меньше чем ввод пользователя
    donor_tower = int(selected_towers[0]) - 1
    acceptor_tower = int(selected_towers[-1]) - 1
    
    # проверка донорской башни на наличие дисков
    if len(towers[donor_tower]) == 0:
        return False
    
    # проверка акцепторской башни на наличие элементов
    if len(towers[acceptor_tower]) == 0:
        return True
    
    # проверка того, что диск донора больше диска акцептора
    if towers[donor_tower][-1] >= towers[acceptor_tower][-1]:
        return False
    # проверка того, что диск донора меньше диска акцептора
    if towers[donor_tower][-1] < towers[acceptor_tower][-1]:
        return True

#
def PrintASCIITowers(towers,number_of_disks,move_number):
    """
    Функция предназначена для того, чтобы на  основе  полученных  массивов
    сделать ASSCI картинку в консоли. Если в массиве не хватает  элементов
    то они будут дополняться нулями. Сначала отчищается консоль после чего
    создается словарь из возможных отображений дисков.  По  соответсвующим
    значениям для элементов массивов, составляется картинка башень
    """
    try:
        os.system("cls")
    except:
        os.system("clear")

    towers = towers.copy()
    for i,tower in enumerate(towers):
        towers[i] = tower + [0] * (number_of_disks - len(tower))
    
    tower_elements = {0: "         ||         ",
                      1: "        =||=        ",
                      2: "       ==||==       ",
                      3: "      ===||===      ",
                      4: "     ====||====     ",
                      5: "    =====||=====    ",
                      6: "   ======||======   ",
                      7: "  =======||=======  ",
                      8: " ========||======== "
        }
    
    
    print("         /\         "*3) # Шапка башень
    for i in range(number_of_disks-1,-1,-1):
        first_tower_disk = tower_elements[towers[0][i]]
        second_tower_disk = tower_elements[towers[1][i]]
        last_tower_disk = tower_elements[towers[2][i]]
        print(f"{first_tower_disk}{second_tower_disk}{last_tower_disk}")
    print((" "*9 + "/\\" + " "*9) * 3)
    print(f"{move_number} ходов")

main()

