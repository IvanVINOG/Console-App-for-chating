class Person:
        while True:
            country = input("Enter your country please")
            city = input("Enter your city please")
            age = int(input("Enter your age please"))
            gender = input("Men  or Women")
            name = input("Enter your name please")
            number = int(input("Enter your number"))
            interest  = input("Please enter your interests")
            Germany = {
                "Berlin",
                "Cologne",
                "Hamburg",
                "Munich",
                "Dortmund",
                "Leipzig",
                "Frankfurt"
            }
            Russia = {
                "Moscow",
                "Saint Petersburg",
                "Novosibirsk",
                "Yekaterinburg",
                "Nizhny Novgorod",
                "Samara",
                "Omsk",
                "Kazan",
                "Rostov-on-Don"
            }
            France = {
                "Toulouse",
                "Marseille",
                "Lyon",
                "Nice",
                "Paris",
                "Nantes",
                "Strasbourg",
                "Montpellier",
                "Bordeaux"
            }
            Spain = {
                "Madrid",
                "Barcelona"
                "Valencia",
                "Seville",
                "Zaragoza",
                "Malaga",
                "Murcia",
                "Palma",
                "Las Palmas",
                "Bilbao"
            }
            England = {
                "London",
                "Manchester",
                "Birmingham",
                "Liverpool",
                "Sheffield",
                "Bristol",
                "Leeds",
                "Glasgow",
                "Edinburgh"

            }
            USA = {
                "New York",
                "Los Angeles",
                "Chicago",
                "Houston",
                "Phoenix",
                "Philadelphia",
                "San Antonio",
                "San Diego",
                "Dallas"

            }
            girl1 = {
                "USA",
                "New York",
                "23",
                "Women",
                "Rose"
            }
            men1 = {
                "Russia",
                "Moscow",
                "27",
                "Men",
                "Timur"

            }
            girl2 = {
                "Germany",
                "Berlin",
                "35",
                "Women",
                "Emma"

            }
            men2 = {
                "Spain",
                "Madrid",
                "33",
                "Men",
                "Diego"

            }
            girl3 = {
                "France",
                "Paris",
                "42",
                "Women",
                "Alice"
            }
            men3 = {
                "England",
                "London",
                "44",
                "Men",
                "Ivan"

            }
            if country == "USA" or  country == "usa" or country == "America":
                if city in USA:
                    if 20 <= age <= 29:
                        if gender == "Men":
                            for item in girl1:
                                print(item)
                        print(name, ",I think you would like her !")
            if country == "Russia":
                if city in Russia:
                    if 20 <= age <= 29:
                        if gender == "Women":
                            for men in men1:
                                print(men)
                        print(name, ",I think you would like him !")

            if country == "Germany":
                if city in Germany:
                    if 30 <= age <= 39:
                        if gender == "Men":
                            for girl in girl2:
                                print(girl)
                        print(name, ",I think you would like her !")
            if country == "Spain":
                if city in Spain:
                    if 30 <= age <= 39:
                        if gender == "Women":
                            for bn in men2:
                                print(bn)
                        print(name, ",I think you would like him !")
            if country == "France":
                if city in France:
                    if 40 <= age <= 45:
                        if gender == "Men":
                            for gh in girl3:
                                print(gh)
                        print(name, ",I think you would like her !")
            if country == "England":
                if city in England:
                    if 40 <= age <= 45:
                        if gender == "Women":
                            for mn in men3:
                                print(mn)
                        print(name, ",I think you would like him !")

Person()