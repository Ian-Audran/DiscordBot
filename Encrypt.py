import os
from cryptography.fernet import Fernet

def SaveData(data):
  #Encoding
  #data = json.dumps(data)
  encoded = data.encode()
  #Encrypting
  f = Fernet("4jQ01XKo0KKRzKi_mkAApqT853PNZ3XuEzlbxamUBG8=")
  encrypted = f.encrypt(encoded)
  #Save Encrypted To File
  with open('data.txt', 'wb') as f:
    f.write(encrypted)

def GetJsonData():
  with open('data.txt', "rb") as f:
    in_data = f.read()
  f2 = Fernet("4jQ01XKo0KKRzKi_mkAApqT853PNZ3XuEzlbxamUBG8=")
  JsonData = f2.decrypt(in_data).decode()
  return(str(JsonData))