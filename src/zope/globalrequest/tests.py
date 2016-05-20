from unittest import TestSuite
from zope.configuration import config
from zope.configuration import xmlconfig
from zope.testing.cleanup import cleanUp
import doctest
import zope.app.wsgi.testlayer
import zope.globalrequest


def zcml(source):
    context = config.ConfigurationMachine()
    xmlconfig.registerCommonDirectives(context)
    xmlconfig.string(source, context)


def tearDown(test):
    cleanUp()

testLayer = zope.app.wsgi.testlayer.BrowserLayer(zope.globalrequest)


def test_suite():
    flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    readme = doctest.DocFileSuite(
        'README.rst',
        package='zope.globalrequest',
        globs={
            'zcml': zcml},
        optionflags=flags,
        tearDown=tearDown)
    readme.layer = testLayer
    return TestSuite((readme,))
