from setuptools import setup, find_packages


exclude = ['sentinella.{{cookiecutter.plugin_name}}.{{cookiecutter.plugin_name}}']

install_requires = ['trollius==2.0']

setup(
    name='{{cookiecutter.plugin_name}}',
    description='{{cookiecutter.plugin_description}}',
    version='0.1',
    packages=find_packages(exclude=exclude),
    zip_safe=False,
    namespace_packages=['sentinella'],
    install_requires=install_requires,
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    url='{{cookiecutter.repo_url}}',
    license='ASF',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Monitoring',
    ],
    keywords='monitoring metrics agent openstack sentinella',
)
