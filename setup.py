from distutils.core import setup
import os

try:
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except IOError:
    long_description = """
# simple-tts

Simple TTS system for Windows, using Windows Speach API (SAPI) via win32com provided by pywin32 project.

See `README.md` for usage.

"""

# Build and publish to PyPI:
#   python setup.py sdist bdist_wheel
#   twine check dist/*
#   twine upload -r testpypi dist/*
#   twine upload -r pypi dist/*
setup(
    name='simple-tts',
    version='2020.04.01',
    packages=['simple_tts'],
    url='https://github.com/scholer/simple-tts',
    license='GNU General Public License v3 (GPLv3)',
    author='Rasmus Scholer Sorensen',
    author_email='rasmusscholer@gmail.com',
    description='Simple TTS system for Windows, using Windows Speech API via win32com (from pywin32 project).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'pywin32',
    ],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',

        # 'Topic :: Software Development :: Build Tools',
        'Topic :: Education',

        # Pick your license as you wish (should match "license" above)
        # 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'License :: OSI Approved :: GNU Affero General Public License v3',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

        'Operating System :: Microsoft',
        # 'Operating System :: MacOS',
        # 'Operating System :: POSIX :: Linux',
    ],

)
