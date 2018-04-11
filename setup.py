from distutils.core import setup

setup(
    name='ororo-etl',
    version='0.1',
    author='Andrew Ho',
    author_email='andrew.kenneth.ho@gmail.com',
    license='GNU',
    description='ETL for the ororo project',
    packages=['extract'],
    long_description='Get weather data, transform it, and store it into some RDB',
    url='https://github.com/andrewkho/ororo-etl',
    keywords=['ororo', 'ororo-etl'],
    classifiers=[
        'Data Science, Weather',
    ],
    install_requires=[
        'requests', 'requests_oauthlib', 'urllib3', 'sqlalchemy', 'pandas', 'psycopg2'
    ]
)
