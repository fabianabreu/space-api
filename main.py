import json
import os
import requests



def people_in_space():
  url = "http://api.open-notify.org/astros.json"
  response = requests.get(url)
  parsed = response.json()
  print(json.dumps(parsed, sort_keys=True, indent = 4))
  input("Press enter to return to menu...")
  os.system("clear")

def get_picture_of_the_day():
  pass

def main():
  
  while True:
    print()
    print("MENU:")
    print("1. View Astronauts in Space")
    print("2. View NASA's Pictures of the Day")
    print("3. Exit")
    choice = input("Please choose an option: ")
    os.system("clear")

    if choice == "1":
      people_in_space()
    elif choice == "2":
      get_picture_of_the_day()
    elif choice == "3":
      break
    else:
      print("Invalid choice.")
      print()

if __name__=="__main__":
  main()
      