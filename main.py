"""
COMP-305 Team Fortran Final Project
Professor: Anuzen
Names: Frank Veldhuizen, Olivia Kallmeyer, Brayan Mendoza, Chris Redd
Purpose: Create terminal based operational version of our Winter Olympic results 
application

1/ begins with definitions of the three parent classes 
2/ defines the many sub-event derived child classes
3/ declares the driver portion of the program

****Notice*****
We have decided to use a single file, although not best practice, for the
implementation of the classes since we ran 
into several issues with running out of seperate files.

"""

#1/ Defines the three parent classes: AlpineSkiing, Snowboarding, and IceHockey

class AlpineSkiing(object):
  
  def __init__(self) -> None:
    self.mgold = mgold
    self.msilver = msilver
    self.mbronze = mbronze
    self.wgold = wgold
    self.wsilver = wsilver
    self.wbronze = wbronze
    
  def __str__(self)->str:
    return f"\nresults... \n\n ************ Mens ************  \n\n medal | country | name | time | \n\n GOLD: {self.mgold} \n SILVER: {self.msilver} \n BRONZE: {self.mbronze} \n\n ************ Womens ************ \n\n medal | country | name | time | \n\n GOLD: {self.wgold} \n SILVER: {self.wsilver} \n BRONZE: {self.wbronze} \n"


class Snowboarding(object):
  def __init__(self) -> None:
    self.mgold = mgold
    self.msilver = msilver
    self.mbronze = mbronze
    self.wgold = wgold
    self.wsilver = wsilver
    self.wbronze = wbronze

  def __str__(self)->str:
    return f"\nresults... \n\n ************ Mens ************  \n\n medal | country | name | \n\n GOLD: {self.mgold} \n SILVER: {self.msilver} \n BRONZE: {self.mbronze} \n\n ************ Womens ************ \n\n medal | country | name | \n\n GOLD: {self.wgold} \n SILVER: {self.wsilver} \n BRONZE: {self.wbronze} \n"


class IceHockey(object):

  def __init__(self) -> None:
    self.mgold = "Finland"
    self.msilver = "Russian Olympic Committee"
    self.mbronze = "Slovakia"
    self.wgold = "Canada"
    self.wsilver = "United States of America"
    self.wbronze = "Finland" 
    
  def __str__(self)->str:
    return f"Ice Hockey \nresults... \n\n ************ Mens ************  \n\n medal | country |\n\n GOLD: {self.mgold} \n SILVER: {self.msilver} \n BRONZE: {self.mbronze} \n\n ************ Womens ************ \n\n medal | country | \n\n GOLD: {self.wgold} \n SILVER: {self.wsilver} \n BRONZE: {self.wbronze} \n"


#2/ Below defines the many child classes that represent sub events of the main sports

class Slalom(AlpineSkiing):
  def __init__(self) -> None:
    self.mgold = "FRA, Clement Noel, 1:44.09"
    self.msilver = "AUT, Johannes Strolz, 1:44.70"
    self.mbronze = "NOR, Sebastian Foss-Solevaag, 1:44.79"
    self.wgold = "SVK, Petra Vlhova, 1:44.98"
    self.wsilver = "AUT, Katharina Liensberger, 1:45.06"
    self.wbronze = "SUI, Wendy Holdener, 1:45.10"

  def __str__(self)->str:
    return "Alpine Skiing: Slalom" + super().__str__()


class SuperG(AlpineSkiing):
  def __init__(self) -> None:
    self.mgold = "AUT, Matthias Mayer, 1:19.94"
    self.msilver = "USA, Ryan Cochran-Siegle, 1:19.98"
    self.mbronze = "NOR, Aleksander Aamondt Kilde, 1:20.36"
    self.wgold = "SUI, Lara Gut-Behrami, 1:13.51"
    self.wsilver = "AUT, Mirjam Puchner, 1:13.73"
    self.wbronze = "SUI, Michelle Gisin, 1:13.81"

  def __str__(self)->str:
    return "Alpine Skiing: Super Giant Slalom" + super().__str__()
    

class GSlalom(AlpineSkiing):
  
  def __init__(self) -> None:
    self.mgold = "SUI, Marco Odermatt, 2:09.35"
    self.msilver = "SLO, Zan Kranjec, 2:09.54"
    self.mbronze = "FRA, Mathieu Faivre, 2:10.69"
  
    self.wgold = "SWE, Sara Hector, 1:55.69"
    self.wsilver = "ITA, Federica Bridgone, 1:55.97"
    self.wbronze = "SUI, Lara Gut-Behrami, 1:56.41"
   

  def __str__(self)->str:
    return "Alpine Skiing: Giant Slalom" + super().__str__()


class Downhill(AlpineSkiing):
  def __init__(self) -> None:
  
    self.mgold = "SUI, Beat Feuz, 1:42.69"
    self.msilver = "FRA, Johan Clarey, 1:42.79"
    self.mbronze = "AUT, Mattias Mayer, 1:42.85"
    self.wgold = "SUI, Corinne Suter, 1:31.87"
    self.wsilver = "ITA, Sofia Goggia, 1:32.03"
    self.wbronze = "ITA, Nadia Delago, 1:32.44"

  def __str__(self)->str:
    
    return "Alpine Skiing: Downhill" + super().__str__()


class BigAir(Snowboarding):
    def __init__(self) -> None:
      self.mgold = "CHN, Yiming Su"
      self.msilver = "NOR, Mons Roisland"
      self.mbronze = "CAN, Max Parrot"
      self.wgold = "AUT, Anna Gasser"
      self.wsilver = "NZL, Zoi Sadowski Synnott"
      self.wbronze = "JPN, Kokomo Murase"
      
    def __str__(self)->str:
      return "Snowboarding: Big Air" + super().__str__()


class Cross(Snowboarding):
  def __init__(self) -> None:
    self.mgold = "AUT, Alessandro Haemmerle"
    self.msilver = "CAN, Eliot Grondin"
    self.mbronze = "ITA, Omar Visintin"
    self.wgold = "USA, Lindsey Jacobellis"
    self.wsilver = "FRA, Chloe Treseuch"
    self.wbronze = "CAN, Meryeta Odine"
    
  def __str__(self)->str:
    return "Snowboarding: Cross" + super().__str__()
    

class HalfPipe(Snowboarding):
  def __init__(self) -> None:
    self.mgold = "JPN, Ayumu Hirano"
    self.msilver = "AUS, Scotty James"
    self.mbronze = "SUI, Jan Scherrer"
    self.wgold = "USA, Chloe Kim"
    self.wsilver = "ESP, Queralt Castellet"
    self.wbronze = "JPN, Sena Tomita" 

  def __str__(self)->str:
    return "Snowboarding: Halfpipe" + super().__str__()


class ParallelGS(Snowboarding):
  def __init__(self) -> None:
    self.mgold = "AUT, Benjamin Karl"
    self.msilver = "SLO, Tim Mastnak"
    self.mbronze = "ROC, Vic Wild"
    self.wgold = "CZE, Ester Ledecka"
    self.wsilver = "AUT, Daniela Ubling"
    self.wbronze = "SLO, Gloria Kotnik"

  def __str__(self)->str:
    return "Snowboarding: Parallel Giant Slalom" + super().__str__()


class SlopeStyle(Snowboarding):
  def __init__(self) -> None:
    self.mgold = "CAN, Max Parrot"
    self.msilver = "CHN, Yiming SU"
    self.mbronze = "CAN, Mark Mcmorris"
    self.wgold = "NZL, Zoi Sadowski"
    self.wsilver = "USA, Julia Marino"
    self.wbronze = "AUS, Tess Coady"
    
  def __str__(self)->str:
    return "Snowboarding: Slope Style" + super().__str__()


#3/ This marks the beginning of the driver portion of the program


def createOutput(sport, event)->None: #generates objects based on user input

  #handles the special case for icehockey having no events
  if sport == "B" and event == " ":
    obj = IceHockey()

  #handles the case of an event under alpine skiing
  if sport == "A":
    if event == "A":
      obj = Slalom()
    elif event == "B":
      obj = Downhill()
    elif event == "C":
      obj = SuperG()
    elif event == "D":
      obj = GSlalom()

  #handles the case of an event under snowboarding
  if sport == "C":
    if event == "A":
      obj = ParallelGS()
    elif event == "B":
      obj = BigAir()
    elif event == "C":
      obj = Cross()
    elif event == "D":
      obj = HalfPipe()
    elif event == "E":
      obj = SlopeStyle()
  print("============================================")
  print(obj)#prints out string representation of the a
  print("============================================")



def main()->None:
  print("Select desired WINTER OLYMPIC sport by inputing a letter A,B, or C:")
  print("Alpine Skiing -> (A)")
  print("Ice Hockey -> (B)")
  print("Snowboarding -> (C)")
  sport = input().upper()

  if sport == "A":
    print("Select desired alpine skiing event by inputing a letter A-D:")
    print("Slalom -> (A)")
    print("Downhill -> (B)")
    print("Super-G -> (C)")
    print("Giant Slalom -> (D)")
    event = input().upper()
  
  elif sport == "B":
    event = " "

  elif sport =="C":
    print("Select desired snowboarding event by inputing letter A-E:")
    print("Parallel Giant Slalom -> (A)")
    print("Big Air -> (B)")
    print("Cross -> (C)")
    print("Halfpipe -> (D)")
    print("Slope Style -> (E)")
    event = input().upper()
  else:
    print("********ERROR, incorrect input********")

  #creates an object and prints out details 
  createOutput(sport, event)


if __name__ == "__main__":
    again = "Y"
    while again == "Y":
        main()
        print("Enter (Y/y) to run again, or (N/n) to stop")
        again = input().upper()