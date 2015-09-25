from pattern.web import *
all_caps = URL('http://genius.com/Madvillain-all-caps-lyrics').download()
all_caps = plaintext(all_caps)
lines = len(all_caps.splitlines())



great_day = URL('http://genius.com/Madvillain-great-day-lyrics').download()
great_day = plaintext(great_day)
print all_caps

