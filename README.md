# pyPacking_xhr包说明
> 包简介：实现快速搭建python打包环境，快速打包python包。

## 1.包的安装:
```cmd
pip install pyPacking_xhr@git+https://github.com/...(后面加上文件的位置)

eg：
pip install  pyPacking_xhr@git+https://github.com/jhfwb/pyPacking_xhr
```

## 2.如何开始运行pyPacking_xhr

> 以打包test_xhr为例

###### 1.准备工作

①创建一个文件夹（文件名称自己取，建议和包名一致），将需要打包的包放入该文件夹中

②创建一个demo.py文件，也放在文件夹中。注意不是放在包中。文件结构如下：

> test_xhr	(这个文件夹名字自取，建议和包名一致)
>
> ​		test_xhr	（包的名称.此处以test_xhr为例）
>
> ​				\_\_init\_\_.py	（此包必须含有该文件，否则报错）
>
> ​		demo.py

③书写demo.py

```python
from pyPacking_xhr import PackingTool #导包
#	1.创建打包对象packingTool
packTool=PackingTool()
#	2.创建打包环境（不执行打包操作）  **重点：一般只执行该语句就行
packTool.create_packing_env(pyPackage='test_xhr')
#	3.执行打包操作
packTool.runningSetup()
#	完成

#	或者直接执行创建+打包
#	PackingTool().pack(pyPackage='test_xhr')

```

## 3.pyPacking_xhrの主要功能及介绍

## 4.pyPacking_xhrの目录结构

## 5.pyPacking_xhrの原理







