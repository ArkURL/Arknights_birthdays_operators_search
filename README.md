# Arknights_birthdays_operators_search
使用scrapy框架爬取prts上的干员生日信息并保存到本地，从而可以方便的使用干员-生日双向查询功能

## 环境需求
需要python环境中至少有以下依赖：
1. python 3.8及以上（没有测试过python 3.7及以下版本，最好使用3.8及以上版本的python解释器）
2. scrapy包及其相关依赖包（如lxml、twisted等）。
3. pyqt包及相关依赖包。

## 用法
在pycharm等IDE中运行View/MainInterface.py，即可看到图形界面，通过图形界面进行对应操作即可。

## 日志
### ver 1.1
#### 改动
1. 增加了图形界面。
2. 通过设置并行请求数提高了爬虫速度，在网络状况良好的情况下能更快完成信息爬取。

#### 可改进的地方
1. 可在middlewares处设置随机UA，使并发爬虫更容易通过。

### ver 1.2
#### 改动
1. 在settings.py文件中设置了UA表用于随机UA访问网站，同时在middlewares.py中做出了对应的修改。
2. 修改了爬虫完成信息爬取后弹出的信息框按钮，可直接在按钮中进行重新爬取。

#### 附言
采用了随机UA后发现效果并不理想，耗费时间多于并发爬取、单UA设置的耗费时间，因此改回使用单UA，若要修改随机UA则只需要在settings.py中取消注释即可。

### ver 1.3
#### 改动
1. 添加了icon，同时修改了一下面板

### ver 1.4
#### 改动
1. 尝试使用pyinstaller输出exe文件，但会出现路径问题及窗口重复出现的问题，还是直接通过python解释器运行比较稳定。
2. 完善了README.MD文件。