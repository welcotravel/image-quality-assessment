from setuptools import setup
from setuptools import find_packages

setup(
  name='image_quality',
  version='0.1.0',
  description='image quality assessment',
  url='https://github.com/welcotravel/image-quality-assessment',
  author='victusfate',
  author_email='messel@gmail.com',
  license='Apache License 2.0',
  packages=find_packages(),
  install_requires = [
    
  ],
  # package_data={'image_quality': []},
  zip_safe=False
)
