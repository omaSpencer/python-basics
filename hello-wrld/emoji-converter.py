def emoji_converter(message):
    output = ""
    words = message.split(' ')
    emojis = {
        ":)": "😄",
        ":D": "😄",
        ":(": "😞"
    }
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))
