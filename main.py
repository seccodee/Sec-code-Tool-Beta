import os, sys
import readline
import requests
import json
print("""

█▀ █▀▀ █▀▀ ▄▄ █▀▀ █▀█ █▀▄ █▀▀ ▀░▄▀
▄█ ██▄ █▄▄ ░░ █▄▄ █▄█ █▄▀ ██▄ ▄▀░▄
SEC'S TOOL BETA
""")

"""
This Program is for ethical purposes only i'm not responsible for any damage
or any kind such as illegal use
"""

print("""#---i will add new things soon---#
1 ---Get Proxies""")

tool = input("enter a choice:")

if tool == "1":
  f = open("proxies.txt", "r")
  print(f.read())
  

else:
  print("invalid") 
