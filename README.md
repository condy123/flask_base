本人也热爱各种技术，对php，ruby，java，python都很所涉及，
```
如果您也是编程道路上一个热爱学习新技术的道友，可以加好友一起互相学习
```

由于发展需要，从php->ruby到学习java、python语言，接下来准备进军算法和人工智能领域。

写此小项目，主要是为了练手，了解flask。以及一些遇到过的坑，方便日后直接使用flask可以直接copy


欢迎刚学习flask的同学查阅，给出宝贵的建议和意见。如果有什么出错的地方麻烦不喜勿喷谢谢


####遇到的bug
如果您在测试过程中运行models.py报错，请先剪切掉admin/views,运行完成之后再黏贴回去。

报错信息：
```
sqlalchemy.exc.InvalidRequestError: Table 'user' is already defined for this MetaData instance.
Specify 'extend_existing=True' to redefine options and columns on an existing Table object.

```

####主要功能：
```
表单验证
重定向
视图展示
图片接收展示
redis缓存的使用
蓝图的构造
配置文件加载
消息闪现
使用装饰器限制未登录用户
日志处理
```


####后续增加功能
```
kafka
rabbitmq
消息队列
```



