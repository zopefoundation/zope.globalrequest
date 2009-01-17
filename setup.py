from setuptools import setup, find_packages
from os.path import join

version = '1.0a2'
readme = open(join('src', 'zope', 'globalrequest', 'README.txt')).read()
history = open('CHANGES.txt').read()

setup(name = 'zope.globalrequest',
      version = version,
      description = 'Global way of retrieving the currently active request.',
      long_description = readme[readme.find('\n\n'):] + '\n' + history,
      classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Zope2',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords = 'zope request global',
      author = 'Andreas Zeidler',
      author_email = 'az@zitc.de',
      url = 'http://pypi.python.org/pypi/zope.globalrequest',
      license = 'ZPL',
      packages = find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages = ['zope'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires = [
          'setuptools',
      ],
      extras_require = dict(
          test = [
              'zope.testing',
              'zope.configuration',
              'zope.app.publisher',
              'zope.app.securitypolicy',
              'zope.testbrowser',
          ],
      ),
      entry_points = '',
)
