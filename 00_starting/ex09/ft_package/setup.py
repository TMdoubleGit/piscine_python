from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    url='https://github.com/TMDoubleGit/ft_package',
    author='TMDoubleGit',
    author_email='tmichel-@42.student.fr',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ft_package = ft_package.__main__:main',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
