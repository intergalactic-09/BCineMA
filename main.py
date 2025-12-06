import time

def l_of_movies():
    try:
        movies = open("csv.py")
        for film in movies:
             print(film[0])
    except:
         print('Files does not exist')


def get_genre():
    try:
        movies = open("csv.py")
        user = input("What genre are you looking for?: ")
        for genre in movies:
             genre = genre.rstrip()
             genre = genre.split(",")
             print(genre[0], genre[1])
    except:
         print('Files does not exist')  

def get_title():
    try:
        movies = open("csv.py")
        user = input(" Which movie title are you looking for?: ")
        for title in movies:
             title = title.rstrip()
             title = title.split(",")
             print(title[0], title[1])
    except:
         print('Files does not exist')

def get_actor():
    try:
        movies = open("csv.py")
        user = input(" Which actor are you looking for?: ")
        for actor in movies:
             actor = actor.rstrip()
             actor = actor.split(",")
             print(actor[0], actor[1])
    except:
         print('Files does not exist')


def get_by_genre():
        pass 


def get_by_title():
        pass


def get_by_actor():
        pass



def display_movies():
        pass

def main_menu():
    print("Main Menu")
    time.sleep(2)
    print("Welcome to BCineMA!: ")
    time.sleep(1.5)
    print("We offer you selections of movies, and sort them based on three factors.")
    time.sleep(1.2)
    print("That you can choose from ")
    time.sleep(1.5)
    print("Based on their titles, actors, and genres.")
    time.sleep(2)

    while True:
        print("1. Choose based by Genre: ")
        print("2. Choose based by Title: ")
        print("3. Choose based on Actors: ")
        print("4. Exit ")
        try:
            opt = int(input("Type the number to start search for: "))
            if (opt == 1):
                print(get_genre())
            elif(opt == 2):
                print(get_title())
            elif(opt == 3):
                print(get_actor())
            elif(opt == 4):
                print("Alrighy then, bye!")
                break
            else:
                print("Not in the list of options")
                break
        except:
            print("Place the number to work.")
            break

 

    

    