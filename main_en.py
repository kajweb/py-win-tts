#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

from src.PyWinTTS_EN import *;

def PyWinTTS_Tester():
	pwt = pyWinTTS();
	# 设置播放设备
	outputCount = pwt.getAudioOutputCount();
	pwt.displayAudioOutputLists( "There are %d devices in the current system:" % outputCount );
	audioOutputIndex = pwt.getAudioOutputIndex();
	audioOutputIndex = input( "Please select the device you want to export [%d]:" % audioOutputIndex );
	if audioOutputIndex:
		audioOutputIndex = int(audioOutputIndex);
		pwt.setAudioOutput( audioOutputIndex );
	audioOutputName = pwt.getAudioOutputName();
	print( "Current device name:%s" % audioOutputName );


	# 显示播音员列表和当前发音人
	voiceCount = pwt.getVoiceCount();
	print("\n")
	pwt.displayVoiceLists( "There are currently %d speakers in the system:" % voiceCount );
	voiceIndex = pwt.getVoiceIndex();
	voiceIndex = input( "Please select an announcer [%d]:" % voiceIndex );
	if voiceIndex:
		voiceIndex = int(voiceIndex);
		pwt.setVoice( voiceIndex );

	voiceName = pwt.getVoiceName();
	print( "Current speaker: %s" % voiceName );

	# 显示输出音量
	volume = pwt.getVolume();
	# print( "当前系统音量%s" % volume );
	newVolume = input( "\n★Adjust the system volume to(0-100)[%d]：" % volume );
	if newVolume and newVolume!=volume:
		pwt.setVolume( int(newVolume) );
	volume = pwt.getVolume();
	print( "The current pronunciation volume is：%s" % volume );

	while True:
		sentence = input("\nPlease output what you want to say:");
		print( "Pronunciation……" );
		pwt.speak( sentence );
		print( "Pronunciation complete" );

if __name__ == '__main__':
	PyWinTTS_Tester();