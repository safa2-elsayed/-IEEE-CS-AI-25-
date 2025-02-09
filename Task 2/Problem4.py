books ={"book 1": {"title" : "Zekola Land" , "auther" : "Amr Abdelhameed" , "Publication Year" : 2010 },
        "book 2": {"title" : "Amareta" , "auther" : "Amr Abdelhameed" , "Publication Year" : 2015 },
        "book 3": {"title" : "Wadi Elze2ab " , "auther" : "Amr Abdelhameed" , "Publication Year" : 2023 },
}

for book, details in books.items():
    print(f"Book: {book}")
    print(f"Title: {details['title']}")
    print(f"Author: {details['auther']}")
    print(f"Year: {details['Publication Year']}")
    print("-" * 30)
