has_sword = False
has_key = False
print ('Вы очнулись в неивестной комнате')
def go_to_start():
    print ('перед вами 3 двери')
    print ('1 - первая')
    print ('2 - вторая')
    print ('3 - третья')
    action = input()
    if action == '1':
        go_to_room1()
    if action == '2':
        go_to_room2()
    if action == '3':
        go_to_room3()
    if action != '1' and action != '2' and action != '3':
        print ('Чаво, я не понял! Можно повторить ещё раз?')

def go_to_room1():
    global has_key
    print ('Чёрт, тупик! Однако тут есть ключ')
    print ('взять ли мне его?')
    action = input()
    if action == 'да':
        print ('Пожалуй возьму, мало ли где пригодится')
        has_key = True
        go_to_start()
    if action == 'нет':
        print ('Зачем мне этот хлам? Не буду я его брать!')
        go_to_start()
        
def go_to_room2():
    action = input()
    global has_sword
    print('Перед вами запертый сундук с сокровищами')
    if has_key == True:
        print ('Вы отрыли сундук и нашли там железный меч с рунами на нём')
        has_sword = True
    else:
        print ('Чёрт, у меня нет ключа!')
    print ('Перед вами 5 дерей')
    print ('1 - первая')
    print ('2 - на старт')
    print ('3 - третья')
    print ('4 - четвёртая')
    print ('5 - пятая')
    action = input()
    if action == '1':
        go_to_room3()
    if action == '2':
        go_to_start()
    if action == '3':
        go_to_room4()
    if action == '4':
        go_to_boss()
    if action == '5':
        go_to_exit()
    if action != '1' and action != '2' and action != '3' and action != '4' and action != '5':
        print ('Чаво, я не понял! Можно повторить ещё раз?')
        go_to_room2()
        
def go_to_room3():
    print ('Перед вами демонический медведь, настроенный агрессивно')
    if has_sword == True:
        print ('Вы его одолели')
    else:
        print ('он вас убил и сожрал')
        exit()
    print ('перед вами 4 двери')
    print ('1 - первая')
    print ('2 - вторая')
    print ('3 - на старт')
    print ('4 - четвёртая')
    action = input()
    if action == '1':
        go_to_room2()
    if action == '2':
        go_to_room4()
    if action == '3':
        go_to_start()
    if action == '4':
        go_to_boss()
    if action != '1' and action != '2' and action != '3' and action != '4':
        print ('Чаво, я не понял! Можно повторить ещё раз?')
        go_to_room3()
        
def go_to_room4():
    print ('Перед вами демон, настроеный агрессивно')
    if has_sword == True:
        print ('вы его успешно убили')
    else:
        print ('Он вас убил так, что и хоронить нечего.')
        exit()
    print ('перед вами 4 двери')
    print ('1 - первая')
    print ('2 - вторая')
    print ('3 - третья')
    print ('4 - четвёртая')
    action = input()
    if action == '1':
        go_to_room2()
    if action == '2':
        go_to_exit ()
    if action == '3':
        go_to_room3()
    if action == '4':
        go_to_boss()
    if action != '1' and action != '2' and action != '3' and action != '4':
        print ('Чаво, я не понял! Можно повторить ещё раз?')
        go_to_room4()
        
def go_to_boss():
    print ('перед вами - чернокнижник, который вас сюда заточил')
    print ('он желет вас убить')
    if has_sword == True:
        print ('Вы его одолели, нои он и вас нехило так поджарил')
    else:
        print ('Ваша участь не завидна, ибо он убил вас самой мучительной смертью!')
        exit()
    print ('перед вами 4 двери')
    print ('1 - первая')
    print ('2 - вторая')
    print ('3 - третья')
    print ('4 - четвёртая')
    action = input()
    if action == '1':
        go_to_room2()
    if action == '2':
        go_to_room3()
    if action == '3':
        go_to_room4()
    if action == '4':
        go_to_exit()
    if action != '1' and action != '2' and action != '3' and action != '4':
        print ('Чаво, я не понял! Можно повторить ещё раз?')
        go_to_boss
def go_to_exit():
    print ('Вы уже видите выход, а за дверью стоит ваша любимая собака!!!!')
    exit()
    
go_to_start()
