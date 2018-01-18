import enchant

def read_words(filename):
    words = set([word.strip("\n").lower() for word in open(filename, "r").readlines()])
    return words

def replace_all(sentence, replacements):
    for replacement in replacements:
        sentence = sentence.repleace(replacement, replacements[replacement])
    return sentence

def sanitize_word_input(sentence):
    symbols = [
        "!", "@", "#", "$", "%", "^", "&", "*",
        "(", ")", "_", "+", "=", "<", ">", ",",
        "`", "~", ":". ";", "\'", "\"", "[", "]",
        "{", "}", "|", "\\", "\/"
    ]
    replacements = {}
    
    for s in symbols:
        replacement[s] = ""
    
    for r in replacements:
        replacements.replace(r, replacements[r])

    return sentence

def check_words(sentence):
    dictionary = enchant.Dict("en_US")
    return len(list(dictionary.check(word) for word in sentence))

def main():
    read_words("words.txt")

if __name__ == "__main__":
    main()