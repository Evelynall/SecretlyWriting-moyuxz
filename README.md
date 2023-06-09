# SecretlyWriting-moyuxz
对更多内容有兴趣，欢迎访问我的[个人主页](https://evelynall.github.io/)

🐟：一款可以上班摸鱼码字的神器软件~（An artifact software that can secretly write at work ~）

这是一款用Python编写的小小小软件，灵感来自于Utools的“摸鱼阅读”。

咱几乎没有Python基础，此软件是在**ChatGPT**的帮助下完成的。

由于一开始是为个人需求制作，并没有设置太多自定义功能，仅仅在决定打包分享的时候制作了一些基础设定。

### 使用方法&展示
解压，双击“moyuxz.exe”即可，
打包的exe版本**比较臃肿**，整整**9.44MB**，而且启动速度偏慢，如果电脑**有Python环境**的话可以使用源文件，只有**4kb**。

默认界面为Adobe的黑色，如图

![应用界面](https://cdnjson.com/images/2023/06/08/image.png)

* 鼠标按住可以**随意拖动位置**，但暂时不支持调整大小
* 按下回车可以保存已经输入的内容到文件目录的`text.txt`中。
* 双击界面或者按 `Ctrl`+`w` 快捷键可以直接退出，退出时文本框内容会保存，同时保存软件当前位置，下次打开时会在同一位置出现。

### 自定义内容
在文件目录有一个 `config.txt` 文件，可以编辑基本的功能。
```
position: 53,1012  //软件位置，每次退出时会更新
background: #262626   //软件背景颜色
foreground: #8a8a8a    //文字颜色
exitkey: <Control-w>   //退出快捷键
filename: text.txt    //文件位置（直接写则为相对路径，如需其他位置的文件，请写绝对路径 如 C:\Tools\text.md ）
```
注意：所有自定义内容前需要有一个空格才能生效，负责会报错。（如 filename:[空格]text.txt ）

ps:本来想做一个界面的，但Python写界面好麻烦www

### 开源内容
软件代码完全开源（毕竟也没几行，也没什么技术含量XD）
同时几乎**每一行代码都有注释**(菜是这样的)

![开源代码](https://cdnjson.com/images/2023/06/08/image27d960424334db16.png)

### 更新日志
* 2023-06-09 增加自定义文件位置功能
* 2023-06-08 软件发布

### ending
欢迎关注我的各个平台，或许会有其他小东西更新~

![名片](https://cdnjson.com/images/2023/03/12/image8749fd86705e58b5.png)
