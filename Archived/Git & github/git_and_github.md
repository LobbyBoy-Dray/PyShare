> **目录**
> 
> 1. Git & Github
> 	* Git
> 	* Github
> 	* 两者关系
> 2. Repository
> 	* Create a repo
> 	* Create a new file in github
> 	* Modify a file in github
> 	* Upload a new file in github
> 3. Branch
> 	* 创建分支
> 	* 合并分支
> 4. Fork
> 5. Pull Request
> 6. Issue
> 7. Git与使用命令
> 	* Git概述
> 	* 基本Linux命令
> 	* 初次使 Git
> 8. Clone
> 9. Status & Add & Commit
> 	* 一些概念
> 	* 本地修改
> 	* 进入缓存区
> 	* 提交修改
> 	* 查看修改日志
> 10. Push/Pull
> 	* Push
> 	* Pull
> 11. Init

## 1. Git & Github

Git与Github是两个不同的概念。

### 1) Git

Git is one of the most popular **version control system(VCS)**. It is a mature, actively maintained, open source project compatible with many operating systems and IDEs.

Git 是一款免费的、开源的分布式**版本控制系统**。

**什么是版本控制？**

简单来说，版本控制是指，将每次对项目的修改，包括修改内容、修改者、修改时间等内容储存起来，以便track或roll back。

### 2) Github

Github是基于Git版本控制的代码托管平台。即，Github上上传的所有项目代码均是基于Git进行版本控制的。但Github的功能除了Git为它提供的版本控制外，还有其他许多强大的功能，比如项目协作等。

### 3) 两者关系

Github使用Git进行版本控制，同时提供其他强大功能。

“大概就是「魔兽争霸」与「对战平台」的关系吧”——某知乎网友。

## 2. Repository

**Repository**, or "**Repo**"：可以简单理解为**Project**，存储着一个项目，可以包含很多文件，即Repository of files；如果想在Github上拥有一个项目，就必须创建一个Repository。

### 1) Create a repo

在加号的下拉菜单中点击`New repository`：

![Alt text](./1.png)

进入创建repo的界面：

![Alt text](./2.png)

创建成功后自动跳转到该repo内部：

![Alt text](./3.png)

可以在github中创建文件或上传文件：

![Alt text](./4.png)

### 2) Create a new file in github

点击`Create new file`，进入文本编辑界面，输入内容即可（注意文件名要加后缀）。完成后，点击`commit new file`

![Alt text](./5.png)

创建完毕：

![Alt text](./6.png)

### 3) Modify a file in github

点击文件，再点击“笔”，进入修改模式：

![Alt text](./7.png)

修改完成，点击commit changes：

![Alt text](./8.png)

修改历史（历史版本）可以在`History`中查看：

![Alt text](./9.png)

每次修改记录均可见：

![Alt text](./10.png)

点击进入可以查看更加详细的修改信息：

![Alt text](./11.png)

### 4) Upload a new file in github

从本地上传文件至github：

![Alt text](./12.png)

## 3. Branch

分支。主要用于项目的团队开发，也可以用于个人work on different aspects of the project。

任何一个Repo都有一个主分支，名为“master”。You can think the history of a project as a linear list of commit，而这个linear list就是master，如下图所示：

![Alt text](./13.png)

即分支是一个流程，是由无数次的修改提交（commit）构成一个时间轴。

而当你想在Repo中为你的项目加入一些新特性，而又isn‘t sure whether you should keep it的时候，你需要一块专门的空间来做experimental try，在这个空间里，你做的任何改动不会影响“大局”，即“master”，你可以放心对文件进行修改，直到修改到满意为止。这个空间就是你新建的分支（branch），可以最终通过merge，将该分支合并到master上，相当于把原来在“试验田”中的新特性正式加到你的项目中。

对于单人开发，可能只需要master和develop两个分支，平时的开发在develop分支进行，开发测试完成后，在发布前将develop合并到master分支即可。

对于团队开发，可以为每个开发者创建一个分支，每个人在自己的分支上开发自己的部分，然后逐步merge到master。

因此分支相当于生产零部件，master相当于主车间里的主体，最终零部件都是要进入主车间进行装配的。

### 1) 创建分支

举例：现在我想为我的歌词加入中文翻译，因此我可以创建一个分支，名为translation：

![Alt text](./14.png)

创建完毕后：

![Alt text](./15.png)

已经进入translation分支，下面在该分支里对文件进行修改并提交：

![Alt text](./16.png)

点击`Branch`可以切换回master分支：

![Alt text](./17.png)

可以看到在master分支中，中文翻译并没有被加入：

![Alt text](./18.png)

### 2) 合并分支

新建的分支可以在Repo主页面看到：

![Alt text](./19.png)

上图中的绿框`Compare & pull request`就好像这个分支的创建者（这里是我自己）对我说：would you please take my changes? would you please pull my request and merge into the master branch?

所以pull request的含义是：take some changes from the particular branch and bring them into another branch（usually master branch）。

如果想要将该分支合并，点击该绿框，进入pull request页面：

![Alt text](./20.png)

点击`create pull request`。但此时还没有完成merge，点击后github会检测两个合并的分支是否存在冲突，若不存在冲突，继续点击`merge pull request`、`confirm merge`：

![Alt text](./21.png)

合并完成，translation分支可以被删除了：

![Alt text](./22.png)

在`Insights`-`network`里可以看到这一过程的图示：

![Alt text](./23.png)

## 4. Fork

相当于复刻，将别人的Repo完完整整地复刻到自己的Github中，供自己参考，或者在别人的项目基础上进行改进。此时任你如何修改这个fork过来的repo，丝毫不会影响原作者那边的Repo，因为这个Repo相当于副本，也可以理解为使一个branch，在branch上改，当然不影响其他的branch。

**怎样fork别人的Repo？**

进入该Repo，随便点击一个文件，点击“笔”：

![Alt text](./24.png)

或者点击右上角的fork：

![Alt text](./25.png)

## 5. Pull Request

在Branches部分已经简单提及Pull Request的概念，可以理解为“获取请求”。假设别人fork了你的Repo，然后在这个fork上面做了一些改进，他觉得改进很棒，也有利于你的代码，因此他想把他在你的fork上的修改提供给你——contribute it back to the original repo。此时他需要push request，即“推出请求”，即向你发出请求，请求你允许他将他的那部分代码合并到你的原Repo中；而你如果同意的话，就需要pull request，即“获取请求”。

当修改完毕fork的Repo后，

![Alt text](./26.png)

点击后并按操作继续，可以向原Repo的主人push request，接着你就只需默默祈祷他能够pull your request。

在原主人那里，他会接收到你push的request，在下图的`Pull requests`里可以看到，他会根据他的需求选择是否接受你的修改。

![Alt text](./27.png)

## 6. Issue

问题，事件。

![Alt text](./28.png)

Issues  is a place to leave a comment about the project. It can be some one who finds a bug, or you would like to start a vote.

点击`New issue`创建一个issue：

![Alt text](./29.png)

创建完毕后，在issues界面可以看到有一个issue是open的：

![Alt text](./30.png)

点进去后可以关闭这个issue。对于别人发起的issue，你看到了这些问题可以去逐个修复，修复完成后就可以一个个的close掉。

## 7. Git与使用命令行

### 1) Git概述

你可以在Github上使用Git进行版本管理，也可以在自己的电脑上（本地）使用Git进行版本管理，并与Github进行交互，但前提是你的电脑上已经安装了Git。

Mac系统自带Git，但Win不一定。在命令行中键入`git`并回车，如果没有报错（如下图），则你的电脑已经安装Git；如果报错，则需要在Git官网根据自己的电脑类型下载相应安装包：

![Alt text](./31.png)

[Git for Win](https://git-scm.com/download/win)

强烈推荐使用命令行（Command Line）操作Git而非GUI界面，因为使用命令行操作可以加深对于Git的理解。

Git的基本操作命令如下（不用全部记住，浏览一下就好）：

![Alt text](./32.png)

可以发现，Git命令均以`git`开头。

### 2) 基本Linux命令

Win系统下，`ls`命令无法使用，等价命令为`dir`。

推荐一款Win的终端替代软件——cmder，免费，颜值高，功能强大，解决`ls`在Win下无法使用的问题等等。下载地址为：[Download](http://cmder.net/)

必须知道的四个命令：

* `cd`：切换当前工作目录至xxx，`cd ..`表示返回上一层目录；
* `pwd`：显示当前工作目录；
* `ls`：显示当前工作目录中所有文件的名称，`ls -a`显示包括隐藏文件的名称；
* `clear`：清除屏幕（历史记录）。

![Alt text](./33.png)

### 3) 初次使用Git

初次使用Git需要设置姓名和邮箱，告诉Git你是谁：

* `git config –global user.name "你的姓名"`
* `git config –global user.email "你的邮箱"`

## 8. Clone

`git clone`: Clone a repository into a new directory.

Clone命令将一个GitHub上的Repo克隆（download）到本地，变为本地仓库。

Clone一个Repo需要给到该Repo的url，查看方法如下：

![Alt text](./34.png)

因此要Clone该Repo（Lyrics）到我的桌面，步骤为：

* 打开终端；
* cd到桌面；
* 找到该Repo的链接：https://github.com/LobbyBoy-Dray/Lyrics.git；
* `git clone https://github.com/LobbyBoy-Dray/Lyrics.git`；

![Alt text](./35.png)

## 9. Status & Add & Commit

`git status`: Show the working tree status.

### 1) 一些概念

![Alt text](./36.png)

根据上图理解以下概念：

* `working tree`：工作区，即Repo文件夹。在上例中，working tree就是Lyrics这个文件夹，包括里面的所有文件夹和文件。每当你修改了其中的某个文件，working tree的状态就会改变；
* `stage`：缓存区，一个中转站；
* `local repository`：本地仓库，也叫版本库，存储着各种不同的版本，即History。

回到上面的例子，对于刚刚clone下来的Lyrics仓库，cd进去后，键入`git status`：

![Alt text](./37.png)

因为对刚刚clone下来的Lyrics仓库，我还没有做任何改动，所以会显示`nothing to commit, working tree clean`。

PS: 建议大家没事就输一下这个命令来查看你当前工作区的状态。

### 2) 本地修改

两处变化：

* 修改Lyrics中的`That girl.md`文件（加了两句英文歌词）；
* 增加了一个文件，名为`That girl_2.md`。

此时，再次键入`git status`：

![Alt text](./38.png)

上图说明了两点，也是Git帮你发现的两个改变：

* 工作区中的`That girl.md`文件被修改，该文件的状态变为**modified**，且该修改还**not staged**；
* 工作区中的`That girl_2.md`是个新文件，刚才还不在工作区里，所以被Git标记为**untracked**，说明该文件虽然在工作区里，但是没有加入到git库中，不参与版本控制。

可见，工作区中的文件有三种类型：

* `untracked`：未跟踪状态，一般是新建的文件或文件夹。虽然该文件在工作区中，但并没有加入到Git库中，不参与版本控制，需要进行后续一些操作将其入库；
* `unmodified`：未修改状态，比如Lyrics中的readme文件，我没有修改它，所以它是未修改状态。这样的文件已经入库，参与版本控制，但没有被修改，git status命令也不会显示这些文件；
* `modified`：修改状态，说明该入库的文件已经被修改。

### 3) 进入缓存区

工作区发生变化，即出现`untracked`或`modified`文件时，Git会提示你将他们提交到**缓存区**，即**stage**。

使用`git add .`将所有改动，包括提交到缓存区；使用`git add 文件名`将特定的改动文件提交到缓存区。这里我使用前一种命令，将一个`untracked`文件和一个`modified`文件提交到stage中，并使用`git status`查看状态：

![Alt text](./39.png)

可见，字体颜色由红变绿，说明改动被成功提交至缓存区。此时上述两个文件来到了一个新的状态——**staged**，暂存状态。

处于该状态下的修改，仅仅为“暂存”，并没有最终生成新的版本。还需要再进行一步`git commit`，将修改最终同步到库中。

因此，可以将缓存区理解为临时保存你的改动的区域，这样做的优点是防止失误提交。

如果“后悔了”，可以use `git reset HEAD <file>..." to unstage`将修改移出缓存区，回到第一步中的工作区成为`untracked`状态或`modified`状态。

### 4) 提交修改

使用`git commit -a -m "这里写一些注释"`来完成最终提交。

![Alt text](./40.png)

在最终提交完毕后，那些staged状态的文件，最终会转化为unmodified状态，回到工作区，其历史版本信息则被保存在local repository中。

在commit后，使用`git status`再次查看状态，可以发现，`nothing to commit, working tree clean`，一切重归于好。

### 5) 查看修改日志

使用`git log`：

![Alt text](./41.png)

可以看到，除了刚刚的修改被记录了下来，早上在Github上操作的修改也被记录了下来，这是因为Clone的效果，Clone把一切信息都复制了下来。

## 10. Push/Pull

### 1) Push

此时，你想把刚刚在本地对Repo的修改同步到Github上，需要使用`git push`命令。

![Alt text](./42.png)

`push`：推。如果你本地代码有更新，那么就需要把本地代码推到远程仓库（remote repository），这样本地仓库（local repository）跟远程仓库就可以保持同步了。

一般直接使用`git push origin master`，意思是将本地代码“推”到远程仓库的master分支上。

![Alt text](./43.png)

### 2) Pull

`pull`：拉。如果别人提交代码到远程仓库，这个时候你需要把远程仓库的最新代码同步到自己本地电脑上的Repo中。

常用命令：`git pull origin master`

一般在push前都会先pull一下，这样不容易产生冲突。

## 11. Init

如果想要在本地电脑从零开始创建一个Repo，再将其上传至github，就要使用`git init`命令。

**举例：在本地新建名为Poem的Repo**

首先，在桌面新建名为Poem的文件夹，并在其中新建名为`love_story.txt`的文件，输入一些内容并保存。

![Alt text](./44.png)

打开终端，cd到Poem文件夹（在进行任何git操作前，都要先切换到仓库目录，也就是要cd到项目文件夹的目录下），键入`git status`查看Repo的状态：

![Alt text](./45.png)

系统会提示`Not a git repository`，意思就是当前目录还不是一个Repo——肯定的啊，不是随便在自己电脑上建一个文件夹它就是Git仓库的，需要手动设置，标定它成为Repo。

在根目录下使用`git init`：

![Alt text](./46.png)

可以看到，Poem文件夹已经被初始化一个Git仓库了。

此时`git status`：

![Alt text](./47.png)

上图说明，该Repo中的所有文件都没有被tracked，处于untracked状态，因此需要add并commit：

`git add .`: 将所有文件放入缓存区；
`git commit -a -m "xxxxxx"`：提交修改；

接下来使用`git push origin master`命令上传到Github，发现出现错误：

![Alt text](./48.png)

这是因为，这个刚刚创建的本地仓库，并没有和远程仓库——即github上的Repo建立关联（not associated）。使用`git remote`或`git remote -v`查看与本地仓库关联的远程仓库：

![Alt text](./49.png)

发现的确该本地Repo还没有关联任何远程Repo。

此时需要打开Github，新建一个同名的Repo，注意此时不用选中Initialize this repository with a readme。

![Alt text](./50.png)

新建后转到如下页面：

![Alt text](./51.png)

拿到远程仓库链接后，使用`git remote add origin 链接`命令，将本地仓库与远程仓库连接起来：

![Alt text](./52.png)

此时再使用`git remote`和`git remote -v`查看，发现已经关联完毕。

最后使用`git push origin master`命令将该Repo上传到Github，成功：

![Alt text](./53.png)

总结一下步骤（以Poem为例）：

1. cd到Poem下；
2. `git init`；
3. 在github上创建Repo，拿到远程仓库链接；
4. `git remote add origin 链接`；
5. `git add .`；
6. `git commit -a -m "注释"`；
7. `git push origin master`；

**为什么clone下来的文件夹不需要init？**

因为clone操作可以看做**高级复制**，clone下来的项目本身已经被git处理好了，已经是一个git仓库了，所以不需执行`git init`命令。







