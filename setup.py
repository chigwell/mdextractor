from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='mdextractor',
    version='0.0.3',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='Extract Markdown code blocks from text strings.',
    long_description=long_description,
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
    license='MIT',
    tests_require=['unittest'],
    test_suite='test',
)
