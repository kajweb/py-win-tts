#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

from src.PyWinTTS import *;

if __name__ == '__main__':
	str1 = "The program runs.";
	str2 = "Prepare to pronounce.";
	str3 = "Please pay attention to whether you hear any sound.";
	sentence = "\n".join([str1, str2, str3]);

	print( "[start]", sentence, sep="\n" );
	pwt = pyWinTTS();
	pwt.speak( sentence );
	print( "[end]" );