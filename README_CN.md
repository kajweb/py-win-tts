# py-win-tts

 [English](README.md)　中文文档



> 基于SAPI.SpVoic 开发的语音合成系统
>
> 通过本系统，可以快速实现文字转语音并输出到指定的播放设备



![操作界面](https://i.loli.net/2020/09/10/hrJK4Oja36LQbBS.png)



## 依赖 

- windows 7、windows 8、windows 10
- Microsoft Speech SDK 5 .1 以上
- Python3



## 安装

```bash
git clone https://github.com/kajweb/py-win-tts.git
cd py-win-tts
pip install -r requirements.txt
```



## 用法

- 在本仓库中，预设了两个示例方法，分别是`main.py`、`simple.py`，您可以

  - 在`CMD命令行`中调用`simple.py`文件

    ```bash
    python simple.py
    ```

  - 在`CMD命令行`中调用`main.py`文件

    ```bash
    python main.py
    ```

    

- 您也可以通过自己新建一个`*.py`文件，新建以下内容并通过`python`调用该文件。

```python
from PyWinTTS import *;
pwt = pyWinTTS();
pwt.speak( "sentence" );
```

> 在不选择输出设备的情况下，默认输出到系统的默认音频输出设备。



## 方法

### getAudioOutput()

获得当前输出设备



### setAudioOutput( index )

设置输出设备



### getVoice()

获得当前播音员



### setVoice( index )

设置播音员



### getVolume()

获得当前音量



### setVolume( value )

设置音量 



### speak( sentence, flags=0 )

开始说话



[更多属性](https://github.com/kajweb/py-win-tts/wiki/属性)　[更多属性](https://github.com/kajweb/py-win-tts/wiki/属性)

## 注意

由于`Microsoft Speech SDK`只能运行在`windows`环境中，同时本项目依赖`Microsoft Speech SDK`，所以本项目**只支持`windows`系统**，其他系统需要对`SAPI.SpVoic`进行兼容处理。

需要更多帮助，请转移到[Wiki页面](https://github.com/kajweb/py-win-tts/wiki/首页)查看帮助

## 许可

MIT