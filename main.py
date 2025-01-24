
def main():
    symbols = {"!","("}
    w = count_words(read_book())
    #print(w)
    charcount = count_chars(read_book())
    #print(charcount)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{w} words found in the document")
    for key in charcount:
        if key.isalpha():
            print (f"The '"+key+f"' character was found {charcount.get(key)} times")



def count_words(text):
    count= 0
    words = text.split()
    for word in words:
        count += 1
    return count

def count_chars(text):
    dict = {}
    lowtext = text.lower()
    for s in lowtext:
        if dict.get(s) == None:
            dict[s] = 1
        else:
            dict.update({s:dict.get(s)+1})
    return dict



def read_book():
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
        return file_contents


main()