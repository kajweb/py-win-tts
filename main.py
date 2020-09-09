#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

from src.PyWinTTS import *;

def PyWinTTS_Tester():
	pwt = pyWinTTS();
	# 设置播放设备
	outputCount = pwt.getAudioOutputCount();
	pwt.displayAudioOutputLists( "当前系统共有%d个设备：" % outputCount );
	audioOutputIndex = pwt.getAudioOutputIndex();
	audioOutputIndex = input( "请选择你要输出的设备[%d]：" % audioOutputIndex );
	if audioOutputIndex:
		audioOutputIndex = int(audioOutputIndex);
		pwt.setAudioOutput( audioOutputIndex );
	audioOutputName = pwt.getAudioOutputName();
	print( "当前设备名称：%s" % audioOutputName );


	# 显示播音员列表和当前发音人
	voiceCount = pwt.getVoiceCount();
	print("\n")
	pwt.displayVoiceLists( "当前系统共有%d个发音员：" % voiceCount );
	voiceIndex = pwt.getVoiceIndex();
	voiceIndex = input( "请选择播音员[%d]：" % voiceIndex );
	if voiceIndex:
		voiceIndex = int(voiceIndex);
		pwt.setVoice( voiceIndex );

	voiceName = pwt.getVoiceName();
	print( "当前发音人：%s" % voiceName );

	# 显示输出音量
	volume = pwt.getVolume();
	# print( "当前系统音量%s" % volume );
	newVolume = input( "\n★调整系统音量为(0-100)[%d]：" % volume );
	if newVolume and newVolume!=volume:
		pwt.setVolume( int(newVolume) );
	volume = pwt.getVolume();
	print( "当前发音音量为：%s" % volume );

	while True:
		sentence = input("\n请输出你想说的话：");
		print( "正在发音……" );
		pwt.speak( sentence );
		print( "发音完成" );

if __name__ == '__main__':
	PyWinTTS_Tester();