def get_book_contents():
    contents = ""
    with open("./books/frankenstein.txt") as f:
        contents = f.read()
    return contents

def get_word_count(contents):
    words = contents.split()
    return len(words)

def get_letter_counts(contents):
    letters = {}
    for i in range(0, len(contents)):
        curr = contents[i].lower()
        if curr in letters:
            letters[curr] += 1
        else:
            letters[curr] = 1
    return letters

def convert_counts_to_list(dict):
    ret = []
    for key in dict:
        if key.isalpha():
            ret.append({"letter": key, "count": dict[key] })
    return ret

def sort_on(dict_item):
    return dict_item["count"]

def main():
    contents = get_book_contents()
    character_counts = get_letter_counts(contents)
    letter_list = convert_counts_to_list(character_counts)
    letter_list.sort(reverse=True, key=sort_on)
    print(letter_list)

main()