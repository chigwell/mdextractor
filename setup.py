from setuptools import setup, find_packages

setup(
    name='mdextractor',
    version='0.0.2',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='Extract Markdown code blocks from text strings.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/mdextractor',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
