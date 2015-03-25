import os

urlpref = "http://cts.cdn.scaleengine.net/sestore1/vodstore/cts/c2k/c"
urlsfx  = ".mp3"

books = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
         "Joshua", "Judges", "Ruth", "1Samuel", "2Samuel", 
         "1Kings", "2Kings", "1Chronicles", "2Chronicles", "Ezra",
         "Nehemiah", "Esther", "Job", "Psalms", "Proverbs",
         "Ecclesiastes", "SongOfSolomon", "Isaiah", "Jeremiah", "Lamentations",
         "Ezekiel", "Daniel", "Hosea", "Joel", "Amos",
         "Obadiah", "Micah", "Nahum", "Habakkuk", "Zephaniah",
         "Zechariah", "Malachi", 
         "Matthew", "Mark", 
         "Luke", "John", "Acts", "Romans", "1Corinthians", 
         "2Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", 
         "1Thessalonians", "2Thessalonians", "1Timothy", "2Timothy", "Titus", 
         "Philemon", "Hebrews", "James", "1Peter", "2Peter", 
         "1John", "23John", "Jude", "Revelation"]


filecnts = [19, 12, 5, 4, 7, # Deuteronomy
            3, 4, 1, 4, 3, # 2 Samuel
            4, 4, 3, 5, 1, # Ezra
            2, 1, 6, 16, 6, # Proverbs
            2, 1, 17, 14, 1, # Lamentations
            9, 4, 3, 2, 2, # Amos
            1, 1, 1, 1, 1, # Habakkuk
            4, 1, # Malachi
            16, 10,  # Mathew, Mark
            15, 12, 16, 9, 10,
            7, 4, 6, 3, 2,
            2, 1, 3, 2, 1,
            1, 7, 2, 2, 1,
            4, 1, 1, 10]

def start():
    startfile = 2001
    for (lim, book) in zip(filecnts, books):
        os.mkdir(book)
        mp3lst = open(book + "/urlist.txt", "w")
        endfile = startfile + lim
        for i in range(startfile, endfile):
            print urlpref + `i` + urlsfx
            mp3lst.write(urlpref + `i` + urlsfx + "\n")
        mp3lst.close()
        startfile = endfile

if __name__ == "__main__":
    start()
