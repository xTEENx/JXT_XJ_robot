[TOC]

# 项目概述

## 项目背景

项目名为**交小通**，是XJTUSER的NLP课程设计项目

> 该项目主要是为了解决XJTU传统教务处的种种弊端

该项目是我们团队利用 langchain 思想实现的基于本地知识库的问答应用，简单而言就是**将交大官网、教务处、各学书院官网、实践中心、团委等主体网页中的相关通知、规定、声明、解决方案等信息文件作为本地知识导入知识库。用户提出疑问后大模型根据本地知识库总结概括生成答案**。

技术路线如下：

部署文件/技术路线.png

## 项目进展

由于时间紧张以及团队技术受限，我们完成了以下功能（打勾的即为完成的，未打勾即为未完善或未来完成的）：

- [x] WEB 爬虫
  - [x] 西安交通大学教务处官网通知
  - [x] 西安交通大学百度贴吧讨论
  - [x] 西安交通大学相关百度词条
  
- [ ] 本地知识库搭建
  - [x] 知识文档获取
  - [ ] 结构化文件拆分（如 csv）
  - [x] 非结构化文件拆分（如 txt）
  - [x] 文本分割功能
  - [x] 向量化
- [ ] 大模型 API 接入
  - [x] 本地大模型接入（[FastChat ](https://github.com/lm-sys/FastChat)等）
  - [ ] 联网大模型接入（chatGPT 3.5，chatGPT 4.0，文心一言等）
- [x] 数据库
  - [x] 数据库概念模型
  - [x] 数据库SQL仓库
- [x] WEB UI
  - [x] 对话界面
  - [x] 知识库管理界面
  - [x] 界面优化

# 项目部署

## 本地化部署
如果助教老师需要查看项目，我们不推荐本地化部署，电脑配置要求较高：
1. 显卡：RTX 3090及以上
2. 内存：5GB及以上

如果本地化部署该项目，操作如下：
1. 首先确保有python运行环境
2. 克隆该项目，并安装好相应的依赖

> 注意：依赖较大，下载时间较久
```shell
# 拉取仓库
$ git clone 

# 安装全部依赖
$ pip install -r requirements.txt 
$ pip install -r requirements_api.txt
$ pip install -r requirements_webui.txt  
```
3. 需要下载相应的大模型文件
```shell
$ git lfs install
$ git clone https://huggingface.co/THUDM/chatglm3-6b
$ git clone https://huggingface.co/BAAI/bge-large-zh
```
4. 项目启动
```shell
$ python startup.py -a
```
5. 查看项目

可以查看WEB UI 界面，注意，**每个电脑的端口设置不同**，请以运行结果出现的链接为主！
如果在浏览器输入链接后出现如下界面，则说明项目运行无误：

![展示图](.\展示图.png)

## 云部署

1、选择右侧AutoDL创建容器

> 创建用户，实名认证，充值等操作请自行摸索！

2、选择主机环境，gpu环境,，注意版本为cuda12!

![镜像配置](.\镜像配置.png)

3、开机

![镜像配置](.\开机.png)

![jupyter](.\jupyter.png)

4、打开终端

> 终端在左下角打开即可
>
> 或者可以在图像化主页看到终端

下面是终端命令
4.1 一键启动
选择新的终端

```shell
$  cd /root/.../
$  conda activate /root/pyenv
$  python startup.py -a
```

等待出现下图

5、打开页面

企业用户

![SSH](.\SSH.png)

个人用户

点击**自定义服务**

![隧穿](.\隧穿.png)

>  根据操作方法建立隧道链接**ssh隧道**，按照官网教程操作即可运行服务

运行如下图：

![展示图](.\展示图.png)
