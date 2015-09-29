#John Bozzella, SoftDes 2015
#Function to import lyrics from genius.com with inputs of the URLs and titles
#the script also calculates the number of unique words in each song and plots the word counts and ratio
#Extra print statements in the actual function are for debugging

from pattern.web import *
from math import *
import matplotlib.pyplot as plt
import numpy as np



doomsites = ['http://genius.com/Madvillain-the-illest-villains-lyrics' , 'http://genius.com/Madvillain-accordion-lyrics' , 'http://genius.com/Madvillain-meat-grinder-lyrics' , 'http://genius.com/Madvillain-bistro-lyrics' , 'http://genius.com/Madvillain-raid-lyrics' , 'http://genius.com/Madvillain-americas-most-blunted-lyrics' , 'http://genius.com/Madvillain-rainbows-lyrics' , 'http://genius.com/Madvillain-curls-lyrics' , 'http://genius.com/Madvillain-money-folder-lyrics' , 'http://genius.com/Madvillain-shadows-of-tomorrow-lyrics' , 'http://genius.com/Madvillain-operation-lifesaver-aka-mint-test-lyrics' , 'http://genius.com/Madvillain-figaro-lyrics' , 'http://genius.com/Madvillain-hardcore-hustle-lyrics' , 'http://genius.com/Madvillain-strange-ways-lyrics' , 'http://genius.com/Madvillain-fancy-clown-lyrics' , 'http://genius.com/Madvillain-eye-lyrics' , 'http://genius.com/Madvillain-all-caps-lyrics' , 'http://genius.com/Madvillain-great-day-lyrics' , 'http://genius.com/Madvillain-rhinestone-cowboy-lyrics']
doomtitle = ['Madvillainy']
beatlessites = ['http://genius.com/The-beatles-back-in-the-ussr-lyrics' , 'http://genius.com/The-beatles-dear-prudence-lyrics' , 'http://genius.com/The-beatles-glass-onion-lyrics' , 'http://genius.com/The-beatles-ob-la-di-ob-la-da-lyrics' , 'http://genius.com/The-beatles-wild-honey-pie-lyrics' , 'http://genius.com/The-beatles-the-continuing-story-of-bungalow-bill-lyrics' , 'http://genius.com/The-beatles-while-my-guitar-gently-weeps-lyrics' , 'http://genius.com/The-beatles-happiness-is-a-warm-gun-lyrics' , 'http://genius.com/The-beatles-martha-my-dear-lyrics' , 'http://genius.com/The-beatles-im-so-tired-lyrics' , 'http://genius.com/The-beatles-blackbird-lyrics' , 'http://genius.com/The-beatles-piggies-lyrics' , 'http://genius.com/The-beatles-rocky-raccoon-lyrics' , 'http://genius.com/The-beatles-dont-pass-me-by-lyrics' , 'http://genius.com/The-beatles-why-dont-we-do-it-in-the-road-lyrics' , 'http://genius.com/The-beatles-i-will-lyrics' , 'http://genius.com/The-beatles-julia-lyrics' , 'http://genius.com/The-beatles-birthday-lyrics' , 'http://genius.com/The-beatles-yer-blues-lyrics' , 'http://genius.com/The-beatles-mother-natures-son-lyrics' , 'http://genius.com/The-beatles-everybodys-got-something-to-hide-except-me-and-my-monkey-lyrics' , 'http://genius.com/The-beatles-sexy-sadie-lyrics' , 'http://genius.com/The-beatles-helter-skelter-lyrics' , 'http://genius.com/The-beatles-long-long-long-lyrics' , 'http://genius.com/The-beatles-revolution-i-lyrics' , 'http://genius.com/The-beatles-honey-pie-lyrics' , 'http://genius.com/The-beatles-savoy-truffle-lyrics' , 'http://genius.com/The-beatles-cry-baby-cry-lyrics' , 'http://genius.com/The-beatles-revolution-9-lyrics' , 'http://genius.com/The-beatles-good-night-lyrics']
beatlestitle = ['The White Album']
mjsites = ['http://genius.com/Michael-jackson-wanna-be-startin-somethin-lyrics' , 'http://genius.com/Michael-jackson-baby-be-mine-lyrics' , 'http://genius.com/Michael-jackson-the-girl-is-mine-lyrics' , 'http://genius.com/Michael-jackson-thriller-lyrics' , 'http://genius.com/Michael-jackson-beat-it-lyrics' , 'http://genius.com/Michael-jackson-billie-jean-lyrics' , 'http://genius.com/Michael-jackson-human-nature-lyrics' , 'http://genius.com/Michael-jackson-pyt-pretty-young-thing-lyrics' , 'http://genius.com/Michael-jackson-the-lady-in-my-life-lyrics' , 'http://genius.com/Michael-jackson-carousel-lyrics']
mjtitle = ['Thriller']
tswiftsites = ['http://genius.com/Taylor-swift-welcome-to-new-york-lyrics' , 'http://genius.com/Taylor-swift-blank-space-lyrics' , 'http://genius.com/Taylor-swift-style-lyrics' , 'http://genius.com/Taylor-swift-out-of-the-woods-lyrics' , 'http://genius.com/Taylor-swift-all-you-had-to-do-was-stay-lyrics' , 'http://genius.com/Taylor-swift-shake-it-off-lyrics' , 'http://genius.com/Taylor-swift-i-wish-you-would-lyrics' , 'http://genius.com/Taylor-swift-bad-blood-lyrics' , 'http://genius.com/Taylor-swift-wildest-dreams-lyrics' , 'http://genius.com/Taylor-swift-how-you-get-the-girl-lyrics' , 'http://genius.com/Taylor-swift-this-love-lyrics' , 'http://genius.com/Taylor-swift-i-know-places-lyrics' , 'http://genius.com/Taylor-swift-clean-lyrics' , 'http://genius.com/Taylor-swift-wonderland-lyrics' , 'http://genius.com/Taylor-swift-you-are-in-love-lyrics' , 'http://genius.com/Taylor-swift-new-romantics-lyrics']
tswifttitle = ['1989']

def lyricsimport(sites):

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


	for count , elem in enumerate(sites):  #Create a list containing the HTML from each page as plaintext, split up by line

		textbyline.append(plaintext(URL(sites[count]).download()).splitlines())
		text.append(plaintext(URL(sites[count]).download()).split())

	for count , elem in enumerate(text):  #Create a list where each element is the number of lines in each page
		lines.append(len(textbyline[count]))
			
	
	
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

	return lyrics
	

 #Call the function
doomlyrics = lyricsimport(doomsites)
beatleslyrics = lyricsimport(beatlessites)
mjlyrics = lyricsimport(mjsites)
tswiftlyrics = lyricsimport(tswiftsites)



def lyricsplot(lyrics,title):
	uniquewordcount = []  #define a word count list
	wordcount = []

	for count , elem in enumerate(lyrics):  #Find the number of words and unique words used in each song
		uniquewordcount.append(len(set(lyrics[count])))
		wordcount.append(len(lyrics[count]))


	awc = np.array(wordcount)			#create an array for wordcount and uniquewordcount
	auwc = np.array(uniquewordcount)
	wcratio = np.true_divide(auwc,awc)
		
	titlecount = np.arange(1,len(lyrics)+1)

	plt.figure		#using matplotlib, plot the arrays 

	plt.subplot(2,1,1)
	plt.plot(titlecount , wordcount , 'ro')
	plt.axis([0, len(titlecount)+1, 0, 700])
	plt.plot(titlecount , uniquewordcount , 'g^')
	plt.axis([0, len(titlecount)+1, 0, 700])
	plt.title('Word Counts')

	plt.subplot(2,1,2)
	plt.plot(titlecount , wcratio, 'bs')
	plt.axis([0, len(titlecount)+1, 0, 1])
	plt.title('Percent Unique Words')
	plt.xlabel(title)
	plt.show()


lyricsplot(doomlyrics,doomtitle)
lyricsplot(beatleslyrics,beatlestitle)
lyricsplot(mjlyrics,mjtitle)
lyricsplot(tswiftlyrics,tswifttitle)

	








	









 