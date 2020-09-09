#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

##################################################################
##													      		##
## 		  					PY-WIN-TTS						    ##
## 		     通过Microsoft Speech SDK调用SAPI.SpVoice发音	 		##
## 		 	 	  如需输出到麦克风，请自行安装虚拟声卡	     		##
## 			GITHUB：https://github.com/kajweb/py-win-tts			##
##															    ##
##################################################################

import win32com.client

class pyWinTTS():
	# 初始化
	def __init__( self ):
		self._spVoice = self._getSpVoice();

	# 获得一个SpVoice对象
	def _getSpVoice( self ):
		return win32com.client.Dispatch( "SAPI.SpVoice" );

	# 显示播放设备列表
	def displayAudioOutputLists( self, title=False ):
		audioOutputLists = self.getAudioOutputLists();
		if title:
			print( "★", title, sep="" );
		index = 0;
		for i in audioOutputLists:
			print( index, i.GetDescription(), sep=":" );
			index += 1;

	# 获得播放设备数量
	def getAudioOutputCount( self ):
		audioOutputLists = self.getAudioOutputLists();
		return len( audioOutputLists );

	# 获得播放设备列表
	def getAudioOutputLists( self ):
		spVoice = self._spVoice;
		return spVoice.GetAudioOutputs();

	# 判断音频输出设备的序号是否存在
	def isExitsAudioOutput( self, index ):
		audioOutputCount = self.getAudioOutputCount();
		return True if index<audioOutputCount else False;

	# 获得当前输出设备
	def getAudioOutput( self ):
		spVoice = self._spVoice;
		return spVoice.AudioOutput;

	# 获得当前输出设备的序号
	def getAudioOutputIndex( self ):
		audioOutput = self.getAudioOutput();
		audioOutputLists = self.getAudioOutputLists();
		audioOutputCount = self.getAudioOutputCount();
		index = 0;
		while audioOutput.Id != audioOutputLists[index].Id:
			index += 1;
			if( index>=audioOutputCount ):
				raise NotFoundAudioOutput( "无法匹配设备" );
		return index;

	# 获得当前输出设备名称
	def getAudioOutputName( self ):
		audioOutput = self.getAudioOutput();
		return audioOutput.GetDescription();

	# 设置输出设备
	def setAudioOutput( self, index ):
		spVoice = self._spVoice;
		isExitsAudioOutput = self.isExitsAudioOutput( index );
		if not isExitsAudioOutput:
			raise NotFoundAudioOutput( "无法找到该设备" );
		audioOutputLists = self.getAudioOutputLists();
		spVoice.AudioOutput = audioOutputLists[index];

	# 获得当前说话者
	def getVoice( self ):
		spVoice = self._spVoice;
		return spVoice.Voice;

	# 获得当前说话者信息
	def getVoiceName( self ):
		voice = self.getVoice();
		return voice.GetDescription();

	# 判断音频输出设备的序号是否存在
	def isExitsVoice( self, index ):
		voiceCount = self.getVoiceCount();
		return True if index<voiceCount else False;

	# 获得播音员数量
	def getVoiceCount( self ):
		voiceLists = self.getVoiceLists();
		return len( voiceLists );

	# 显示播音员列表
	def displayVoiceLists( self, title=False ):
		voiceLists = self.getVoiceLists();
		if title:
			print( "★", title, sep="" );
		index = 0;
		for i in voiceLists:
			print( index, i.GetDescription(), sep=":" );
			index += 1;

	# 获得系统中发音员列表
	def getVoiceLists( self ):
		spVoice = self._spVoice;
		return spVoice.GetVoices();

	# 获得当前输出设备的序号
	def getVoiceIndex( self ):
		voice = self.getVoice();
		voiceLists = self.getVoiceLists();
		voiceCount = self.getVoiceCount();
		index = 0;
		while voice.Id != voiceLists[index].Id:
			index += 1;
			if( index>=voiceCount ):
				raise NotFoundVoice( "无法匹配播音员" );
		return index;

	# 获得播音员名称
	def getVoiceName( self ):
		voice = self.getVoice();
		return voice.GetDescription();

	# 设置播音员
	def setVoice( self, index ):
		spVoice = self._spVoice;
		isExitsVoice = self.isExitsVoice( index );
		if not isExitsVoice:
			raise NotFoundVoice( "无法找到该播音员" );
		VoiceLists = self.getVoiceLists();
		spVoice.Voice = VoiceLists[index];

	# 获得输出音量（ 0 - 100 ）
	def getVolume( self ):
		spVoice = self._spVoice;
		return spVoice.Volume;

	# 设置输出音量（ 0 - 100 ）
	def setVolume( self, value ):
		spVoice = self._spVoice;
		if not value>=0 and not value<=100:
			raise VolumeSettingError( "声音输出范围不在有效值" );
		spVoice.Volume = value;
		print( "【成功】设置音量为%d" % value );

	# 播放声音
	def speak( self, sentence, flags=0 ):
		# sentence As String
		# flags As SpeechVoiceSpeakFlags = SVSFDefault

		# Enum SpeechVoiceSpeakFlags
		#     'SpVoice Flags
		#     SVSFDefault = 0
		#     SVSFlagsAsync = 1
		#     SVSFPurgeBeforeSpeak = 2
		#     SVSFIsFilename = 4
		#     SVSFIsXML = 8
		#     SVSFIsNotXML = 16
		#     SVSFPersistXML = 32

		#     'Normalizer Flags
		#     SVSFNLPSpeakPunc = 64

		#     'TTS Format
		#     SVSFParseSapi = 
		#     SVSFParseSsml = 
		#     SVSFParseAutoDetect = 

		#     'Masks
		#     SVSFNLPMask = 64
		#     SVSFParseMask = 
		#     SVSFVoiceMask = 127
		#     SVSFUnusedFlags = -128
		# End Enum
		spVoice = self._spVoice;
		spVoice.Speak( sentence, flags );

# 捕抓异常 - 父类
class RunTimeError(Exception):
	def __init__(self, errmsg):
		print( "【执行异常】：%s"%errmsg );
		self.errmsg = errmsg
	def __str__(self):
		return self.errmsg

# 找不到音频输出设备
class NotFoundAudioOutput(RunTimeError):
	pass;

# 找不到播音员
class NotFoundVoice(RunTimeError):
	pass;

# 音量设置错误
class VolumeSettingError(RunTimeError):
	pass;