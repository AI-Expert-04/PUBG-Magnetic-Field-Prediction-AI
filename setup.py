from setuptools import setup

setup(name='heatmappy.py',
      version='0.1',
      description='Package to combine image and heat map',
      url='http://github.com/durandtibo/heatmap',
      author='Thibaut Durand',
      author_email='durand.tibo@gmail.com',
      license='MIT',
      packages=['heatmappy.py'],
      install_requires=['numpy', 'scikit-image', 'scipy', 'matplotlib'],
      zip_safe=False)
