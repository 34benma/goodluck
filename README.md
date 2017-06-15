# goodluck

<pre>
 ,-.           . ,            ,
/              | |            |
| -. ,-. ,-. ,-| |    . . ,-. | ,
\  | | | | | | | |    | | |   |<
 `-' `-' `-' `-' `--' `-` `-' ' `
</pre>

## mercurial插件，程序员命令行下代码提交神器，帮助你谨慎提交代码

[mercurial](https://www.mercurial-scm.org)是一款优秀的代码管理管理,有丰富的插件，也支持自己编写插件(python编写)

goodluck是我在工作过程中使用mercurial命令行提交代码过程中问题总结编写而成。

### 插件编写动机

是否经常在切换分支或者提交代码前忘记先pull代码而造成分支多头？

是否经常创建分支时选择错误分支在合并代码之后才发现问题？

是否经常提交代码的时候忘记比对每次代码修改，确认代码修改都正确？

是否经常合并代码的时候选择错了分支？

如果你跟我一样，喜欢使用命令行，享受命令行带来的简洁和效率快感~

*但是* 你又是一个风行的人,性格急躁，做事情火急火燎~

那么，难免可能会犯上面的错误~

为了减少这些错误的发生，强制自己在代码提交中养成良好的习惯，所以编写了这个插件~

这个插件不能保证你编写的代码没有任何bug，也不能保证你装上这个插件之后，不再犯任何错误~

*但是* 这个拆件可以很大程度上减少你犯这些错误的几率，帮助你养成良好的代码提交习惯~

### 插件原理

插件编写原理非常简单，就是在那些关键代码前后包装一下，增加提示语，让你主动确认才进行操作

让你的步伐慢下来，在那些关键操作前，让你有充足的思考时间，思考清楚再做决定。

详细请查看代码，代码也非常简单~

### 软件运行要求

我是在Mac环境下编写的本插件，Mac系统自带Python，我的默认版本是2.7 因此对于Mac用户和Linux用户使用应该非常简单，执行几个命令即可

- Python 2.7 (暂时不支持python3,后续根据时间和需求，可能会支持Python3)
- mercurial 1.9-3.6 (mercurial目前已经是4.1版本，但是因为我的是3.4，引入的mercurial库貌似只支持到3.6，具体最新版本是否支持待验证)

### 安装前确认

打开命令行工具,进入到用户目录 ~

Step1
```
python --version
```
校验python版本，如果输出2.7版本即可(2.6也可以，更低的不保证某些特性是否支持，如果你懂python，可以检查或修改源码)

Step2 
查看当前目录下是否有 *.hgrc* 配置文件，如果没有，请先找到你的mercurial配置文件，默认安装就在当前用户目录下

### 安装
安装极其简单，将下载的py文件中的*goodluck.py* 拷贝到当前用户目录~ 下

输入
```
python goodluck.py
```
注意，如果你的.hgrc配置文件不在当前目录下，则输入

```
python goodluck.py your_hgrc_path
```

如果提示没有权限执行可以将goodluck.py赋予可执行权限

不到2s，你看到
![](http://o9z6i1a1s.bkt.clouddn.com/goodluck1.png)


打开.hgrc文件，确认是否安装成功

![](http://o9z6i1a1s.bkt.clouddn.com/goodluck2.png)

表示你安装成功


### 使用

因为是对命令进行的包装，因此除了多了一些提示外，其他所有的操作和hg命令一模一样，参数使用也一样。

1. 更新代码

![](http://o9z6i1a1s.bkt.clouddn.com/goodluck_update.png)

2. 提交代码到本地

![](http://o9z6i1a1s.bkt.clouddn.com/goodluck_ci.png)

3. 推送代码

![](http://o9z6i1a1s.bkt.clouddn.com/good_luck_push.png)

4. 合并代码

![](http://o9z6i1a1s.bkt.clouddn.com/good_luck_merge.png)

5. 切换分支

![](http://o9z6i1a1s.bkt.clouddn.com/goodluck_sw_branch.png)

6. 创建分支

![](http://o9z6i1a1s.bkt.clouddn.com/goodluck_branch.png)

### 下一步

下一步要支持实现的是自动打开代码比对工具，强制比对代码~

这个特性还需要研究下hgdiff这个插件以及如何强制打开的问题~

### 后记

这个插件总共花费3个小时左右编写而成~

自己用了暂时没啥问题~

如果你喜欢或者有好的建议，欢迎提Issue或者发邮件告诉我~

Good Luck to you and me~~~

Author: LouisWang

ContancatMe: <a href="mailto:wantedonline@outlook.com">wantedonline@outlook.com</a>

个人GitHub主页: [https://github.com/34benma](https://github.com/34benma)









