from fetch_weather import fetch_weather
from display_weather import display_weather

def main():    
    while True:
        data = fetch_weather()
        if data:
            display_weather(data)
        a=input("Check another city?(y/n):")
        if a=="y":
            continue
        elif a=="n":
            print("Goodbye.")
            break
           
if __name__ == "__main__":
    main()