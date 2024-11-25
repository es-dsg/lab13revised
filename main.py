'''
DEVELOPER: julia de guzman
COLLABORATORS: <anyone you worked with or who helped you>
DATE:11/24/2024
'''

"""
To organize different species that are affected by Climate Change. The most fundamental part of inheritance is to be able to reuse attributes and methods that are share among different groups. For example there are many different mammals species. We are looking at two main species affected by Climate Change, polar bears and snow leopards.
"""

##### IMPORTS #####
from mammal import *
from polarbear import *
from snowleopard import *

##### FUNCTIONS #####
# create your main definition
def main():
  mammalObject = Mammal("eukaryota", "Animalia", "chordata", "mammalia")
  print(mammalObject)

  polarBearObject = PolarBear("eukaryota", "Animalia", "chordata", "mammalia", "polarbear")
  print(polarBearObject)
  
  snowLeopardObject = SnowLeopard("eukaryota", "Animalia", "chordata", "mammalia", "snowLeopard")
  print(snowLeopardObject)
  
  # leave this part as it is
  print("Climate change extreme weather events not only affect us economically, air quality health, and the destruction of cities by tornados, wildfires, hurricanes; we never think about how is affecting other species we share this world with.\n")
  print("Nikhil Advani conducted animal species assessments affected by Climate Change and determined their vulnerability, resilience, and status.\n")

  # create your menu to choose between Polar Bear, Snow Leopard and Exit follow by a submenu to choose between Vulnerability, Resilience, Status, and Exit
  while (True):
    choose = input("Choose animal under danger: a) Polar Bear, b)Snow Leopard, c) Exit\n")
    while (choose == "a"):
      choose2 = input("Choose animal's: a) Vulnerabiliy b) Resilience c) Status d) Exit\n")
      if choose2=="a":
        print(polarBearObject.get_vulnerability())
      elif choose2=="b":
        print(polarBearObject.get_resilience())
      elif choose2 =="c":
        print(polarBearObject.get_status())
      elif choose2=="d":
        break
    while choose == "b":
      choose2 = input("Choose animal's: a) Vulnerabiliy b) Resilience c) Status d) Exit\n")
      if choose2=="a":
        print(snowLeopardObject.get_vulnerability())
      elif choose2=="b":
        print(snowLeopardObject.get_resilience())
      elif choose2 =="c":
        print(snowLeopardObject.get_status())
      elif choose2=="d":
        break
    if choose == "c":
      print("Goodbye!")
      break

##### MAIN PROGRAM #####    
if __name__ == '__main__':
  main()

