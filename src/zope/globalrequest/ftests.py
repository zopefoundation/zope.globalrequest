from zope.publisher.browser import BrowserPage
from zope.interface import Interface
from zope.component import queryUtility


class IFoo(Interface):
    """ interface for a foo-ish utility """

    def foo():
        """ return some foo """


class FooView(BrowserPage):
   """ a browser view """

   def __call__(self, *args, **kw):
       foo = queryUtility(IFoo, default=None)
       if foo is not None:
           return foo.foo()
       else:
           return 'sif!'

