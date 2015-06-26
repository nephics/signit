from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='signit',
    version='1.0.0',
    author='Jacob Svensson',
    author_email='jacob@nephics.com',
    packages=['signit'],
    url='https://github.com/nephics/signit',
    license='MIT License',
    description='Simple cryptographically signing and signature '
                'verification using HMAC-256.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)