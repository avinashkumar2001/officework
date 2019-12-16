massage=input(">>")
words=massage.split(' ')
emoji={
    ":)":"😊",
    ":(":"😟",
    ";)":"🤣",
    ";(":"😥",
    ":":"😶"
}
mix=""
for ch in words:
    mix+=emoji.get(ch,ch)+" "
print(mix)