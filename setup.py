import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='get_inertia',
    version='0.0.1',
    author='Guido Bocchio',
    author_email='guido@bocch.io',
    description='A simple tool to get the inertia matrix from a stl file.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bocchio/get_inertia',
    project_urls={
        'Bug Tracker': 'https://github.com/bocchio/get_inertia/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'numpy',
        'numpy-stl',
        'pint'
    ],
    scripts=['bin/get_inertia'],
    python_requires='>=2.7',
)
