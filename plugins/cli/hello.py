from random import randint
import ucltip

def __test_function(test_parameter):
    print "Use internal function is ok the parameter is %s!" % test_parameter

def hello_world_cmd(name):
    """Execute remote performance test.

    -n=<str> --name=<str>       Hello Name
    """
    print "hello world cmd %s" % name
    print "Test import random %d" % randint(0, 51)

def test_site_packages_cmd():
    echo = ucltip.Cmd("echo")
    print echo("Hello World ucltip")

    __test_function("test_parameter")