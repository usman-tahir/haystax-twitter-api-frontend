import enchant

def sanitize_word_input(sentence):
    symbols = [
        "!", "@", "#", "$", "%", "^", "&", "*",
        "(", ")", "_", "+", "=", "<", ">", ",",
        "`", "~", ":", ";", "\"", "[", "]", "{",
        "}", "|", "\\", "\/", "?"
    ]
    replacements = {}
    
    for s in symbols:
        replacements[s] = ""
    
    for r in replacements:
        sentence = sentence.replace(r, replacements[r])

    return sentence

def check_words(sentence):
    dictionary = enchant.Dict("en_US")
    sentence = sanitize_word_input(sentence)
    filtered_words = list(word for word in sentence.split(" ") if len(word) > 0 and dictionary.check(word))
    return len(filtered_words)