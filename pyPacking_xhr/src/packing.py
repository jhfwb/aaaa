import os
import configparser
import shutil
import pipreqs
def readConfig():
    cf = configparser.ConfigParser()
    cf.read('../resouce/config.ini', encoding='utf-8')
    secs = cf.sections()
    options = cf.options("test")
    return options

#获取当前文件名称
class _createPackingFile:
    def __init__(self,saveDirPath,pyPackingName,pyPackage,options):
        self.options=options
        self.saveDirPath=saveDirPath
        self.pyPackingName=pyPackingName
        self.createLICENSE()
        self.createMANIFESE()
        self.createREADME()
        self.createSETUP()
        self.createGITIGNORE()
        #判断保存地址是不是当前地址，如果是，则不创建源码，如果不是，则要创建
        if not pyPackingName in os.listdir(saveDirPath):
            # 复制整个文件夹到指定目录
            shutil.copytree(pyPackage, saveDirPath+'\\'+pyPackingName)
        else:
            pass

    def _createFile(self,fileName='LICENSE' or 'README.md' or 'MANIFEST.in'or '.gitignore' or 'setup.py' ,sign='@xxx@'):
        if fileName=='LICENSE':
            fileNameAbsPath = os.path.realpath(__file__).replace('src\\packing.py', 'resouce\\LICENSE.tmpl')
        elif fileName=='README.md':
            # os.path.abspath('pyPacking_xhr').split('\\')[-2]
            fileNameAbsPath = os.path.realpath(__file__).replace('src\\packing.py', 'resouce\\README.md.tmpl')
        elif fileName == 'MANIFEST.in':
            fileNameAbsPath = os.path.realpath(__file__).replace('src\\packing.py', 'resouce\\MANIFEST.in.tmpl')
        elif fileName == '.gitignore':
            fileNameAbsPath = os.path.realpath(__file__).replace('src\\packing.py', 'resouce\\.gitignore.tmpl')
        elif fileName == 'setup.py':
            #x寻找外部包
            fileNameAbsPath = os.path.realpath(__file__).replace('src\\packing.py', 'resouce\\setup.py.tmpl')
            fp = open(file=fileNameAbsPath, mode='r', encoding='utf-8')
            wp = open(file=self.saveDirPath + '\\' + fileName, mode='w', encoding='utf-8')
            lines=fp.readlines()
            for i in range(len(lines)):
                for option in self.options:
                    if '@'+option+'@' in lines[i]:
                        lines[i]=lines[i].replace('@'+option+'@',self.options[option])
            wp.writelines(map(lambda x:x.replace(sign,self.pyPackingName),lines))
            fp.close()
            wp.close()
            return
        fp = open(file=fileNameAbsPath, mode='r', encoding='utf-8')
        wp = open(file=self.saveDirPath+'\\'+fileName, mode='w', encoding='utf-8')
        wp.writelines(map(lambda x:x.replace(sign,self.pyPackingName),fp.readlines()))
        fp.close()
        wp.close()
    def createGITIGNORE(self):
        self._createFile(fileName='.gitignore')
    def createLICENSE(self):
        self._createFile(fileName='LICENSE')
    def createMANIFESE(self):
        self._createFile(fileName='MANIFEST.in')
    def createREADME(self):
        self._createFile(fileName='README.md')
    def createSETUP(self):
        self._createFile(fileName='setup.py')
    def createSRC(self):
        pass
class PackingTool:
    """打包工具"""
    def runningSetup(self,savePath=''):
        """
        运行savePath中的setup.py文件，执行打包操作
        :param savePath:
        :return:
        """
        os.system('python setup.py sdist bdist_wheel')
        pass
    def pack(self,pyPackage='',savePath='',options={'version':'0.0.0.0','description':'暂无软件简介信息'}):
        """创建打包环境,并执行打包语句

        :param pyPackage:软件包的名称
        :param savePath:该软件包保存的地址
        :param options:选项，包括version，description等
        :return: None
        """
        self.create_packing_env(pyPackage=pyPackage,savePath=savePath,options=options)
        self.runningSetup(savePath=savePath)
    def create_packing_env(self,pyPackage='',savePath='',options={'version':'0.0.0.0','description':'暂无软件简介信息'}):
        """
        提供打包环境,包括生成LICENSE，MANIFEST.in，README.MD,setup.py，外部打包工具
        :param pyPackage: 打包的文件夹路径
        :param savePath: 保存打包环境的路径，如果该路径不存在，则会创建一个该路径
        :param options: 执行打包的参数
        :return:
        """
        # 获取该包的名称。
        os.system('pipreqs ./  --encoding=utf8  --force')
        pyPackage=os.path.realpath(pyPackage)
        savePath=os.path.realpath(savePath)
        pyPackageName = os.path.basename(pyPackage)
        # 1.参数检查
        #       检查两个参数路径是否存在
        if not os.path.exists(pyPackage) and os.path.isdir(pyPackage):
            raise FileNotFoundError("该文件夹路径不存在:"+pyPackage+'')
        # 2.判断savePath是否为空
        #       如果为空则保存在本地
        #       如果不为空则保存在其他地方
        if not os.path.exists(savePath):
            os.makedirs(savePath)
        #       检查dirPath 是否是个python包。如果不是则抛出异常
        if not '__init__.py' in os.listdir(pyPackage):
            raise ValueError('此包'+pyPackage+'下不存在__init__.py文件')
        # 自动获取文件的依赖包
        # 3.创建打包外的所用东西
        _createPackingFile(savePath,pyPackageName,pyPackage,options)

    def upload(self,user='',password=''):#上传

        pass

