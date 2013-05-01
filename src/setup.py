from distutils.core import setup

setup(
    name = 'CreateTables',
    version = '1.0',
    py_modules=['CreateTables'],
    description = 'Wrapper utility to create tables easily in HTML, spreadsheet, or PDF',
    author='Swara Technologies',
    author_email='swaratechnologies@outlook.com',
    url='https://github.com/swaratechnologies/CreateTables.git',
    long_description='CreateTables is a simple utlity wrapper over TableFactory. It provides support for parsing lists and thereby creating tables with them. An example is provided to easily demonstrate this functionality',
    keywords=['reports', 'pdf', 'spreadsheet', 'tables'],
    classifiers=[
        'Development Status :: 0 - Beta',
        'Environment :: Other Environment',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML',
        ],
    install_requires=['xlwt', 'ReportLab'],
        )
