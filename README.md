# CUIT教学平台手动刷课脚本：

事情的起因是这样的，我们老师让我们在教学平台上面看视频课，需要看到足够的时间，才能获得一个证书，我干脆手写了一个脚本，用来刷课。

因为教学平台很简陋，所以其实可以直接完成视频进度。

**只是完成，我还没有添加增长学习时间的部分**

## 使用须知：

> 需要Python版本>3.10
>
> 需要导入
>
> 1.  requests
> 2. json
> 3. re
>
> 三个模块

## 使用方式：

首先登录你的教学平台

![image-20230513152520631](https://cdn.jsdelivr.net/gh/Ho1L0w-By/Picturebed@main/img/image-20230513152520631.png)

按f12，进入到存储部分，找到你本地的cookie：

![image-20230513152730113](https://cdn.jsdelivr.net/gh/Ho1L0w-By/Picturebed@main/img/image-20230513152730113.png)

复制除了CsrfToken的另外四个值，然后依次填入程序需要的：

![image-20230513152908734](https://cdn.jsdelivr.net/gh/Ho1L0w-By/Picturebed@main/img/image-20230513152908734.png)

然后进到视频页面，找到上方链接，输进去，回车即可

![image-20230513153344261](https://cdn.jsdelivr.net/gh/Ho1L0w-By/Picturebed@main/img/image-20230513153344261.png)

![image-20230513153113636](https://cdn.jsdelivr.net/gh/Ho1L0w-By/Picturebed@main/img/image-20230513153113636.png)

如果成功，就会显示成功。

接下来就重复这个过程，来回复制即可。

增加学习时间功能回头我再添上，做这个主要还是为了好玩。

**警告：**

严正声明，由脚本导致的任何后果与我本人无关。

