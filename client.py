import socket
import time
import os
import threading
from random import randrange
# import winsound

xyz = 0


def print_notif(x):
    global player, name, s, bot
    for i in sorted(x):
        i = i.upper()
        if i[0] == 'K':
            if name == i[1]:
                clearscreen()
                print("||    ||  |||||||||  ||     ||    ||||     ||  |||||||")
                print(" ||  ||   ||     ||  ||     ||    || ||    ||  ||")
                print("  ||||    ||     ||  ||     ||    ||  ||   ||  ||")
                print("   ||     ||     ||  ||     ||    ||   ||  ||  |||||||")
                print("   ||     ||     ||  ||     ||    ||  ||   ||  ||")
                print("   ||     ||     ||  ||     ||    || ||    ||  ||")
                print(
                    "   ||     |||||||||  |||||||||    ||||     ||  |||||||  ||  ||  ||")
                # sound2()
                s.send("-".encode('ascii'))
                s.close()
                return False
            else:
                print("<< %s(%s) was killed >>" %
                      (i[1], 'player' if i[1] in player else 'bot'))
            bot = bot.replace(i[1], '')
        elif i[0] == 'E':
            if i[1] == name:
                name = i[2]
                print("Your Name Is \'%s\'" % name)
            bot = bot.replace(i[2], '')
            player = player.replace(i[1], '')
            bot = "%s%s" % (bot, i[1])
            player = "%s%s" % (player, i[2])
            print("bot =", bot)
            print("player =", player)

        elif i[0] == 'I' and i[1] == name:
            add_item()
        elif i[0] == 'D' and name in i[1:]:
            print("<< You was Detected >>")
        elif i[0] == 'C':
            print("<< Cursing >>")
        elif i[0] == 'U':
            print("<< Uncursing >>")
    return True


def print_map(x):
    size = 9
    map_ = [[] for i in range(size * size)]
    stack = []
    for i in x:
        map_[int(i[0]) * size + int(i[1])].append(i[2]
                                                  if i[2]in player else i[2].lower())
    for i in range(size):
        if i % 3 == 0:
            print('-' * (size // 3 * 4 + 1))
        for j in range(size):
            if j % 3 == 0:
                print('|', end='')
            if len(map_[i * size + j]) > 1:
                map_[
                    i * size + j] = [k for k in map_[i * size + j] if k != '?']
            if len(map_[i * size + j]) == 0:
                print(' ', end='')
            elif len(map_[i * size + j]) == 1:

                print(map_[i * size + j][0], end='')
            else:
                print(len(stack), end='')
                stack.append(map_[i * size + j])
        print("|")
    print('-' * (size // 3 * 4 + 1))
    for i in range(len(stack)):
        print('*%d' % i, "=", stack[i])


def clearscreen():
    try:
        os.system('clear')
    except:
        os.system('cls')


def add_item():
    global item_name, ITEM
    possible = '2223335' + 'P' * 2 + 'E' * 1 + 'C' * 1 + 'F' * 2 + 'LXZ'
    ans = possible[randrange(0, len(possible))]
    if '0' <= ans <= '9':
        ITEM['H'] += int(ans)
        print("Get >>", item_name['H'], 'x' + ans)
    else:
        ITEM[ans] += 1
        print("Get >>", item_name[ans])


# connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9999
size = 2048
item_name = {'H': '[H]ack', 'P': '[P]ush', 'E': '[E]xchange', 'C': '[C]urse',
             'F': '[F]ake Curse', 'L': 'kill [L]ane.', 'X': 'kill [X]cross.', 'Z': 'kill [Z]one.'}
ITEM = dict()


# def sound():
#     global xyz
#     xyz += 1
#     winsound.PlaySound('dang.wav', winsound.SND_ALIAS)


# def sound2():
#     winsound.PlaySound('dang2.wav', winsound.SND_ALIAS)


def flsh():
    global xyz
    for flash in range(3):
        print(
            '     ||     ||  |||      ||  ||||||||||  ||  ||||||||||  ||       |||||||||')
        print(
            '     ||     ||  ||||     ||      ||      ||      ||      ||       ||       ')
        print(
            '     ||     ||  ||  ||   ||      ||      ||      ||      ||       ||       ')
        print(
            '     ||     ||  ||   ||  ||      ||      ||      ||      ||       |||||||||')
        print(
            '     ||     ||  ||    || ||      ||      ||      ||      ||       ||       ')
        print(
            '     ||     ||  ||     ||||      ||      ||      ||      ||       ||       ')
        print(
            '     |||||||||  ||      |||      ||      ||      ||      |||||||  |||||||||')
        time.sleep(0.3)
        clearscreen()
        print(
            '    ||     ||  |||      ||  ||||||||||  ||  ||||||||||  ||       |||||||||')
        print(
            '     ||     ||  ||||     ||      ||      ||      ||      ||       ||       ')
        print(
            '      ||     ||  ||  ||   ||      ||      ||      ||      ||       ||       ')
        print(
            '    ||     ||  ||   ||  ||      ||      ||      ||      ||       |||||||||')
        print(
            '     ||     ||  ||    || ||      ||      ||      ||      ||       ||       ')
        print(
            '      ||     ||  ||     ||||      ||      ||      ||      ||       ||       ')
        print(
            '     |||||||||  ||      |||      ||      ||      ||      |||||||  |||||||||')
        time.sleep(0.05)
        clearscreen()
        print(
            '    ||     ||  |||      ||  ||||||||||  ||  ||||||||||  ||       |||||||||')
        print(
            '     ||     ||  ||||     ||      ||      ||      ||      ||       ||       ')
        print(
            '     ||     ||  ||  ||   ||      ||      ||      ||      ||       ||       ')
        print(
            '      ||     ||  ||   ||  ||      ||      ||      ||      ||       |||||||||')
        print(
            '     ||     ||  ||    || ||      ||      ||      ||      ||       ||       ')
        print(
            '    ||     ||  ||     ||||      ||      ||      ||      ||       ||       ')
        print(
            '     |||||||||  ||      |||      ||      ||      ||      |||||||  |||||||||')
        time.sleep(0.05)
        clearscreen()
        xyz += 1
for i in item_name:
    ITEM[i] = 0
flsh()
add_item()
while True:
    try:
        host = input("Connect to HOST = ")
        #host = socket.gethostname()
        s.connect((host, port))
        s.settimeout(99999)
        print("Connecting Complete")
        break
    except:
        print("Cant Connnect to Server")

# Game Start
while True:
        try:
            name = s.recv(4).decode('ascii')
            break
        except:
            pass
print("Your Name Is \'%s\'" % name)
print("WAITING for other player")
while True:
        try:
            player, bot = s.recv(1024).decode('ascii').split()
            break
        except:
            pass
print(player)
while True:
        try:
            msg = s.recv(2048).decode('ascii')
            break
        except:
            pass
strmap = msg
# print_map(msg.split())

# loop for each turn
while True:
    msg = '...'
    while True:
        print_map(strmap.split())
        print("[M]ove.: [U]p,[D]own,[L]eft,[R]ight")
        for i in sorted(ITEM):
            if ITEM[i] > 0:
                print(' -', item_name[i], 'x%d' % ITEM[i])
        print("[I]nformation:[""command""]")
        print("End[.]")
        x = input(" -> ").upper()
        #x = 'M'+'UDLRI'[randrange(0,5)]
        if x[0:3] == '\\\\ ':
            msg = x[3:]
            break
        else:
            if len(x) > 0:
                i = x[0]
                x = x[1:]
            else:
                print("INPUT ERROR: please try again")
                continue
            # Case Move
            if i == 'M':
                if len(x) > 0:
                    i = x[0]
                    x = x[1:]
                else:
                    print("[U]p,[D]own,[L]eft,[R]ight")
                    i = input(" -> ").upper()
                    if i == '..':
                        continue
                if i in ['U', 'D', 'L', 'R', 'I']:
                    msg = "%s %s" % (msg, name + 'm' + i + name)
                    break
                else:
                    print("INPUT ERROR: please try again")
                    continue
            elif i == 'H' and ITEM['H'] > 0:
                can_ = name + bot.lower()
                if len(x) > 0:
                    i = x[0]
                    x = x[1:]
                else:
                    print("\'%s\'" % can_)
                    i = input(" -> ").upper()
                    if i == '..':
                        continue
                if i in [j for j in can_.upper()]:
                    if len(x) > 0:
                        j = x[0]
                        x = x[1:]
                    else:
                        print("[U]p,[D]own,[L]eft,[R]ight")
                        j = input(" -> ").upper()
                        if j == '..':
                            continue
                    if j in ['U', 'D', 'L', 'R', 'I']:
                        msg = "%s %s" % (msg, i + 'H' + j + name)
                        print("Hack >> %s %s" % (i, j))
                        ITEM['H'] -= 1
                    else:
                        print("INPUT ERROR: please try again")
                        continue
            elif i == 'P' and ITEM['P'] > 0:
                can_ = name + bot.lower()
                if len(x) > 0:
                    i = x[0]
                    x = x[1:]
                else:
                    print("\'%s\'" % can_)
                    i = input(" -> ").upper()
                    if i == '..':
                        continue
                if i in [j for j in can_.upper()]:
                    if len(x) > 0:
                        j = x[0]
                        x = x[1:]
                    else:
                        print("[U]p,[D]own,[L]eft,[R]ight")
                        j = input(" -> ").upper()
                        if j == '..':
                            continue
                    if j in ['U', 'D', 'L', 'R', 'I']:
                        if len(x) > 0:
                            k = x[0]
                            x = x[1:]
                        else:
                            print("Distance [0-8]")
                            k = input(" -> ").upper()
                            if k == '..':
                                continue
                        if '0' <= k <= '8':
                            msg = "%s%s" % (
                                msg, (' ' + i + 'P' + j + name) * int(k))
                            print("Push >> %s %s %s" % (i, j, k))
                            ITEM['P'] -= 1
                        else:
                            print("INPUT ERROR: please try again")
                            continue
                    else:
                        print("INPUT ERROR: please try again")
                        continue
                else:
                    print("INPUT ERROR: please try again")
                    continue
            elif i == 'E' and ITEM['E'] > 0:
                can_ = name + bot.lower()
                if len(x) > 0:
                    i = x[0]
                    x = x[1:]
                else:
                    print("\'%s\'" % can_)
                    i = input(" -> ").upper()
                    if i == '..':
                        continue
                if i in [j for j in can_.upper()]:
                    msg = "%s %s" % (msg, (name + 'E' + i))
                    print("Exchange >>", i)
                    ITEM['E'] -= 1
                else:
                    print("INPUT ERROR: please try again")
                    continue
            elif i == 'C' and ITEM['C'] > 0:
                can_ = name + bot.lower()
                if len(x) > 0:
                    i = x[0]
                    x = x[1:]
                else:
                    print("\'%s\'" % can_)
                    i = input(" -> ").upper()
                    if i == '..':
                        continue
                if i in [j for j in can_.upper()]:
                    msg = "%s %s" % (msg, (i + 'C'))
                    print("Curse >>", i)
                    ITEM['C'] -= 1
                else:
                    print("INPUT ERROR: please try again")
                    continue
            elif i == 'F' and ITEM['F'] > 0:
                msg = "%s %s" % (msg, ('_F'))
                print("Fake Curse")
                ITEM['F'] -= 1
            elif i in ['L', 'X', 'Z'] and ITEM[i] > 0:
                map_ = strmap.split()
                can_ = []
                for k in map_:
                    if k[2] == name:
                        mypos = k[0:2]
                        break
                if i == 'L':
                    for k in map_:
                        if k[2] in bot:
                            if k[0] == mypos[0] or k[1] == mypos[1]:
                                can_.append(k[2])
                elif i == 'X':
                    for k in map_:
                        if k[2] in bot:
                            if int(k[0]) - int(k[1]) == int(mypos[0]) - int(mypos[1]) or int(k[0]) + int(k[1]) == int(mypos[0]) + int(mypos[1]):
                                can_.append(k[2])
                elif i == 'Z':
                    for k in map_:
                        if k[2] in bot:
                            if int(k[0]) // 3 * 3 + int(k[1]) // 3 == int(mypos[0]) // 3 * 3 + int(mypos[1]) // 3:
                                can_.append(k[2])
                if len(x) > 0:
                    j = x[0]
                    x = x[1:]
                else:
                    print("\'%s\'" % ''.join(can_))
                    j = input(" -> ").upper()
                    if j == '..':
                        continue
                if j in can_:
                    msg = "%s %s" % (msg, ('_' + i + j))
                    print("Kill >>", j)
                    ITEM[i] -= 1
                    break
                else:
                    print("INPUT ERROR: please try again")
                    continue
            # elif i == '+':
            #     clearscreen()
            #     if len(x) == 0:
            #         x = input('Adding -> ').upper()
            #         if x == '..':
            #             continue
            #     if x in ITEM :
            #         ITEM[x] += 1
            #         print('<< Adding',item_name[x],'>>')
            elif i == 'I':
                clearscreen()
                print('================================================================================')
                if len(x) == 0:
                    print("Input your action or item that you want to know")
                    x = input(' -> ').upper()
                    if x == '..':
                        continue
                if x[0] in ['M', 'H', 'P', 'E', 'C', 'F', 'L', 'X', 'Z', '.']:
                    if x == 'M':
                        print('[M]ove use to move your character')
                    elif x == 'H':
                        print(' #H              T')
                        print('   &            ()O')
                        print('   *A_.-' ' -._%A')
                        print("   ,', ~'` ( .'`.")
                        print("  ( ~'_ , .'(  > )")
                        print(" ( . ' (  `__. <  )")
                        print("  ( ` ..  '_   . ')")
                        print("   `(_( ( ' ` '. )")
                        print("      @`-.__. '=/")
                        print("    A#    `._`='@")
                        print('    %        \\\  #')
                        print('  H$             !')
                        print(' @                G#')
                        print('?                   ?')
                        print(
                            '[H]ack use to control bot or yourself to gain extra move')
                        print(
                            'And when you control bot to pick up an item you will recive that item')
                    elif x == 'P':
                        print('     @        @')
                        print('      @   @@   @@')
                        print('    @@      @    @')
                        print('@@@@@        @    @')
                        print('           @@     @')
                        print('@@@@@@@@@@@      @')
                        print('               @@')
                        print('        @@@@@@@   _O_')
                        print('@@@@@@@@@       (=| |')
                        print('                  |_|')
                        print('@@@@@@@@@@')
                        print('         @@@@@@')
                        print('               @')
                        print('                @')
                        print('[P]ush use to push player or bot (0-8 unit)')
                    elif x == 'E':
                        print(
                            '[E]xchange use to swap your with bot or yourself')
                    elif x == 'C':
                        print('    @@@       @@@')
                        print('   @@PP       bb@@')
                        print('   @PPP       bbb@')
                        print('   @PPP       bbb@')
                        print('   @PPP   /   bbb@')
                        print('    @@@  /==  @@@')
                        print('  @@PPP  \==  bbb@@')
                        print(' @@PPPP   \   bbbb@@')
                        print(' @PPPPP       bbbbb@')
                        print(' @PPPPP       bbbbb@')
                        print(' @PPPPP       bbbbb@')
                        print('  @PPPP       bbbb@')
                        print('   @@PP       bb@@')
                        print('    @@@       @@@')
                        print(
                            '[C]urse use to make bot rise "player" instead "bot" when detected')
                    elif x == 'F':
                        print('      ______ _')
                        print('     /  _/ /( )___')
                        print('    _/ // __//(_ <')
                        print('   /___/\__/ /___/')
                        print('         ___')
                        print('        / _ |')
                        print('       / __ |')
                        print('      /_/ |_|')
                        print('  ______')
                        print(' /_  __/______ ____')
                        print('  / / / __/ _ `/ _ \ ')
                        print(' /_/ /_/  \_,_/ .__/')
                        print('             /_/')
                        print('')
                        print(
                            '[F]ake Curse use to rise the notification of [C]urse but dont have any effect')
                    elif x == 'L':
                        print('   %   _______')
                        print('   %   |     |')
                        print('   %  (| | | |)')
                        print('   %   |_____|')
                        print('   %     [_] ')
                        print('%%%%%%%%%%%%%%%%%%%%%')
                        print('   %      |')
                        print('   %      V')
                        print('   %')
                        print('   %   .-"""-.')
                        print('   %  / _   _ \ ')
                        print("   %  ](_' `_)[")
                        print("   %  `-. * ,-'")
                        print('   %    |---|')
                        print(
                            'Kill [L]ane use to kill 1 bot in your direction')
                    elif x == 'X':
                        print('%%     _______     %%')
                        print('  %    |     |    %')
                        print('   %% (| | | |) %%')
                        print('     % |_____| %')
                        print('      %  [_]  %')
                        print('       %%   %%')
                        print('         %|%')
                        print('         %V%')
                        print('       %%   %%')
                        print('      %.-"""-.%')
                        print('     %/ _   _ \%')
                        print("   %% ](_' `_)[ %%")
                        print("  %   `-. * ,-'   %")
                        print('%%      |---|      %%')
                        print(
                            'Kill [X]cross use to kill 1 bot in your cross direction')
                    elif x == 'Z':
                        print('   |%%%_______%%%|')
                        print('   |%%%|     |%%%|')
                        print('   |%%(| | | |)%%|')
                        print('   |%%%|_____|%%%|')
                        print('   |%%%%%[_]%%%%%|')
                        print('   |%%%%%%%%%%%%%|')
                        print('   |      |      |')
                        print('   |      V      |')
                        print('   |             |')
                        print('   |   .-"""-.   |')
                        print('   |  / _   _ \  |')
                        print("   |  ](_' `_)[  |")
                        print("   |  `-. * ,-'  |")
                        print('   |    |---|    |')
                        print('Kill [Z]one use to kill 1 bot in your zone')
                    elif x == '.':
                        print('End[.] use to end your turn')
                    else:
                        print("INPUT ERROR: please try again")
                        continue
                    print(
                        '================================================================================')
                else:
                    print("INPUT ERROR: please try again.")
            elif i == '.':
                break
            else:
                print("INPUT ERROR: please try again")
                continue
    s.send(msg.encode('ascii'))

    print("WAITING for other player")
    while True:
        try:
            msg = s.recv(2048).decode('ascii')
            break
        except:
            pass
    clearscreen()

    notif, strmap = msg.split(',')
    notif = notif.split()
    if '-' in notif:
        print("YOU WIN!!")
        s.close()
        time.sleep(3)
        break
    if print_notif(notif) == False:
        break
    print_map(strmap.split())
