def emojies():
    emoji={
        ":)":"😊",
        ":(":"😟",
        ";)":"🤣",
        ";(":"😥",
        ":":"😶"
    }
    return emoji


def al(massage):
    emoji = emojies()
    mix = ""
    words = massage.split(' ')
    for ch in words:
        mix += emoji.get(ch, ch) + " "
    return mix


massage=input(">>")
print(al(massage))