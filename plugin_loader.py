from imp import *
import os
import inspect
import sys
from os.path import *
import types
import json

sys.path.append("./site-packages")

#Find this loader file path this should be a global variable
loader_root        = dirname(abspath(__file__))

plugins_root       = "plugins"
site_packages_root = "site-packages"
plugin_config_name = "plugin.json"
cmd_obj = sys.modules['__main__']

def cli_print(format, value):
    print format % value

def __import_plugin_cmd(module_name, plugin_name):

    module_path = join(plugins_root, module_name)
    plugin_path = join(plugins_root, module_name, plugin_name + '.py')

    #Load plugin module
    plugin_module = load_module(module_name, *find_module(plugin_name, [module_path]))

    #Get the command method and set it to command object
    methods = dir(plugin_module)
    for method in methods:
        if method.endswith("cmd"):
            method_obj = getattr(plugin_module, method)
            setattr(cmd_obj, method, method_obj)

    return plugin_module

def __load_module_from_package(package):

    #Find all python file in the package file
    package_path = os.path.join(plugins_root, package)

    plugin_files = os.listdir(package_path)

if __name__ == '__main__':

    __import_plugin_cmd("cli" ,"hello")

    import clime
    clime.start(white_pattern=clime.CMD_SUFFIX, debug=True)




