from setuptools import setup, find_packages

setup(name='pysumma',
      version='3.0.0',
      description='A python wrapper for SUMMA',
      url='https://github.com/UW-Hydro/pysumma.git',
      author='YoungDon Choi, Andrew Bennett',
      author_email='choiyd1115@gmail.com, andrbenn@uw.edu',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'xarray>=0.11.0',	  
          'pandas',	  
          'netcdf4>=1.2.5',	  
          'numpy>=1.11.2',
          'dask',
          'distributed',
          'toolz',
          'pytest',		
          'matplotlib',
          'geopandas',
          'pandas',
          'hs_restclient',
          ],
       extras_require=[
          'fiona',
          'cartopy',	
          'shapely',
          'seaborn'
          ],
      include_package_data=True,
      test_suite='pysumma.tests')
