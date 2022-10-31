import sys
import time
import random

print("C-OS 0.1 Beta , Loading ...")
time.sleep(1)

print("""*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

Welcome To C-OS,

Protect By Ctox Codeworks And Ctox NewLight.
-----------------------------------------------------------
Login for press = G

For Exit Press = E
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-""")

while True:
    a= input("Please Enter Code:")
    if a == "e":
        print("Safe Exiting.")
        time.sleep(2)
        break
    elif a == "g":
        input("Protect by Ctox NewLight  , Please enter to Contiune")

        print("""********************************************
        1- Ctox CodeWorks Register (İn Work )
        2- Ctox CodeWorks Login (İn Work)
        ----------------------------------------------
        3- C-OS About The System
        4- Ctox CodeGuard (Deactive)
        5- C-OS Calculator
        6- Ctox Store
        7- My Games
        8- Files
        9- University Point Calc
        10-Ctox Produciton Offical Web
        11-Special
        12-İnfo
        13-Exit
        *********************************************""")

        say = int(input("Please Enter Code:"))

        while True:
            if say == 13:
                print("Exiting")
                break

            elif say == 1:
                import re

                kullanıcılar = {}
                durum = ""


                def get_username():
                    while True:
                        uname = input("Nickname: ")
                        if len(uname) < 3:
                            print("Min 3 Word")
                            continue
                        if re.search("\\s+", uname):
                            print("Dont Space")
                            continue
                        break  # input başarılı
                    return uname


                def get_password():
                    while True:
                        passwd = input("Ctox Password: ")
                        if len(passwd) < 5:
                            print("Password so \n\tMinimum 5 karakter olmalı\n")
                            continue
                        if re.search("\\s+", passwd):
                            print("fault")
                            continue
                        break  # input success
                    return passwd


                def register():
                    while True:
                        uname = get_username()
                        if uname not in kullanıcılar:
                            break  #
                        else:
                            print("This Nickname is already")

                    passwd = get_password()
                    if passwd:
                        kullanıcılar[uname] = passwd
                    print("Ctox Codeworks Account is Ready")


                def login():
                    for i in range(3):
                        username = input("Ctox CodeWorks Name: ")
                        if username in kullanıcılar:
                            password = input("NewLight PassWord: ")
                            if kullanıcılar[username] != password:
                                print("Fault")
                        else:
                            print("Account is not found")
                    else:
                        print("0")


                status = input("Register for k ...\n")
                if status.lower() == "k":
                    register()



            elif say == 2:
                import re

                kullanıcılar = {}
                durum = ""


                def login():
                    for i in range(3):
                        username = input("Ctox CodeWorks İsminiz: ")
                        if username in kullanıcılar:
                            password = input("NewLight Şifreniz ")
                            if kullanıcılar[username] != password:
                                print("Hatalı ")
                        else:
                            print("Kullanıcı Bulunamadı")
                    else:
                        print("Deneme sınırı aşıldı")


                status = input("Kayıt Olmak İçin (g) harfine basınız...\n")
                if status.lower() == "g":
                    login()






            elif say == 3:
                import platform

                my_system = platform.uname()

                print("C-OS 0.1 beta")
                print(f"System: {my_system.system}")
                print(f"Node Name: {my_system.node}")
                print(f"Release: {my_system.release}")
                print(f"Version: {my_system.version}")
                print(f"Machine: {my_system.machine}")
                print(f"Processor: {my_system.processor}")

                break



            elif say == 5:
                print("""****************************

                1 . (+)

                2 . (-)

                3 . (*)

                4 . (/)

                5 . (fac)
                *****************************
                """)

                input("Enter , continue")

                a = int(input("First Number :"))
                b = int(input("Second Number :"))

                pro = input("Process Number :")

                if pro == "1":
                    print("{} + {} = {}".format(a, b, a + b))

                elif pro == "2":
                    print("{} - {} = {}".format(a, b, a - b))

                elif pro == "3":
                    print("{} * {} = {}".format(a, b, a * b))

                elif pro == "4":
                    print("{} / {}  = {}".format(a, b, a / b))

                else:
                    print("Error")

            elif say == 6:
                print("""***************************************************


                Welcome To  Ctox Store...

                1. C-Coin
                2. C-Coin Store
                3. Ctox Game Store
                4. Exit
                *****************************************************""")

                print("Protect by Ctox CodeWorks ")
                time.sleep(2)



                while True:
                    bakiye = 150

                    a = int(input("Please Type the Process Number :"))

                    if (a == 4):
                        print("Safe Exit")


                        def say():
                            return say

                    elif (a == 1):
                        print("C-Coin : {} ".format(bakiye))

                    elif (a == 2):
                        print("""*************************

                          1- 1.000  =  tl steam Key
                          2- 5.000  = Özel oyun
                          3- 100.000 = Cyberpunk


                          **************************""")
                    elif (a == 3):
                        print("""------------------------
                        1- Cyberpunk = 100.000 
                        2- red Dead Redemption 2 = 175.000 
                        3- Witcher 3 = 1000 

                        


                        --------------------------""")

                        abc = int(input("Type Game Code:"))

                        if abc == 1:
                            print("C-coin is loading")
                            time.sleep(3)
                            bakiye <= 1000
                            print("enough coin")

                        elif abc == 2:
                            print("C-coin is loading")
                            time.sleep(3)
                            bakiye <= 100000
                            print("enough coin")

                        elif abc == 3:
                            print("C-coin is loading")
                            time.sleep(3)
                            bakiye <= 1000000
                            print("enough coin")

                        else:
                            print("Error")
                            break


            elif say == 7:
                print("""
                   C OS Gaming

                   1- Ctox Football Manager 2023(GAME)
                   2- Haaland (GAME)
                   3-Valo r6 sens converter(program)
                   4.EXİT
                   """)

                t = input("Sistem kodunu giriniz:")

                while True:
                    if t == "4":
                        print("Exit ")
                        break

                    elif t == "1":
                        import time
                        import random

                        print("""*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

                                           CTOX FOOTBALL MANAGER 2023 / BARCELONA Edition


                                           CTOX Football Manager ,

                                           1- Be Legend
                                           2- İnfo Ctox
                                           3- Exit
                                           4- C-COİN Game Cards(soon)


                                           *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                                           """)


                        a = int(input("Process Number:"))

                        while True:
                            if a == 3:
                                print("Exit")
                                time.sleep(2)
                                break




                            elif a == 1:

                                my_team_name = input('name your team: ')
                                opp_team_names = ['Manu', 'City', 'Madrid', 'Cheal']
                                opp_team_name = random.choice(opp_team_names)
                                print('your match is against {}'.format(opp_team_name))
                                pass_text = [' gives the ball to ', ' passes it to ', ' sharply gives it to ',
                                             ' puts it in the path of ']
                                defend_text = [' performs a great tackle ', ' comes up with a meaty tackle ']
                                shoot_text = ['hits the ball ', ' curls it towards the goal ', ' shoots ']
                                goal = ' have scored a beauty!'
                                no_goal = " have missed it!"

                                opp_team = ['jamie', 'kurt', 'andy', 'jack', 'sam', 'michael', 'roberts', 'samuel',
                                            'zack', 'charlie', ' bob']


                                def matchStart():
                                    my_team_score = 0
                                    opp_team_score = 0
                                    match_time = 0
                                    print("ref blows the whistle and we're under way!")
                                    while match_time < 10:
                                        goal_or_not = random.randint(0, 1)
                                        whose_ball = random.randint(0, 1)
                                        if whose_ball == 0:
                                            time.sleep(2)
                                            print("the ball is taken and {} {} {} {} ".format(random.choice(opp_team),
                                                                                              random.choice(pass_text),
                                                                                              random.choice(opp_team),
                                                                                              random.choice(
                                                                                                  shoot_text)))
                                            time.sleep(2)
                                            if goal_or_not == 1:
                                                print("{} score!".format(opp_team_name))
                                                opp_team_score += 1
                                                time.sleep(2)
                                                print(" it's {} {} ".format(str(my_team_score), str(opp_team_score)))
                                                match_time += 1
                                            else:
                                                time.sleep(2)
                                                print("{} {} {} {}".format(random.choice(my_team),
                                                                           random.choice(pass_text),
                                                                           random.choice(my_team),
                                                                           random.choice(shoot_text)))
                                                time.sleep(2)
                                                print("{} {}!".format(opp_team_name, no_goal))
                                                match_time += 1
                                        else:
                                            if goal_or_not == 1:
                                                time.sleep(2)
                                                print("{} {} {} {}".format(random.choice(my_team),
                                                                           random.choice(pass_text),
                                                                           random.choice(my_team),
                                                                           random.choice(shoot_text)))
                                                time.sleep(2)
                                                print("{} {}!".format(my_team_name, goal))
                                                my_team_score += 1
                                                time.sleep(2)
                                                print(" it's {} {} ".format(str(my_team_score), str(opp_team_score)))
                                                match_time += 1
                                            else:
                                                time.sleep(2)
                                                print("{} {} {} {}".format(random.choice(my_team),
                                                                           random.choice(pass_text),
                                                                           random.choice(my_team),
                                                                           random.choice(shoot_text)))
                                                time.sleep(2)
                                                print("{} {}!".format(my_team_name, no_goal))
                                                time.sleep(2)
                                                match_time += 1

                                    if my_team_score > opp_team_score:
                                        print("{} {} {} win!".format(my_team_score, opp_team_score, my_team_name))
                                    elif my_team_score < opp_team_score:
                                        print("{} {} {} win!".format(my_team_score, opp_team_score, opp_team_name))
                                    else:
                                        print("{} {} It's a tie".format(my_team_score, opp_team_score))


                                manager_name = input('enter name of manager: ')
                                print(
                                    'hi {} , you have $120 million dollars to start with and build your very own dream team .' \
                                    "you can buy 11 players.listed player prices are in million ".format(manager_name))

                                my_budget = 350
                                players =  {'benzema': 25, 'lewa': 25, 'haaland': 50, 'gavi': 35, 'havertz': 30,
                                             'de jong': 30,
                                             'ronaldo': 45, 'messi': 10, 'alisson': 31, 'hazard ': 30, 'foden': 25,
                                             'ramos'
                                             : 40, 'aguero': 40, 'neymar': 45, 'suarez': 20}
                                my_team = []

                                for key, value in players.items():
                                    print("Name: {} Value: {} Million Dollars".format(key, value))

                                while len(my_team) < 11:
                                    buy_player = input('name player to buy: ')
                                    if buy_player in my_team:
                                        print(buy_player + " is already in your team")
                                        continue
                                    if buy_player not in players:
                                        print(
                                            'that player is not available for transfer . check the transfer list again')
                                        continue
                                    print(
                                        "Player: {} Value: {} Million Dollars; {}'s Budget: {} Million Dollars".format(
                                            buy_player, players[buy_player], manager_name, my_budget))
                                    ask_final = input(
                                        'are you sure you want to make this purchase ? (yes or no) , this cannot be reversed; ')
                                    if ask_final.lower() != "yes":
                                        continue
                                    if my_budget - players[buy_player] <= 0:
                                        print("insufficient funds")
                                        ask_to_sell = input('you need to sell players , enter name of player to sell')
                                        if ask_to_sell not in my_team:
                                            continue
                                        print("{} ,  Value: {} Million Dollars.Sold ".format(ask_to_sell,
                                                                                             players[buy_player]))
                                        my_team.remove(ask_to_sell)
                                        my_budget += players[ask_to_sell]
                                        print("{} is your new budget".format(my_budget))
                                        print("you have {} players in your team".format(str(len(my_team))))
                                        continue
                                    my_budget -= players[buy_player]
                                    my_team.append(buy_player)
                                    print("you have {} players in your team".format(str(len(my_team))))

                                print("\n".join(my_team))
                                print('  This is your final team.May you achieve victory and glory with them!')

                                matchStart()


                            elif a == 2:
                                print("""********************************
                                       -Ctox CodeWorks
                                       -Tatarius
                                       -codeboy101(github)

                                       İlk tanıtım : 2015
                                       Revizyon : 2022 (Ctox)

                                       Oyun Sürümü : 1.2 
                                       ********************************""")
                                break

                            else:
                                break


                    elif t == "2":
                        import random
                        import time

                        print("""*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/


                                          HAALAND guessing game...



                                          */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/""")

                        input("Plase type 0 to 60 goal number")

                        sayı = random.randint(1, 60)
                        hak = 7

                        while True:

                            gol = int(input("Haaland Goal this year:"))

                            if (gol < sayı):
                                print("Moreeeee")
                                time.sleep(1)

                                print("plase say high")

                                hak -= 1

                            elif (gol > sayı):
                                print("no no no")
                                time.sleep(1)

                                print("Say lower")

                                hak -= 1

                            else:
                                print("Good Job ", sayı)
                                break

                                bakiye += 50

                            if (hak == 0):
                                print("calculating")
                                time.sleep(1)
                                print("zero")
                                break


                    elif t == "3":
                        A = float(input("Rainbow Six Sens:"))
                        B = float(input("Valorant Sens:"))

                        input("Calculating ")

                        print("Your New Sens for R6 to valo", A * (0.081851))
                        print("Your New Sens for Valo to R6", B * (12.217305))

                    else:
                        print("error")
                        break



            elif say == 8:
                print("""**************************************

                1-System Files C-OS
                2-Downloads
                3-Photos
                4-EXit

                ****************************************""")

                q = int(input("Process Number:"))
                if q == 4:
                    print("Exit ")
                    time.sleep(2)
                    break

                elif q == 1:
                    input("""
                    -System C-OS 
                    -System Main Files
                    -C OS Main Visuals 
                    -Windows X C-Os 
                    """)


                elif q == 2:
                    input("""
                    -Haalandgame.py
                    -Ctoxfootball.py
                    """)
                    break

                elif q == 3:
                    print("""
                    -haaland.png
                    """)
                    break
                else:
                    print("error")


            elif a == 9:
                not1 = float(input("First Note:"))
                not2 = float(input("Second:"))
                final = float(input("Final:"))

                note = not1 * 3 / 10 + not2 * 3 / 10 + final * 4 / 10

                if note >= 90:
                    print("AA")
                elif note >= 85:
                    print("BA")
                elif note >= 90:
                    print("BA")
                elif note >= 80:
                    print("BB")
                elif note >= 75:
                    print("CB")
                elif note >= 70:
                    print("CC")
                elif note >= 65:
                    print("DC")
                elif note >= 60:
                    print("DD")
                else:
                    print(":(")




            elif say == 10:
                print("Loading...")
                time.sleep(2)
                import webbrowser

                webbrowser.open("https://ctoxbilisim.blogspot.com/")
                break

            elif say == 11:
                from turtle import *

                color('blue', 'yellow')
                begin_fill()
                while True:
                    forward(200)
                    left(170)
                    if abs(pos()) < 1:
                        break
                end_fill()
                done()
                break

            elif say == 12:

                input("""*******************************************************

            -C OS 0.1 English Version
            -This is Product of Ctox CodeWorks . 
            -Ctox NewLight Guard 
            -Discord/ https://discord.gg/sQtSVF7F


            **************************************************""")
                break

            else:
                print("geçersiz işlem")