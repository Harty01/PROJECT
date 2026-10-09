def read(filename):
    with open(filename, "r") as file:
        text =file.read()
        return(text)
text=read("original_song_lyrics1.txt")
"""def count(words,number):
    similar=[]
    words=words.split()
    for word in words:
        counts=len(word)
        
        if counts==number:
            similar.append(word)
    return similar

resut=count(text,3)
print(len(resut))"""

def longest(text):
    max=""
    text=text.split()
    for word in text:
        if len(word)>len(max):
            max=word
    return max
result=longest(text)
print(result)

        