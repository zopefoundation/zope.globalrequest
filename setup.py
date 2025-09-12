from setuptools import setup


version = '3.0'

readme = open('README.rst').read()
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
        'Framework :: Zope :: 3',
        'Framework :: Zope :: 5',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords='zope request global',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.dev',
    url='https://github.com/zopefoundation/zope.globalrequest',
    project_urls={
        'Issue Tracker': ('https://github.com/zopefoundation/'
                          'zope.globalrequest/issues'),
        'Sources': 'https://github.com/zopefoundation/zope.globalrequest',
    },
    license='ZPL',
    include_package_data=True,
    platforms='Any',
    zip_safe=False,
    python_requires='>=3.9',
    install_requires=[
        'setuptools',
        'zope.interface',
        'zope.publisher',
        'zope.traversing',
    ],
    extras_require=dict(
        test=['zope.testrunner >= 6.4'],
    ),
)
