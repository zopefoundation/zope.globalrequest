from unittest import TestSuite
from zope.configuration import config
from zope.configuration import xmlconfig
from zope.testing.cleanup import cleanUp
import doctest
import zope.app.wsgi.testlayer
import zope.testbrowser.wsgi
import zope.globalrequest


def zcml(source):
    context = config.ConfigurationMachine()
    xmlconfig.registerCommonDirectives(context)
    xmlconfig.string(source, context)


def tearDown(test):
    cleanUp()


#class WSGILayer(zope.app.wsgi.testlayer.BrowserLayer,
#    zope.testbrowser.wsgi.Layer):

#    def make_wsgi_app(self):
#        return super(WSGILayer, self).make_wsgi_app()


testLayer = zope.app.wsgi.testlayer.BrowserLayer(zope.globalrequest)

#zope.testbrowser.wsgi._APP_UNDER_TEST = testLayer.make_wsgi_app()

def test_suite():
    flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    readme = doctest.DocFileSuite(
        'README.rst',
        package='zope.globalrequest',
        globs={
            'zcml': zcml,
            'layer': testLayer},
        optionflags=flags,
        tearDown=tearDown)
    readme.layer = testLayer
    return TestSuite((readme,))
