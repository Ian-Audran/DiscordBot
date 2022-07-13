import Encrypt
import json

data = json.loads(Encrypt.GetJsonData())
print(json.dumps(data, indent=2))

def sort():
    list = [1, 4, 6, 3, 0, 5]
    newlist = []
    for c in range(len(list)):
        a = 9999999999999999
        for i in range(len(list)):
            if list[i] < a:
                a, i2 = list[i], i

        newlist.append(a)
        list.remove(list[i2])

    print(list)
    print(newlist)

def TriBulle(T):
  Permut = True
  while Permut:
    Permut = False
    for i in range(len(T)-1):
      if T[i+1] < T[i]:
        T[i], T[i+1] = T[i+1], T[i]
        Permut = True


def LeaderboardTest(guild_id):
    Order = ["DD", "UD", "DE", "N", "OC", "SP", "SX", "QN", "QD", "T", "B", "M", "K"]
    PList = []
    SPList = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    Message = []
    Place = 1
    PlayersTp = []

    data = json.loads(Encrypt.GetJsonData())
    for i in range(len(data['Servers'])):
        if data['Servers'][i]['guild_id'] == guild_id:
            for p in range(len(data['Servers'][i]['Players'])):
                formated_tp = []
                Username = data['Servers'][i]['Players'][p]['username']
                Tp = data['Servers'][i]['Players'][p]['tp']
                for c in Tp:
                    if any(map(str.isdigit, c)) or c == "." or c == ",":
                        pass
                    else:
                        formated_tp.append(c)
                Tpletter = "".join(formated_tp)
                Number = Tp.replace(Tpletter, "")
                Number = Number.replace(",", ".")
                PList.append([Username, Tpletter.upper(), Number])
                PlayerTp = str(Number) + " " + str(Tpletter.upper())
                print(Username, PlayerTp)

                PlayersTp.append([PlayerTp, Username])

            for i in range(len(Order)):
                for p in range(len(PList)):
                    if PList[p][1] == Order[i]:
                        SPList[i].append(PList[p])

            print(SPList)

            for tpclass in SPList:
                Permut = True
                while Permut:
                    Permut = False
                    for i in range(len(tpclass) - 1):
                        if tpclass[i + 1][2] < tpclass[i][2]:
                            tpclass[i], tpclass[i + 1] = tpclass[i + 1], tpclass[i]
                            Permut = True

            print(SPList)

            for i in range(len(SPList)):
                if len(SPList[i]) > 0:
                    titre = f'\n      ꧁༺☠༒"THE {Order[i]}"༒☠༻꧂\n'
                    Message.append(titre)
                    for player in SPList[i]:

                        for PLAYER in PlayersTp:
                            if PLAYER[1] == player[0]:
                                playertp = PLAYER[0]
                        PlaceCalc = f"{Place}) "
                        #print(len(str(playertp)))
                        LineLen = len(PlaceCalc) + len(player[0]) + len(str(playertp))
                        if 38 - LineLen > 0:
                            missing = 35 - LineLen
                            #print(missing)
                            for k in range(missing):
                                player[0] = player[0] + " "


                        print(len("1) KRXKEN                     196.1 UD"))
                        print(len(f"\n{Place}) {player[0]} {playertp}\n"))
                        Message.append(f"\n{Place}) {player[0]} {playertp}\n")

                        Place += 1
            Message = "".join(Message)
            print(Message)

            break


LeaderboardTest(837062503741390850)