from setuptools import setup, find_packages

setup(
    name='kinetopy',  
    version='1.0.0',  
    description='A tool for solid-state kinetics and generating plots',
    author='Sherif Ashraf Ahmed Hefney',
    author_email='Sherif1.se@gmail.com',
    packages=find_packages(),  
    install_requires=[  # Dependencies
        'pandas',
        'numpy',
        'scipy',
        'matplotlib',
        'openpyxl'
    ],
    entry_points={  
        'console_scripts': [
            'kinetopy=kinetopy:main',  
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        
    ],
    python_requires='>=3.6',  # Python version requirement
)
