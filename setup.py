from setuptools import setup
import pkg_resources


def get_description():
    return 'Tool for populating ubi repositories'


def get_long_description():
    with open('README.md') as f:
        text = f.read()

    # Long description is everything after README's initial heading
    idx = text.find('\n\n')
    return text[idx:]


def get_rpm_distribution():
    for distribution in ['rpm', 'rpm-python']:
        try:
            pkg_resources.get_distribution(distribution)
        except pkg_resources.DistributionNotFound:
            continue
        else:
            return distribution
    return 'rpm-py-installer'


def get_requirements():
    requirements = [get_rpm_distribution()]

    with open('requirements.txt') as f:
        requirements.extend(f.read().splitlines())

    return requirements


setup(name='ubi-population-tool',
      version='0.1.18',
      license='GNU General Public License',
      author='',
      author_email='',
      description=get_description(),
      long_description=get_long_description(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      url="https://github.com/release-engineering/ubi-population-tool",
      install_requires=get_requirements(),
      packages=['ubipop'],
      entry_points={
          'console_scripts': [
              'ubipop = ubipop.cli:entry_point',
          ]
      }
      )
