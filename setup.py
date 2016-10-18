from distutils.core import setup


setup(
    name='micropython-adafruit-ads1015',
    py_modules=['ads1x15'],
    version="1.0",
    description="Driver for MicroPython for the ADS1x15 ADC.",
    long_description="""\
MicroPython driver for the precision analog-to-digital converters ADS1015 and
ADS1115.""",
    author='Radomir Dopieralski',
    author_email='micropython@sheep.art.pl',
    classifiers = [
        'Development Status :: 6 - Mature',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
