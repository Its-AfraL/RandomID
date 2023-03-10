import requests
from pystyle import *
import random
import os
import time
import datetime
from alive_progress import alive_bar
import time

os.system("title Random ID © v1.0.0   ^|  Created for legal purposes only")
os.system('cls')

def generate_min_infos(output_path, number):

    now = datetime.datetime.now()
    year = '{:02d}'.format(now.year)
    month = '{:02d}'.format(now.month)
    day = '{:02d}'.format(now.day)
    hour = '{:02d}'.format(now.hour)
    minute = '{:02d}'.format(now.minute)
    day_month_year_hour_minute = '{}-{}-{}-{}-{}'.format(
        year, month, day, hour, minute)
    
            
    output_file = open(f"output\\{output_path}" + ".txt", "a")
    output_file.write(f"\nID List generated at : {day_month_year_hour_minute}\n\n")
    
    print(Colors.light_red + "\n\n >>>  G" + Colors.reset + "enerating " + Colors.light_red + str(number) + Colors.reset + " fake ID in " + Colors.light_red + "output\\" + Colors.reset + str(output_path) + Colors.reset + ".txt\n\n")
    
    with alive_bar(int(number), bar='smooth') as bar:
        
        for i in range(int(number)): 
            bar()
            random_infos = requests.get("https://fakeid.vercel.app/api/Gender/random/NameSet/fr/Country/fr").json()
        
            output_file.write("Nom : " + random_infos["data"]["Name"] + "\n")
            output_file.write("Adresse complète : " + random_infos["data"]["Address"] + "\n")
            output_file.write("Age : " + random_infos["data"]["Details"]["Age"] + "\n")
            output_file.write("Date de naissance : " + random_infos["data"]["Details"]["Birthday"] + "\n\n")
    
    output_file.close()
    os.system("pause>nul")

def generate_max_infos(output_path, number):
    
    now = datetime.datetime.now()
    year = '{:02d}'.format(now.year)
    month = '{:02d}'.format(now.month)
    day = '{:02d}'.format(now.day)
    hour = '{:02d}'.format(now.hour)
    minute = '{:02d}'.format(now.minute)
    day_month_year_hour_minute = '{}-{}-{}-{}-{}'.format(
        year, month, day, hour, minute)
    
            
    output_file = open(f"output\\{output_path}" + ".txt", "a")
    output_file.write(f"\nID List generated at : {day_month_year_hour_minute}\n\n")
    
    print(Colors.light_red + "\n\n >>>  G" + Colors.reset + "enerating " + Colors.light_red + str(number) + Colors.reset + " fake ID in " + Colors.light_red + "output\\" + Colors.reset + str(output_path) + Colors.reset + ".txt\n\n")
    
    with alive_bar(int(number), bar='smooth') as bar:
        
        for i in range(int(number)): 
            bar()
            random_infos = requests.get("https://fakeid.vercel.app/api/Gender/random/NameSet/fr/Country/fr").json()
        
            output_file.write("Nom : " + random_infos["data"]["Name"] + "\n")
            output_file.write("Adresse complète : " + random_infos["data"]["Address"] + "\n")
            output_file.write("Age : " + random_infos["data"]["Details"]["Age"] + "\n")
            output_file.write("Date de naissance : " + random_infos["data"]["Details"]["Birthday"] + "\n")
            output_file.write("Signe astrologique : " + random_infos["data"]["Details"]["TropicalZodiac"] + "\n")
            output_file.write("Vehicule : " + random_infos["data"]["Details"]["Vehicle"] + "\n")
            output_file.write("Couleur preferee : " + random_infos["data"]["Details"]["FavoriteColor"] + "\n")
            output_file.write("Groupe sanguin : " + random_infos["data"]["Details"]["BloodType"] + "\n")
            output_file.write("Poids : " + random_infos["data"]["Details"]["Weight"] + "\n")
            output_file.write("Taille : " + random_infos["data"]["Details"]["Height"] + "\n")
            output_file.write("Métier : " + random_infos["data"]["Details"]["Occupation"] + "\n")
            try:
                output_file.write("Visa : " + random_infos["data"]["Details"]["Visa"] + "\n")
            except:
                output_file.write("Mastercard : " + random_infos["data"]["Details"]["MasterCard"] + "\n")
                
            output_file.write("Date d'expiration : " + random_infos["data"]["Details"]["Expires"] + "\n")
            
            try:
                output_file.write("CVV2 : " + random_infos["data"]["Details"]["CVV2"] + "\n\n")
            except:
                output_file.write("CVC2 : " + random_infos["data"]["Details"]["CVC2"] + "\n\n")
                
    output_file.close()
    os.system("pause>nul")
    
    
logo = """
     
                                                              
 _____                    _                    _______  _____  
(_____)        _         (_)                  (_______)(_____) 
(_)__(_) ____ (_)__    __(_)  ___    __   __     (_)   (_)  (_)
(_____) (____)(____)  (____) (___)  (__)_(__)    (_)   (_)  (_)
( ) ( )( )_( )(_) (_)(_)_(_)(_)_(_)(_) (_) (_) __(_)__ (_)__(_)
(_)  (_)(__)_)(_) (_) (____) (___) (_) (_) (_)(_______)(_____) 
                                                               
                                                
"""

def interface():

    os.system('cls')

    print(Colorate.Vertical(Colors.white_to_red, Center.XCenter(logo)))
    print(Center.XCenter(Colors.light_red + "                                                |" + Colors.white + " Created by AfraL" + Colors.light_red + " |     "))
                     
    print("\n")
    print("\n")

    print(Colors.light_red + "1) " + Colors.white + "Generate an ID list with the minimum of informations")
    print(Colors.light_red + "2) " + Colors.white + "Generate an ID list with the maximum of informations")

    choice = input(Colors.light_red + "\nP" + Colors.white + "lease make a choice " + Colors.light_red + "> ")

    try:
        choice = int(choice)
    except:
        print("\n\n /!\\ Please make sure to enter a valid number"+ Colors.reset)
        time.sleep(2)
        interface()
    
    if choice == 1:
        number = input(Colors.light_red + "\nE" + Colors.white + "nter the number of ID to generate " + Colors.light_red + "> ")
        try:
            number = int(number)
        except:
            print("\n\n /!\\ Please make sure to enter a valid number"+ Colors.reset)
            time.sleep(2)
            interface()
        
        output_name = input(Colors.light_red + "E" + Colors.white + "nter output file name (.text file) " + Colors.light_red + "> ")
        generate_min_infos(output_name, number)
        

    elif choice == 2:
        number = input(Colors.light_red + "\nE" + Colors.white + "nter the number of ID to generate " + Colors.light_red + "> ")
        try:
            number = int(number)
        except:
            print("\n\n /!\\ Please make sure to enter a valid number"+ Colors.reset)
            time.sleep(2)
            interface()
        
        output_name = input(Colors.light_red + "E" + Colors.white + "nter output file name (.text file) " + Colors.light_red + "> ")
        generate_max_infos(output_name, number)
    
    else:
        print("\n\n /!\\ Please make sure to enter a valid number"+ Colors.reset)
        time.sleep(2)
        interface()
        
interface()