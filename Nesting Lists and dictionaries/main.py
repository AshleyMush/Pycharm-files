capitals = {"France:": "Paris",
            "Germany": "Berlin",}


#TODO Nesting a list in a dictionary


travel_log = {

    #KEY           #VALUE
#     👇               👇
#
    "France": ["Paris", "Lille", "Dijon"]

    "Germany": ["Berlin", "Hamburg", "Stuttgart"]

}

#TODO Nesting dictionary in a dictionary

travel_log2 = {

'''
          Key             dictionary as Value                      
                 ____________________________________________________________
          👇     |                                                            |         
'''
        "Harare":{ "cities_visited" : ["Mbare", "Mvurwi"] , "total_visits": 12}
}

#_________________________Example 2______________

travel_log = {

     "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},

    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"] ,"total_visits": 5},

}

#Nesting a dictionary in a list
travel_log = [



    {
        "country": "France",

         "cities_visited":["Paris", "Lille", "Dijon"],

         "total_visits": 12
     },

    {
        "country":"Germany",

        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],

        "total_visits": 5},

]