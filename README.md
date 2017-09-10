# message_forward

群消息转发

因为只关注特定人在群内的发言，所以用此机器人转发特点群内特点人的消息给自己

## itchat

本程序使用 [https://github.com/littlecodersh] 实现

## 安装依赖

安装python 3.6

```python
pip install itchat pillow
```

## 安装

请自行下载……

需要安装python 3.6

## 配置

在子目录下的config.py 中配置要关注的群及要关注的群成员名单，将自己设置为master即可

该群内的关注的成员的消息内容会被转发给master

```python
SCRIBUTE_USER_NAMES = ['群成员昵称1','群成员昵称2'] # 订阅群成员的消息
MASTER_NAME = 'master' # 要将消息转发给的好友的名字
GROUP_NAME = '群名称' # 订阅的群名称
```

## 运行
```python
python run.py
```