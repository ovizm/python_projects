#list of books

booklist = {
    "Me Before You": {"Genre": "Novel", "Author": "Jojo Moyes"},
    "Me After You":  {"Genre": "Novel", "Author": "Jojo Moyes"},
    "Still Me":  {"Genre": "Novel", "Author": "Jojo Moyes"},
    "Death Call": {"Genre": "Thriller", "Author": "Chris Carter"},
    "An Evil Mind" :  {"Genre": "Thriller", "Author": "Chris Carter"},
    "One By One": {"Genre": "Thriller", "Author": "Chris Carter"},
    "The Why Are You Here Cafe": {"Genre": "Novel", "Author": "John Strelecky"},
    "Life Safari": {"Genre": "Novel", "Author": "John Strelecky"},
    "The Big Five For Life": {"Genre": "Novel", "Author": "John Strelecky"},
    "The Return To The Why Cafe": {"Genre": "Novel", "Author": "John Strelecky"},
    "The Why Are You Here Cafe: A New Way Of Finding Meaning In Your Life And Your Work": {"Genre": "Novel", "Author": "John Strelecky"},
    }


#shelves by genre

shelves = {
    "shelf_1": {"Genre": "Novel", "Space": 5},
    "shelf_2": {"Genre": "Thriller", "Space": 5},
    }

#sort books by genre and fill up to five

while shelves["shelf_1"]["Space"] <=5 and shelves["shelf_2"]["Space"] <= 5:
    
    choice = input("Which book do you want to put into the shelves?: ").strip().title()

    if choice in booklist:
        
        if booklist[choice]["Genre"] == "Novel":
            print("This book belongs to shelf_1")
            shelves["shelf_1"]["Space"] = shelves["shelf_1"]["Space"]-1
            if shelves["shelf_1"]["Space"] == 0:
                print("This shelf is full. You cannot put any more books on shelf_1!")
                
        elif booklist[choice]["Genre"] == "Thriller":
            print("This book belongs to shelf_2")
            shelves["shelf_2"]["Space"] = shelves["shelf_2"]["Space"]-1
            if shelves["shelf_2"]["Space"] == 0:
                print("This shelf is full. You cannot put any more books on shelf_2!")
        else:
            print("We don't have a shelf for this genre!")

        del booklist[choice]
        
    else:
        print("We don't have this title in our booklist!")
    
