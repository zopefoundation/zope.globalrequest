zope.globalrequest
==================

Introduction
------------

This package provides a global way to retrieve the currently active request
object in a zope-based web framework.


Functional Tests
----------------

First we make sure our test view works:

  >>> from zope.testbrowser.testing import Browser
  >>> browser = Browser()
  >>> browser.open('http://localhost/@@foo')
  >>> browser.contents
  'sif!'

The view tries to query for a utility and use it to "calculate" it's response,
so let's define one:

  >>> from zope.interface import implements
  >>> from zope.globalrequest import ftests
  >>> from zope.globalrequest import getRequest
  >>> class Foo(object):
  ...     implements(ftests.IFoo)
  ...     def foo(self):
  ...         request = getRequest()
  ...         if request:
  ...             name = request.get('name', 'n00b')
  ...         else:
  ...             name = 'foo'
  ...         return 'y0 %s!' % name

Unfortunately the utility class cannot be directly imported from here, i.e.
relatively, so we have to make it available from somewhere else to register
the utility:

  >>> ftests.Foo = Foo
  >>> zcml("""
  ... <configure xmlns="http://namespaces.zope.org/zope">
  ...   <include package="zope.component" file="meta.zcml" />
  ...   <utility
  ...     factory="zope.globalrequest.ftests.Foo"
  ...     provides="zope.globalrequest.ftests.IFoo" />
  ... </configure>
  ... """)

Rendering the view again should now give us the default value provided by the
utility:

  >>> browser.reload()
  >>> browser.contents
  'y0 foo!'

Up to now the request hasn't been stored for us yet, so let's hook up the
necessary event subscribers and try that again:

  >>> zcml("""
  ... <configure xmlns="http://namespaces.zope.org/zope">
  ...   <include package="zope.component" file="meta.zcml" />
  ...   <include package="zope.globalrequest" />
  ... </configure>
  ... """)

Now we should get the request and therefore the fallback value from the form
lookup:

  >>> browser.reload()
  >>> browser.contents
  'y0 n00b!'

If we now provide a request value we should be greeted properly:

  >>> browser.open('?name=d4wg!')
  >>> browser.contents
  'y0 d4wg!!'

Once the request has been processed, it should not be available anymore:

  >>> print getRequest()
  None

