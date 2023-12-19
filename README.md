# xuexitong_auto_input Documention
## Chinese Simplified
### 介绍
彼阳的学习通，赤石的学习通。奶奶滴，不让我粘贴是吧，都别想活着！（误

个人烂活。帮你模拟键盘输入，将需要输入的文字输入学习通窗口的脚本。（也可用于其他不能hack掉粘贴限制的服务，例如批改网）
### 部署
目前只能通过CLI运行。

Dependencies:Python 3,pynput

目前只在Python 3.10.4 64bit @Windows 11上测试过，使用到的函数应该不依赖于版本。欢迎测试。

正常来说不需要再安装`pynput`。如果很不幸，你的系统上没有安装，在终端执行`pip -install pynput`。

将脚本下载到你的本地机器上,方式你喜欢就好。

### 运行
1.在脚本相同目录下创建一个文本文件`input.in` ~~OIer狂喜时间~~ ，将需要输入的文字**以UTF-8编码**保存到该文本文件。（记得打开Windows资源管理器的选项“隐藏已知文件格式拓展名”~~废话~~）

2.在上述目录下打开终端窗口，执行`python3 xuexitong_auto_input.py`（具体请参考你的运行环境。）

### Todo
i18n.（懒）

## English
### Intro
A simple script simulating keyboard input to help you input text into Xuexitong window/webpage to cope with paste limitations.

### Deploy
Make sure you have Python 3 installed on your machine. `pynput` is also required.(It is installed with python interpreter by default. If not, execute `pip -install pynput`.)

Download the script to your machine as you wish.

### Run
1.Create a text file `input.in` on the same directory as the script. Save the text you need to enter as **UTF-8** decode in the file.

2.Run the script using `python3 xuexitong_auto_input.py`.(May differ with environment.)

### Todo
i18n for the tiny project.