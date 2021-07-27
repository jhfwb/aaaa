import os

from pyPacking_xhr import PackingTool
# PackingTool().create_packing_env(pyPackage='pyPacking_xhr')#为pyPacking_xhr这个软件生成打包环境
print(os.getcwd())
PackingTool().runningSetup(savePath='test')#为pyPacking_xhr这个软件生成打包环境




