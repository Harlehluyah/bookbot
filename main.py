def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print_report(count_words(file_contents), count_characters(file_contents))

def count_words(file_contents):
    words = file_contents.split()
    counter = len(words)
    
    return counter
    
def count_characters(file_contents):
    characters = {}
    lower_case_words = file_contents.lower().split()
    
    for word in lower_case_words:
        for char in word:
            if (char in characters):
                characters[char] += 1
            else:
                characters[char] = 1

    return characters
 
#helper function for sorting        
def sort_on(dictionary):
    return dictionary["count"]
    
#sort dict of chars into a list of chars (only the alphabets)
def sort_alphabets_only(characters_dict):
    
    chars_list = []
    
    for char ,count in characters_dict.items():
        if (char.isalpha()):
            chars_list.append({"char": char, "count": count})
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list

def print_report(word_count, characters_dict):
    print("-- Begin report of books/frankenstein.txt --")
    print(f"{word_count} words found in the document")
  
    sorted_alphabets_list = sort_alphabets_only(characters_dict)
    
    for char_dict in sorted_alphabets_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    
main()