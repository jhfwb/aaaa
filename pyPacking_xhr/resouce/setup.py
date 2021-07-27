#!/usr/bin/env python
# coding=utf-8
import setuptools
# sys.argv=['setup.py','sdist','bdist_wheel'] #将sys.argv的外部参数改成setup.py。相当于是运行python

setuptools.setup(
    name="@xxx@",#软件包名称
    version='@version@',
    author="许焕燃",
    author_email='527077832@qq.com',
    description="@description@",
    long_description=open('README.md').read(),#详细描述
    long_description_content_type="text/markdown",#详细描述的格式
    # url="@xxx@@git+https://github/jhfwb/...", #模块的github地址
    packages=setuptools.find_packages(),
    license='TMT',
    include_package_data=True,
    zip_safe=False,
    # py_modules=["Tool"],
    classifiers=[# 程序的所属分类列表
         'Framework :: Scrapy',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[# 填写依赖包(github格式:  包名@git+https://github/jhfwb/包所在文件 )
    ],
    python_requires='>=3'
)
