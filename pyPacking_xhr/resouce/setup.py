#!/usr/bin/env python
# coding=utf-8
import setuptools
# sys.argv=['setup.py','sdist','bdist_wheel'] #将sys.argv的外部参数改成setup.py。相当于是运行python
with open("README.md", 'r',encoding='UTF-8') as f:
    long_description=f.read()
setuptools.setup(
    name="@xxx@",#软件包名称
    version='@version@',
    author="许焕燃",
    author_email='527077832@qq.com',
    description="@description@",
    long_description=long_description,#详细描述
    long_description_content_type="text/markdown",#详细描述的格式
    # url="@xxx@@git+https://github/jhfwb/...", #模块的github地址
    packages=setuptools.find_packages(),
    # py_modules=["Tool"],
    classifiers=[# 程序的所属分类列表
         "Development Status :: 3 - Alpha",
         "Topic :: Utilities",
         "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    install_requires=[# 填写依赖包(github格式:  包名@git+https://github/jhfwb/包所在文件 )
    ],
    python_requires='>=3'
)
