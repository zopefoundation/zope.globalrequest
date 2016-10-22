from setuptools import setup, find_packages
from os.path import join

version = '1.3'

readme = open(join('src', 'zope', 'globalrequest', 'README.rst')).read()
changes = open('CHANGES.rst').read()

setup(
    name='zope.globalrequest',
    version=version,
    description='Global way of retrieving the currently active request.',
    long_description=readme[readme.find('\n\n'):] + '\n' + changes,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Zope2',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='zope request global',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    url='https://github.com/zopefoundation/zope.globalrequest',
    license='ZPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['zope'],
    include_package_data=True,
    platforms='Any',
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.interface',
        'zope.publisher',
        'zope.traversing',
    ],
    extras_require=dict(
        test=[
            'zope.browserpage',
            'zope.app.wsgi',
            'zope.configuration',
            'zope.principalregistry',
            'zope.testbrowser>=5.0',
            'zope.testing',
        ],
    ),
)
