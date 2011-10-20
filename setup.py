__doc__ = """
An app that provides forms that automatically convert timezones into utc on submit, and (almost) automatically converts timezones into the local time
on render

See the README file for details, usage info, and a list of gotchas.
"""

from setuptools import setup

setup(
    name='django-timeforms',
    version='0.1',
    author='Ben Beecher',
    author_email='benbeecher@gmail.com',
    description=("""An app that provides forms that automatically convert timezones into utc on submit, and (almost) automatically converts timezones into the local time \
    on render"""),
    license='GPLv3',
    keywords='django timezones time',
    url='https://github.com/gone/django-timeforms',
    packages=['timeforms'],
    package_data={},
    long_description=__doc__,
    classifiers=[
    	'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ]
)
