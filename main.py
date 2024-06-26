
def read_file():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    return file_contents

def count_words():
    words = read_file().split()
    n_words = 0
    for word in words:
        n_words += 1
    

    return n_words

def count_letters():
        text_lower = read_file().lower()
        characters = list(text_lower)
        #print(characters[1:10])
        # imports "string" then uses string.ascii_lowercase to take all normal lowercase letters and populates a dict with every letter being a:0 for example.
        #use this instead of else below if you only want characters 
        #import string
        #letter_count = dict.fromkeys(string.ascii_lowercase, 0)

        letter_count = {}
        #print(letter_count)
        
        for character in characters:
            if character in letter_count:
                letter_count[character]  += 1
            #this if all characters
            else: 
                 letter_count[character] = 1

                         
        #print(letter_count)
        return letter_count              

def sort_on(dict):
     return dict["num"]

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    print(count_words(), "words found in the document" )
    letter_count = count_letters()
    
    import string
    letterlist = list(string.ascii_lowercase)
    
    list_sorted = []
    for letter in letterlist:
         list_sorted.append({"lett":letter, "num" : letter_count[letter]})
    
    list_sorted.sort(reverse=True, key=sort_on)   
    
    for letter in list_sorted[0:]:
        plet = letter["lett"]
        pnum = letter["num"]
        print(f"the '{plet}' character was found {pnum} times")     
    
    print("--- End report ---")

main()
    
