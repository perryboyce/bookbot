def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f: 
        file_contents = f.read()

        print(get_alphabet_report(get_char_count(file_contents)))
        # print(get_char_count(file_contents))
        # return get_word_count(file_contents)

    pass


    
def get_char_count(file_contents):
    lowerString = file_contents.lower()

    countDict = {}

    for char in lowerString:
        if not(char in countDict):
            countDict[char] = 1
        elif char in countDict:
            countDict[char] +=1

    return countDict

def countdict_sort_on(dict):
    return dict["num"]

def get_alphabet_report(countDict):
    countList = []
    report = ""
    for key in countDict:
        if key.isalpha():
            countList.append({
                "char" : key,
                "num" : countDict[key]
            })

    countList.sort(reverse=True, key=countdict_sort_on)
 
    for item in countList:
        report+= f"The '{item["char"]}' character was found {item["num"]} times\n"

    return report

def get_file_text(file_contents):
    return file_contents

def get_word_count(file_contents):

    return len(file_contents.split())


print(main())