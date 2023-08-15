"""
projekt_1.py: první projekt do  Engeto Online  Python Akademie
  
author: Igor Taraban
e-mail: taraban@centrum.cz
discord: igort2408     - PROSIM  odpoved  poslat na e-mail ! Děkuji moc ! 
                            DISCORD ... moc  nefunguji ! Děkuji moc ! 
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

pair_user={input("Enter your name, please: "):input("Enter your password, please:  ")}
pair_user={"bob":"123","ann":"pass123", "mike":"password123", "liz":"pass123"}
control = all((pair_user.get(key) ==  value for key, value in pair_user.items()))

if control == False :
    print("$ python project1.py")
    print(f"username:",*pair_user.keys())
    print(f"password:",*pair_user.values())
    print("unregistered  user, terminating  the  program ..." )
    
else:
    print("$ python project1.py","\n"f"username: ", *pair_user.keys(), "\n"f"password: ",   *pair_user.values())
    print("------------------------------------------")
    print(f"Welcome to the app,", *pair_user.keys(),"\nWe have 3 texts to be analyzed.")
    print("------------------------------------------")
    choice_text=int(input("Enter a number btw. 1 and 3 to select : "))
    print("------------------------------------------")
   
    length=len(TEXTS)
    if choice_text in range (0,length+1) :
        variable=choice_text - 1
        value_1=len(TEXTS[variable].split())
        print(f"There are {value_1} words in the selected text.") 
                
        value = TEXTS[variable].split()
        V = 0
        index = 0
        for value_1 in value : 
            value_2=(value[index]. istitle()) 
            if value_2==True :
                V = V+1
                index+=1
            else:
                index+=1
        print(f"There are {V} titlecase words.")
                
        BIG=0
        index_1=0
        for value_3 in value: 
            value_4=(value[index_1].isupper()) 
            if value_4 is True :
                value_y=(value[index_1].isalpha())
                if value_y is True :
                    BIG = BIG+1
                    index_1+=1
                else:                          
                    for value_7 in TEXTS[variable].split() : 
                        value_8=(TEXTS[0][indexM].islower()) 
                        if value_8 is True :
                            little = little+1
                            indexM+=1
                        else:
                            indexM+=1
                            print(f"There are {mala} lowercase words.") 
            else:
                index_1+=1
                
        print(f"There are {VELKA} uppercase words.")
                
        little = 0
        
                
        sum=0
        numer=0
        indexN=0
        for value_9 in value: 
            value_10=(value[indexN].isnumeric())
            if value_10 is True :
                numer=numer+1
                y=int(hodnota_9)
                sum=sum+y
                indexN+=1
            else:
                indexN+=1
        print(f"There are {numer} numeric strings.") 
        print(f"There sum off all the numbers {sum}.")
              
        value=TEXTS[promenna].split()
        
        value_2=len(value[index])
           
        print("------------------------------------------")
        print("  LEN |   OCCURENCES      | No.")
        print("------------------------------------------")
        print("     1|" , "*" * number_1, " "*(16-number_1), "|",number_1, end="\n")  
        print("     2|" , "*" * number_2, " "*(16-number_2), "|",number_2, end="\n")
        print("     3|" , "*" * number_3, " "*(16-number_3), "|",number_3, end="\n")
        print("     4|" , "*" * number_4, " "*(16-number_4),"|",number_4, end="\n")
        print("     5|" , "*" * number_5, " "*(16-number_5),"|",number_5, end="\n")
        print("     6|" , "*" * number_6, " "*(16-number_6),"|",number_6, end="\n")
        print("     7|" , "*" * number_7, " "*(16-number_7),"|",number_7, end="\n")
        print("     8|" , "*" * number_8, " "*(16-number_8),"|",number_8, end="\n")
        print("     9|" , "*" * number_9, " "*(16-number_9),"|",number_9, end="\n")
        print("    10|" , "*" * number_10," "*(16-number_10),"|",number_10, end="\n")
        print("    11|" , "*" * number_11," "*(16-number_11),"|",number_11, end="\n")
        print("    12|" , "*" * number_12," "*(16-number_12),"|",number_12, end="\n")
        print("    13|" , "*" * number_13," "*(16-number_13),"|",number_13, end="\n")   
                
    else:
        print("$ python project1.py")
        print(f"username:",*pair_user.keys())
        print(f"password:",*pair_user.values()) 
        print("entered text number is wrong, terminating  the  program ..." )
