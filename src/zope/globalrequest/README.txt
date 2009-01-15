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

