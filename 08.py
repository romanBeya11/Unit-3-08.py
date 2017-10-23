'''
Created by Roman Beya
Created on 23-oct-2017
Created for ICS3U
This program displays the alphabet with it's corresponding unicode integer
'''
for i in range(65, 91): # all CAPITAL letters of alphabet
	print "{} -> ".format(i) + unichr(i)
for i in range(97, 123): # all LOWERCASE letters of alphabet
	print "{} -> ".format(i) + unichr(i)
