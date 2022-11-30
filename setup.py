from setuptools import find_packages, setup
from flaskProject import __version__


setup(
    name='flaskProject',
    version=__version__,
    url='https://github.com/aimerkz/flaskProject.git',
    author='Artem Merkulov',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=False,
    data_files=[('/', ['main.py'])],
    install_requires=[
        'Flask==2.2.0',
        'Flask-Migrate==4.0.0',
        'Flask-RESTful==0.3.9',
        'Flask-SQLAlchemy==3.0.2',
        'flask-swagger-ui==4.11.1',
        'psycopg2-binary==2.9.5',
        'python-dotenv==0.21.0'
    ],
)
