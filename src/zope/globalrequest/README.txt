zope.globalrequest
==================

Introduction
------------

This package provides a global way to retrieve the currently active request
object in a zope-based web framework.

Let's just check the interfaces for now:

  >>> from zope.globalrequest.interfaces import IGlobalRequest
  >>> IGlobalRequest
  <InterfaceClass zope.globalrequest.interfaces.IGlobalRequest>

Also make sure our test view works:

  >>> from zope.testbrowser.testing import Browser
  >>> browser = Browser()
  >>> browser.open('http://localhost/@@foo')
  >>> browser.contents
  'sif!'

The view tries to query for a utility and use it to "calculate" it's response,
so let's define one:

  >>> from zope.interface import implements
  >>> from zope.globalrequest import ftests
  >>> class Foo(object):
  ...     implements(ftests.IFoo)
  ...     def foo(self):
  ...         return 'foo!'

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

Rendering the view again should now give us the value provided by the utility:

  >>> browser.reload()
  >>> browser.contents
  'foo!'

