#!/usr/bin/env python
# coding=utf-8
import os
import sys
import setuptools
# sys.argv=['setup.py','sdist','bdist_wheel'] #将sys.argv的外部参数改成setup.py。相当于是运行python
with open("README.md",'r',encoding='UTF-8') as f:
    long_description=f.read()
setuptools.setup(
    name="pyPacking_xhr",#软件包名称
    version='1.0.0.0',
    author="许焕燃",
    author_email='527077832@qq.com',
    description="实现自动创建包的外部环境,自动创建setup.py,readme.md等文件.",
    long_description=long_description,#详细描述
    long_description_content_type="text/markdown",#详细描述的格式
    # url="pyPacking_xhr@git+https://github/jhfwb/...", #模块的github地址
    packages=setuptools.find_packages(),
    # py_modules=["Tool"],
    classifiers=[# 程序的所属分类列表
         "Development Status :: 3 - Alpha",
         "Topic :: Utilities",
         "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    install_requires=[# 填写依赖包(github格式:  包名@git+https://github/jhfwb/包所在文件 )
    ],
    python_requires='>=3',
)
