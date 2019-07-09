# Creaate the dictiony

information = {
    "name": "Luis Sauceda",
    "age": "36",
    "hobby": [
        "Reading sci-fy books",
        "Drawing",
        "Attend rock gigs"
    ],
    "wakeUp":{
       "Monday": "10 a.m.", 
       "Saturday": "7 a.m.", 
       "Thursday": "7:35 a.m."
       }
    
}
print("Hi my name is " + f'{information["name"]}')
print("I have " + f'{len(information["hobby"])}' + " hobbies")
print("on Mondays I wake up at " + f'{information["wakeUp"]["Monday"]}')
print("My favorite hobby is " f'{information["hobby"][2]}') 