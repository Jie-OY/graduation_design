# graduation_design

### 技术栈

* 前端 VueJS 2.0 + Mint-ui
* 后端 Flask
* 数据库 SQLserver

### 已经实现的功能

* 登录
* 个人信息的修改
* 在线题库练习

### Trick
在进行这种前后端分离的开发时，如果你每次写完前端都生成一个js文件，再放到后端替换是比较繁琐的。
这里直接写作：`  <script type="text/javascript" src="http://localhost:8080/dist/build.js"></script>`
如此，前端更新后后端不用替换任何文件，同时实现热更新

### Screenshot
![个人信息](/image/个人信息.png)
![在线练习1](/image/在线练习1.png)
![在线练习2](/image/在线练习2.png)
