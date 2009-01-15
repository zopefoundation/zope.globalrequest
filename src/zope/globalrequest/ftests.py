from zope.publisher.browser import BrowserPage


class FooView(BrowserPage):
   """ a browser view """

   def __call__(self, *args, **kw):
       return 'sif!'

