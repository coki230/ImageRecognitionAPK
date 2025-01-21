** 其他语言：[English](README.md), [中文](README_zh.md)。 **
# 项目介绍：
此项目用来识别手机的图片，可以识别1000种类型。最最重要的是此项目**不需要联网，不需要联网，不需要联网。重要的事情说三遍。**
而且这只是搭建了一个框架，**可以调用任意模型，可以少量代码迁移到其他平台**，包括ios系统，windows系统，mac系统等等。
所以熟悉了这套框架，你可以在你本地不需要联网调用很多大模型，来实现特定的功能。
## 项目依赖：
此项目说基于[Buildozer](https://buildozer.readthedocs.io/en/latest/)来发布项目
界面是用[kivymd](https://kivymd.readthedocs.io/en/latest/)画出来的。
所以如果你打算自己开发，需要熟悉上面两个项目，
## 发布流程：
如果你已经完全阅读了[Buildozer](https://buildozer.readthedocs.io/en/latest/)的文档，
并安装了相对应的安装包。
在控制台里cd到此项目的根目录，执行：`buildozer -v android debug`，此命令会在此项目的根目录下生成一个中间件依赖目录`.buildozer`，
执行完成后会生成一个`bin`目录，并在里面生成一个apk的文件，把此文件安装到手机里可以直接使用。
**注意，需要给此apk开通读取文件到权限**
## 最后为自己打个广告
本人是一个IT老兵，是一个全栈工程师，熟悉机器学习，和后台开发。如果有远程的工作机会，或者技术移民的机会很乐意和大家探讨。谢谢
如果有兴趣邮件联系我：xiao230coki@gmail.com
