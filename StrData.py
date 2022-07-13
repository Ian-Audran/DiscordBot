
Leaderboard = """
```json
        "SERVER LEADERBOARD"

      ꧁༺☠༒"LES UD"༒☠༻꧂
  
1) KRXKEN                     196.1 UD
2) Adraes                     105.6 UD
3) Fast                       84.00 UD
4) Alex ♥                     40.00 UD

      ꧁༺☠༒"LES DE"༒☠༻꧂

5) Logpos                     100.0 DE
6) SharkDax                   17.65 DE
7) Jermdr                     3.007 DE
  
      ꧁༺☠༒"LES N"༒☠༻꧂

8)  Lety                      115.4 N
9)  Nono_tlz                  32.48 N
10) 7K_Crxzy                  3.102 N
11) Shadow_ninja              1.000 N

      ꧁༺☠༒"LES OC"༒☠༻꧂

12) Diabla                    407.3 oc

      ꧁༺☠༒"LES SP"༒☠༻꧂

13) MdrCclol                  1.261 SP

      ꧁༺☠༒"LES SX"༒☠༻꧂

14) Legeekeryt                56.76 SX
15) T_seag                    10.01 SX

      ꧁༺☠༒"LES QN"༒☠༻꧂

16) legamerarcois             914.1 Qn

      ꧁༺☠༒"LES QD"༒☠༻꧂
      
17) hello25534                125.8 Qd
18) yahyapraa                 52.70 Qd
19) hello25534                15.46 Qd

      ꧁༺☠༒"LES T"༒☠༻꧂

20) ypsoka                    114.5 T

      ꧁༺☠༒"LES M"༒☠༻꧂

21) MadaPsy972                6.768 M

     ꧁༺☠༒"LE NOOB"༒☠༻꧂

22) Tinoob                    0
```
"""

#\n\n***{prefix}command***\nexplanation
#to insert before the last "\n\n"

def HelpMessage(prefix):
  HelpMessage=f"""
  "**Commands:**"\n\n||###########################||\n\n***{prefix}setup*** :\nTo start using the bot on the server.\n\n||###########################||\n\n**Once setup done:**\n\n***{prefix}help***\nGet the list of the commands.\n\n***{prefix}setprefix (prefix)***\nChange the server's prefix.\n\n***{prefix}FULLBOTRESET***\nIf you want the bot to completely reset and delete all data from your server(If you didnt start by the "{prefix}setup" a reset is needed).\n\n***{prefix}user (discord mention or id) (TotalPower) (Rank)***\nTo give a player the roles and add him to leaderboard.\n\n***{prefix}link (discord id or mention) (Roblox Username)***\nTo link the roblox's username and discord username(is needed for leaderboard and the "{prefix}user" command)\n\n***{prefix}hello***\nsimilar to the ping command, the bot will just answer with "hello"\n\n***{prefix}set_ranks_roles (Fighter role) (Shinobi role) (Pirate role) (Ghoul role) (Hero role) (Reaper role) (Saiyan role) (Sin role) (Magi role) (Akuma role) (Yonko role) (Gorosei role) (Otsutsuki role) (Pirate King role) (Kishin role) (Angel role) (Demon King role)***\n*This command is to set the ranks roles*\n\n***{prefix}set_tp_roles (k role) (m role) (b role) (t role) (qd role) (qn role) (sx role) (sp role) (oc role) (n role) (de role) (ud role) (dd role)***\n*This command is to set the TotalPower roles*\n\n*Note that the parentheses are just there to seperate words and are not to be written in the actual commands*
  """
  return(HelpMessage)