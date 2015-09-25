def lyricsimport(sites,titles):

	# originially this was just a script, hence the commented-out code

	#from pattern.web import *  

	#define necessary lists

	#sites = ['http://genius.com/Madvillain-accordion-lyrics' , 'http://genius.com/Madvillain-meat-grinder-lyrics' , 'http://genius.com/Madvillain-americas-most-blunted-lyrics' , 'http://genius.com/Madvillain-rainbows-lyrics' , 'http://genius.com/Madvillain-curls-lyrics' , 'http://genius.com/Madvillain-money-folder-lyrics' , 'http://genius.com/Madvillain-shadows-of-tomorrow-lyrics' , 'http://genius.com/Madvillain-figaro-lyrics' , 'http://genius.com/Madvillain-fancy-clown-lyrics' , 'http://genius.com/Madvillain-eye-lyrics' , 'http://genius.com/Madvillain-all-caps-lyrics' , 'http://genius.com/Madvillain-great-day-lyrics' , 'http://genius.com/Madvillain-rhinestone-cowboy-lyrics']
	#titles = ['Accordion' , 'Meat_Grinder' , 'Americas_Most_Blunted' , 'Rainbows' , 'Curls' , 'Money_Folder' , 'Shadows_of _omorrow' , 'Figaro' , 'Fancy_Clown' , 'Eye' , 'All_Caps' , 'Great_Day', 'Rhinestone_Cowboy']
	text = []
	lines = []
	lyrics = []
	boundlines = [0,0]
	print len(titles)
	print len(sites)


	for count , elem in enumerate(sites):  #Create a list containing the HTML from each page as plaintext, split up by line
		titles[count] = plaintext(URL(sites[count]).download())
		text.append(titles[count].splitlines())

	for count , elem in enumerate(text):  #Create a list where each element is the number of lines in each page
		lines.append(len(text[count]))
			
			
	print len(text)
	print len(lines)
	



	for count , elem in enumerate(text): #cut the plain text HTML into just the song lyrics
		subtext = text[count]
		
		for n in range(lines[count]):  #determine which lines are actually the lyrics
			if subtext[n] == 'Embed' and n<100:  #this is done by checking for key words that appear in the HTML on each page
				#print n
				boundlines[0] = n+2

			if subtext[n] == 'Edit the description to add:':
				#print n
				boundlines[1] = n

		lyrics.append(subtext[boundlines[0] : boundlines[1]])  #create a list : each element is a list of the lyrics of each song from [sites] by line

		

	print len(lyrics)
	return lyrics