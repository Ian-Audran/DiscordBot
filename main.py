##################################################

#Created by Galawa
#Discord: Galawa#6994
#If you use this program or part of it please Give credits

##################################################

import time
import Keep_Alive
import discord
import discord.utils
import os
import flask
#from cryptography.fernet import Fernet
import json
import Encrypt
import StrData
from importlib import reload
import DictRepair


client = discord.Client()
prefix = "L!"

#Encrypt.SaveData(JsonData)

data = json.loads(Encrypt.GetJsonData())
#for i in range(len(data['Servers'])):
#  dic = DictRepair.OrderedDict(data['Servers'][i]['Roles']['Ranks'])
#  dic.KeyRename("overloard","overlord")
#  data['Servers'][i]['Roles']['Ranks'] = dic
  #print(dic)
    
print(json.dumps(data, indent=2))
#data = json.dumps(data)
#Encrypt.SaveData(data)

def BotSend(message, description):
  embed = discord.Embed(
    #title = f'{title}',
    description = f'{description}',
    colour = 0x000000
  )
  client.loop.create_task(message.channel.send(embed=embed))


def IdReplacement(word):
  word = word.replace("<", "")
  word = word.replace("@", "")
  word = word.replace("&", "")
  word = word.replace("!", "")
  word = word.replace(">", "")
  return(int(word))

def GetPrefix(guild_id):
  data = json.loads(Encrypt.GetJsonData())
  for i in range(len(data['Servers'])):
    if data['Servers'][i]['guild_id'] == guild_id:
      prefix = data['Servers'][i]['prefix']
      return(prefix)
  return("L!")

def SavePrefix(guild_id, prefix):
  data = json.loads(Encrypt.GetJsonData())
  for i in range(len(data['Servers'])):
    if str(data['Servers'][i]['guild_id']) == str(guild_id):
      data['Servers'][i]['prefix'] = prefix
      data = json.dumps(data)
      Encrypt.SaveData(data)
      return()
  to_append = {"guild_id": guild_id, "prefix": prefix}
  data['Servers'].append(to_append)
  data = json.dumps(data)
  Encrypt.SaveData(data)

def SaveUser(guild_id, disc_id, tp, rank):
  data = json.loads(Encrypt.GetJsonData())
  for i in range(len(data['Servers'])):
    if str(data['Servers'][i]['guild_id']) == str(guild_id):
      for p in range(len(data['Servers'][i]['Players'])):
        if str(data['Servers'][i]['Players'][p]['disc_id']) == str(disc_id):
          old_rank = data['Servers'][i]['Players'][p]['rank']
          old_tp = data['Servers'][i]['Players'][p]['tp']
          data['Servers'][i]['Players'][p]['tp'] = tp
          data['Servers'][i]['Players'][p]['rank'] = rank
          data = json.dumps(data)
          Encrypt.SaveData(data)
          if old_rank == None or old_rank == "":
            old_rank = "Nothing"
          if old_tp == None or old_tp == "":
            old_tp = "Nothing"
          return(True, old_rank, old_tp)
      return(False, "", "")
      
def GetKey(i, passed_value):
  data = json.loads(Encrypt.GetJsonData())
  for key, value in data['Servers'][i]['Roles']['TpIndex'].items():
    if value == passed_value:
      TP = f"{key.upper()}"
      return(TP)

def TpFormat(ToFormat):
  EndTp = list(ToFormat)
  if len(EndTp) > 1:
    EndTp = str(EndTp[0].upper())+str(EndTp[1].lower())
    return(EndTp)
  return(ToFormat)

def UpdateUser(guild_id, message, Member, Tp, Rank, old_rank, old_tp):
  data = json.loads(Encrypt.GetJsonData())
  formated_tp = []
  formated_oldtp = []
  for i in range(len(data['Servers'])):
    if str(data['Servers'][i]['guild_id']) == str(guild_id):
      for c in Tp:
        if any(map(str.isdigit, c)) or c == "." or c == ",":
          pass
        else:
          formated_tp.append(c)
      Tp = "".join(formated_tp)
      for c in old_tp:
        if any(map(str.isdigit, c)) or c == "." or c == ",":
          pass
        else:
          formated_oldtp.append(c)
      old_tp = "".join(formated_oldtp)
      raw_tprole = data['Servers'][i]['Roles']['TpIndex'][Tp]
      try:
        raw_tprole2 = data['Servers'][i]['Roles']['TpIndex'][old_tp]
        old_roles = True
      except KeyError:
        old_roles = False
      raw_rankrole = data['Servers'][i]['Roles']['Ranks'][Rank]
      try:
        raw_rankrole2 = data['Servers'][i]['Roles']['Ranks'][old_rank]
      except KeyError:
        old_roles = False

      tp_role = IdReplacement(raw_tprole)
      rank_role = IdReplacement(raw_rankrole)
      tp_role = message.guild.get_role(tp_role)
      rank_role = message.guild.get_role(rank_role)
      
      if old_roles:
        tp_role2 = IdReplacement(raw_tprole2)
        rank_role2 = IdReplacement(raw_rankrole2)
        rank_role2 = message.guild.get_role(rank_role2) 
        tp_role2 = message.guild.get_role(tp_role2)
      else:
        rank_role2 = "Nothing"
        tp_role2 = "Nothing"

      if rank_role != rank_role2 and old_roles:
        client.loop.create_task(Member.remove_roles(rank_role2))  
      time.sleep(0.07)
      client.loop.create_task(Member.add_roles(rank_role))
      time.sleep(0.07)
      if tp_role != tp_role2 and old_roles:
        client.loop.create_task(Member.remove_roles(tp_role2))  
      time.sleep(0.07)
      client.loop.create_task(Member.add_roles(tp_role))
      
      if data['Servers'][i]['ChangeUsername'] == True:
        new_tp = GetKey(i, raw_tprole)
        NewNick = Member.nick
        if old_tp != "Nothing":
          NewNick = NewNick.replace(f"[{old_tp.upper()}] ", "")
          NewNick = NewNick.replace(f"[{old_tp.lower()}] ", "")
          NewNick = NewNick.replace(f"[{TpFormat(old_tp)}] ", "")

        NewNick = NewNick.replace("b!bind ", "")
        NewNick = list(NewNick)
        NewNick.insert(0, f"[{TpFormat(new_tp)}] ")
        NewNick = "".join(NewNick) 
        time.sleep(0.1)
        if len(NewNick) < 33:
          client.loop.create_task(Member.edit(nick=NewNick))
        else:
          return False
      return True

def LinkUser(guild_id, disc_id, username):
  data = json.loads(Encrypt.GetJsonData())
  for i in range(len(data['Servers'])):
    if data['Servers'][i]['guild_id'] == guild_id:
      for p in range(len(data['Servers'][i]['Players'])):
        if str(data['Servers'][i]['Players'][p]['disc_id']) == str(disc_id):
          data['Servers'][i]['Players'][p]['username'] = username
          return(True)
          
      data['Servers'][i]['Players'].append({"username": username, "tp": "", "rank": "", "disc_id": disc_id})
      data = json.dumps(data)
      Encrypt.SaveData(data)
      return(False)

def setup(guild_id):
  data = json.loads(Encrypt.GetJsonData())
  for i in range(len(data['Servers'])):
    if data['Servers'][i]['guild_id'] == guild_id:
      return(False)
  to_append = {"guild_id": guild_id, "prefix": "L!", "Players": [{"username": "", "tp": "", "rank": "", "disc_id": ""}], "Roles": {"Ranks": {"fighter": "", "shinobi": "", "pirate": "", "ghoul": "", "hero": "", "reaper": "", "saiyan": "", "sin": "", "magi": "", "akuma": "", "yonko": "", "gorosei": "", "overloard": "", "hokage": "", "kaioshin": "", "sage": "", "espada": "", "shinigami": "", "hashira": "", "hakaishin": "", "otsutsuki": "", "pirateking": "", "kishin": "", "angel": "", "demonking": ""}, "TpIndex": { "k": "", "m": "", "b": "", "t": "", "qd": "", "qn": "", "sx": "", "sp": "", "oc": "", "n": "", "de": "", "ud": "", "dd": ""}}}
  data['Servers'].append(to_append)
  data = json.dumps(data)
  Encrypt.SaveData(data)
  return(True)

def FULLRESET(guild_id):
  data = json.loads(Encrypt.GetJsonData())
  for i in range(len(data['Servers'])):
    if data['Servers'][i]['guild_id'] == guild_id:
      data['Servers'].remove(data['Servers'][i])
      data = json.dumps(data)
      Encrypt.SaveData(data)
      return(True)

def EmbedCreate(title, description, color):
  embed = discord.Embed(
    title = f'{title}',
    description = f'{description}',
    colour = color
  )
  return(embed)

def Reload():
  reload(StrData)
  return(True)

def SetRankRoles(guild_id, msg_var):
  data = json.loads(Encrypt.GetJsonData())
  for i in range(len(data['Servers'])):
    if data['Servers'][i]['guild_id'] == guild_id:
      index = 0
      for p in data['Servers'][i]['Roles']['Ranks']:
        index = index+1
        data['Servers'][i]['Roles']['Ranks'][p] = msg_var[index]
  data = json.dumps(data)
  Encrypt.SaveData(data)
  return(True)

def SetTpRoles(guild_id, msg_var):
  data = json.loads(Encrypt.GetJsonData())
  for i in range(len(data['Servers'])):
    if data['Servers'][i]['guild_id'] == guild_id:
      index = 0
      for p in data['Servers'][i]['Roles']['TpIndex']:
        index = index+1
        data['Servers'][i]['Roles']['TpIndex'][p] = msg_var[index]
  data = json.dumps(data)
  Encrypt.SaveData(data)
  return(True)

def LeaderBoardEmbed(message):
  guild_id = message.guild.id
  data = json.loads(Encrypt.GetJsonData())
  formated_tp = []
  formated_oldtp = []
  for i in range(len(data['Servers'])):
    if data['Servers'][i]['guild_id'] == guild_id:
      for c in Tp:
        if any(map(str.isdigit, c)) or c == "." or c == ",":
          pass
        else:
          formated_tp.append(c)
      Tp = "".join(formated_tp)
      for c in old_tp:
        if any(map(str.isdigit, c)) or c == "." or c == ",":
          pass
        else:
          formated_oldtp.append(c)
      old_tp = "".join(formated_oldtp)
      for p in range(len(data['Servers'][i]['Players'])):
        print(data['Servers'][i]['Players'][p]['username'])
        print(data['Servers'][i]['Players'][p]['tp'])
      break
  title = ""
  text = StrData.Leaderboard
  client.loop.create_task(message.channel.send(embed=EmbedCreate(title, f"{text}", 0x008080)))

############################################################################################################
#Events#####################################################################################################
############################################################################################################

@client.event
async def on_ready():
  print("Bot has logged in as {0.user}".format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.author.bot:
    return
  guild_id = message.guild.id
  admin = message.author.guild_permissions.administrator
  can_manage_roles = message.author.guild_permissions.manage_roles
  prefix = GetPrefix(guild_id) 

  if str(message.author.id) == str(os.environ['CREATORID']):
    if message.content.startswith(f"{prefix}RELOAD"):
      if Reload():
        await message.channel.send("LIB RELOADED")    

#Help#####################################################################

  if message.content.startswith(f"{prefix}help"):
    await message.channel.send(embed = EmbedCreate("**Help**", StrData.HelpMessage(prefix), 0xb700ff))    

  if message.content.startswith(f"{prefix}set"):
    if admin:
      pass
    else:
      await message.channel.send("You do not have the permission to use that command")
    
  if admin:  

#ADM setprefix#####################################################################
 
    if message.content.startswith(f"{prefix}setprefix"):
      content = message.content.split(" ")
      if len(content) > 1:
        newprefix = content[-1]
        print(newprefix)
        SavePrefix(guild_id, newprefix)
        await message.channel.send(f"Prefix has been set to '{newprefix}'")
      else:
        await message.channel.send(f"The corect command is : \n***{prefix}setprefix (prefix)***\n\n*Note that the parentheses are just there to seperate words and are not to be written in the actual command*")

#ADM setup#####################################################################

    if message.content.startswith(f"{prefix}setup"):
      if setup(guild_id):
        await message.channel.send("You can now use the bot !!")
      else:
        await message.channel.send(f"This server is already setup. If you want to reset the Bot (that includes all the data this bot has from this server) use the command:\n{prefix}FULLBOTRESET")

#ADM set_ranks_roles#####################################################################

    if message.content.startswith(f"{prefix}set_ranks_roles"):
      msg_var = message.content.split(" ")
      if len(msg_var) > 25:
        if SetRankRoles(guild_id, msg_var):
          await message.channel.send("Rank Roles have been set")
      else:
        await message.channel.send(f"The corect command is : \n***{prefix}set_ranks_roles (Fighter role) (Shinobi role) (Pirate role) (Ghoul role) (Hero role) (Reaper role) (Saiyan role) (Sin role) (Magi role) (Akuma role) (Yonko role) (Gorosei role) (Otsutsuki role) (Pirate King role) (Kishin role) (Angel role) (Demon King role)***\n\n*Note that the parentheses are just there to seperate words and are not to be written in the actual command*")

#ADM set_tp_roles#####################################################################

    if message.content.startswith(f"{prefix}set_tp_roles"):
      msg_var = message.content.split(" ")
      if len(msg_var) > 12:
        if SetTpRoles(guild_id, msg_var):
          await message.channel.send("TotalPower Roles have been set")  
      else:
        await message.channel.send(f"The corect command is : \n***{prefix}set_tp_roles (k role) (m role) (b role) (t role) (qd role) (qn role) (sx role) (sp role) (oc role) (n role) (de role) (ud role) (dd role)***\n\n*Note that the parentheses are just there to seperate words and are not to be written in the actual command*")

#ADM FULLBOTRESET#####################################################################

  if message.content.startswith(f"{prefix}FULLBOTRESET"):    
    if admin:
      if FULLRESET(guild_id):
        BotSend(message, "Data from this server has completely been deleted")
    else:
      BotSend(message, "You do not have the permission to use that command")

  if message.content.startswith(f"{prefix}leaderboardtest"):
    if admin:
      LeaderBoardEmbed(message)
      
#MANAGE ROLES user#####################################################################

  if message.content.startswith(f"{prefix}USER") or message.content.startswith(f"{prefix}user"):
    if can_manage_roles:
      #await message.channel.send(message.content)
      msg_var = message.content.split(" ")
      disc_user_var = msg_var[1]
      disc_user_var = disc_user_var.replace("!", "")
      disc_id_var = int(str(disc_user_var.replace("<@","")).replace(">", ""))
      #user_var = msg_var[2]
      tp_var = msg_var[2].lower()
      rank_var = msg_var[3].lower()
      member = await message.guild.fetch_member(disc_id_var)
      execution, old_rank, old_tp = SaveUser(guild_id, disc_id_var, tp_var, rank_var)
      if not execution:
        BotSend(message, f"Please link the user before adding his roles. Use the commmand :\n{prefix}link mention roblox_username")
      else:
        if UpdateUser(guild_id, message, member, tp_var, rank_var, old_rank, old_tp):
          BotSend(message, f"User has been set")
        else:
          BotSend(message, "Users roles have been set but nickname lengh has been reached")
        
    else:
      BotSend(message, 'You need the "manage_roles" permission to use that command')
      
#MANAGE ROLES link#####################################################################

  if message.content.startswith(f"{prefix}link"):
    if can_manage_roles:
      msg_var = message.content.split(" ")
      disc_user_var = msg_var[1]
      disc_user_var = disc_user_var.replace("!", "")
      disc_id_var = int(str(disc_user_var.replace("<@","")).replace(">", ""))
      rblx_user_var = msg_var[2]
      
      if LinkUser(guild_id, disc_id_var, rblx_user_var):
        await message.channel.send("Users Link has been modified")
      else:
        await message.channel.send("User has been linked")
    else:
      await message.channel.send('You need the "manage_roles" permission to use that command')

#hello#####################################################################

  if message.content.startswith(f"{prefix}hello"):
    if str(message.author.id) == str(os.environ['CREATORID']):
      await message.channel.send("Hello Master")
    else:
      await message.channel.send("hello")
  
  

Keep_Alive.keep_alive()
client.run(os.environ['TOKEN'])