# 流程图
![业务流程 drawio](https://github.com/Fluchw/Bilibili_Graduation_Design/assets/68312531/ed0f0ad2-d186-49ce-8974-06d9d442d9a6)![R()Y_G {38E_J5GBPT0)HNM](https://github.com/Fluchw/Bilibili_Graduation_Design/assets/68312531/fd0b0934-2a73-4339-839f-184c1fc1a36a)


# 工具使用说明

建议直接使用我提供的Elasticsearch，因为它已经配置好了jieba分词器。其他工具也建议直接使用我的版本，因为使用其他版本可能会出现奇奇怪怪的问题。

下载链接：https://pan.baidu.com/s/1XMqq1DviB1WldifhzihA1w?pwd=ec7h 
提取码：ec7h

## 若是选择自己下载,应该使用的版本:

- apache-zookeeper-3.5.7-bin.tar.gz
- kibana-7.8.0-linux-x86_64.tar.gz
- elasticsearch-7.8.0-linux-x86_64.tar.gz
- elasticsearch-jieba-plugin-7.4.2.tar.gz  (需要自己编译为适配7.8.0)
- filebeat-7.10.2-linux-x86_64.tar.gz
- flink-1.13.0-bin-scala_2.12.tgz
- jdk-8u212-linux-x64.tar.gz
- kafka_2.11-2.4.1.tgz
- Python-3.9.7.tgz
- redis-6.0.6.tar.gz

## 端口映射

hosts:
- 192.168.200.102 hadoop102
- 192.168.200.103 hadoop103
- 192.168.200.104 hadoop104

## 鸣谢

感谢 [https://github.com/Nemo2011/bilibili-api](https://github.com/Nemo2011/bilibili-api) 提供的爬虫程序（bilibili_api） 由于旧版本弹幕文件会丢失，pip下载的最老版本会出现ssl错误，新版本会出现Credential类未提供sessdata错误舍弃。

感谢 [https://github.com/xfgryujk/blivedm](https://github.com/xfgryujk/blivedm) 提供的爬虫程序 在用 /bilibili/blivedm-dev。

感谢 [https://github.com/hiDaDeng/cnsenti](https://github.com/hiDaDeng/cnsenti) 提供的7情绪词典，它是基于大连理工大学情感本体库词典制作的。

