from unittest import TestSuite
from zope.testing.doctest import DocFileSuite
from zope.testing.cleanup import cleanUp


def tearDown(test):
    cleanUp()

def test_suite():
    return TestSuite([
        DocFileSuite('README.txt', package='zope.globalrequest',
            tearDown=tearDown)
    ])

