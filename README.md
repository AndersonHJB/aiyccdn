# AI悦创·流沙视频图床，编程一对一！长期招收编程一对一，少儿编程一对一！微信：Jiabcdefh

## 1. 克隆仓库

使用方法：

```git
git clone git@github.com:AndersonHJB/vd.git
```


## 2. Base Url

基础的 URL，我这里是解析过的，所以使用：[https://github.aiyc.top/aiyccdn/](https://github.aiyc.top/aiyccdn/)，所以后面直接加上你的文件名称和后缀即可。

https://github.aiyc.top/aiyccdn/+你的文件路径

视频分割命令：

```ffmepg
ffmpeg -i [文件名].mp4 -profile:v baseline -level 3.0 -s 1920x1080 -start_number 0 -hls_time 10 -hls_list_size 0 -f hls [生成m3u8文件名].m3u8
```

```url
https://github.aiyc.top/aiyccdn/
```
