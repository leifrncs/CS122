n1 , n2 , n3 = input("Enter three nouns: ").upper().split()
a1, a2, a3 = input("Enter three adjectives: ").upper().split()

song = """\nTitle: You Decorated My Life by Kenny Rogers \n
All my life was a paper once plain, pure and white
Till you moved with your pen changin' moods now and then
Till the balance was right
Then you added some music, ev'ry note was in place
And anybody could see all the changes in me by the look on my face \n
And you decorated my life, created a world where dreams are apart
And you decorated my life by paintin' your love all over my heart
You decorated my life\n
Like a rhyme with no reason in an unfinished song
There was no harmony life meant nothin' to me, until you cam along
And you brought out the colors, what a gentle surprise
Now I'm able to see all the things life can be shinin' soft in your eyes
And you decorated my life, created a world where dreams are a part
And you decorated my life by paintin' your love all over my heart
You decorated my life"""

new = song.replace ("life", n1).replace("heart",­ n2).replace("world",­ n3).replace ("white", a1).replace("right",­ a2).replace("unfinis­hed", a3)

print("\nOriginal Song: \n", song)
print("\n\nModified Song: \n", new)