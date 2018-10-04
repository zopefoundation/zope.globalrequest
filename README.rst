zope.globalrequest
==================

Introduction
------------

This package provides a contextless way to retrieve the currently active request object in a zope-based web framework.
To do so you simply need to do the following::

    from zope.globalrequest import getRequest
    request = getRequest()

This package is mainly intended to be used with the Zope/Plone stack.
While it also works with the Zope3 framework,
the latter promotes a clean separation of concerns and the pattern of having a globally available request object is discouraged.
