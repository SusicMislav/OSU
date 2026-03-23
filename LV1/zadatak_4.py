
fhand = open("zadaci/song.txt")
song_words = {}
for line in fhand :
    words = line.split()
    for word in words:
        if word in song_words:
            song_words[word] += 1
        else:
            song_words[word] = 1

print(song_words)

print("\nWords that only show up once in the song:")
counter = 0

for word in song_words.keys():
    if song_words[word] == 1:
        print(word)
        counter+=1

print("Number of words that only show up once: ", counter)
fhand.close()