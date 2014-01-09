import os
import sys

sys.path.insert(0,'lib')
from setuptools import setup, find_packages
from jnpr.netconify import __version__

requirements = [ 'jinja2', 'lxml', 'pyserial']

setup(
    name = "junos-netconify",
    namespace_packages = ['jnpr'],
    version = __version__,
    author = "Jeremy Schulman",
    author_email = "jschulman@juniper.net",
    description = ( "Junos console/bootstrap automation" ),
    license = "Apache 2.0",
    keywords = "Junos NETCONF networking automation",
    url = "http://www.github.com/jeremyschulman/py-junos-netconify",
    package_dir={'':'lib'},    
    packages=find_packages('lib'),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: Text Processing :: Markup :: XML'
    ],
)
