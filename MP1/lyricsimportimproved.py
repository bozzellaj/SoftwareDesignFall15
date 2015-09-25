#John Bozzella, SoftDes 2015
#Function to import lyrics from genius.com with inputs of the URLs and titles
#the script also calculates the number of unique words in each song
#Extra print statements in the actual function are for debugging

from pattern.web import *


sites = ['http://genius.com/Madvillain-accordion-lyrics' , 'http://genius.com/Madvillain-meat-grinder-lyrics' , 'http://genius.com/Madvillain-americas-most-blunted-lyrics' , 'http://genius.com/Madvillain-rainbows-lyrics' , 'http://genius.com/Madvillain-curls-lyrics' , 'http://genius.com/Madvillain-money-folder-lyrics' , 'http://genius.com/Madvillain-shadows-of-tomorrow-lyrics' , 'http://genius.com/Madvillain-figaro-lyrics' , 'http://genius.com/Madvillain-fancy-clown-lyrics' , 'http://genius.com/Madvillain-all-caps-lyrics' , 'http://genius.com/Madvillain-great-day-lyrics' , 'http://genius.com/Madvillain-rhinestone-cowboy-lyrics']
titles = ['Accordion' , 'Meat Grinder' , 'Americas Most Blunted' , 'Rainbows' , 'Curls' , 'Money Folder' , 'Shadows of Tomorrow' , 'Figaro' , 'Fancy Clown' , 'All Caps' , 'Great Day', 'Rhinestone Cowboy']


def lyricsimport(sites,titles):

	# originially this was just a script, hence the commented-out code

	#from pattern.web import *  

	#define necessary lists

	#sites = ['http://genius.com/Madvillain-accordion-lyrics' , 'http://genius.com/Madvillain-meat-grinder-lyrics' , 'http://genius.com/Madvillain-americas-most-blunted-lyrics' , 'http://genius.com/Madvillain-rainbows-lyrics' , 'http://genius.com/Madvillain-curls-lyrics' , 'http://genius.com/Madvillain-money-folder-lyrics' , 'http://genius.com/Madvillain-shadows-of-tomorrow-lyrics' , 'http://genius.com/Madvillain-figaro-lyrics' , 'http://genius.com/Madvillain-fancy-clown-lyrics' , 'http://genius.com/Madvillain-eye-lyrics' , 'http://genius.com/Madvillain-all-caps-lyrics' , 'http://genius.com/Madvillain-great-day-lyrics' , 'http://genius.com/Madvillain-rhinestone-cowboy-lyrics']
	#titles = ['Accordion' , 'Meat_Grinder' , 'Americas_Most_Blunted' , 'Rainbows' , 'Curls' , 'Money_Folder' , 'Shadows_of _omorrow' , 'Figaro' , 'Fancy_Clown' , 'Eye' , 'All_Caps' , 'Great_Day', 'Rhinestone_Cowboy']
	text = []
	textbyline = []
	lines = []
	lyrics = []
	lyricsbyline = []
	boundlines = [0,0]
	print len(titles)
	print len(sites)


	for count , elem in enumerate(sites):  #Create a list containing the HTML from each page as plaintext, split up by line

		textbyline.append(plaintext(URL(sites[count]).download()).splitlines())
		text.append(plaintext(URL(sites[count]).download()).split())

	for count , elem in enumerate(text):  #Create a list where each element is the number of lines in each page
		lines.append(len(textbyline[count]))
			
			
	print len(text)
	print len(textbyline)
	print len(lines)
	



	for count , elem in enumerate(textbyline): #cut the plain text HTML into just the song lyrics
		subtext = textbyline[count]
		
		for n in range(lines[count]):  #determine which lines are actually the lyrics
			if subtext[n] == 'Embed' and n<100:  #this is done by checking for key words that appear in the HTML on each page
				#print n
				boundlines[0] = n+2

			if subtext[n] == 'Edit the description to add:':
				#print n
				boundlines[1] = n

		lyricsbyline.append(subtext[boundlines[0] : boundlines[1]])  #create a list : each element is a list of the lyrics of each song from [sites] by line
		lyrics.append(" ".join(lyricsbyline[count]).split())

		

	print len(lyrics)
	print len(lyricsbyline)
	return lyrics
	

 #Call the function and print the lyrics to Great Day
lyrics = lyricsimport(sites,titles)
#print lyrics[11]
wordcount = []  #define a word count list

for count , elem in enumerate(lyrics):  #Find the number of different words used in each song
	wordcount.append(len(set(w.lower for w in lyrics[count])))

print titles
print wordcount






	








	









