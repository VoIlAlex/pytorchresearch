from distutils.core import setup
setup(
    name='pytorchresearch',         # How you named your package folder (MyLib)
    packages=['pytorchresearch'],   # Chose the same as "name"
    # Start with a small number and increase it with every change you make
    version='1.0.0-alpha',
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Tools to automate research with PyTorch framework',
    author='Ilya Vouk',                   # Type in your name
    author_email='ilya.vouk@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/VoIlAlex/pytorchresearch',
    # I explain this later on
    download_url='https://github.com/VoIlAlex/pytorchresearch/archive/v1.0.0-alpha.tar.gz',
    # Keywords that define your package best
    keywords=['framework', 'automation', 'research', 'science',
              'machine learning', 'deep learning', 'pytorch'],
    install_requires=[            # I get to this in a second
        'numpy',
        'matplotlib',
        'torch'
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which python versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
