.. module:: ads1x15

.. class:: ADS1115(i2c, address=0x49)

    .. attr:: gain

        Set the gain for all readings.

        The following values are possible:

        +-------+------+---------+
        | Value | Gain | Voltage |
        +=======+======+=========+
        | 0     | ⅔×   | 6.144V  |
        +-------+------+---------+
        | 1     | 1×   | 4.096V  |
        +-------+------+---------+
        | 2     | 2×   | 2.048V  |
        +-------+------+---------+
        | 3     | 4×   | 1.024V  |
        +-------+------+---------+
        | 4     | 8×   | 0.512V  |
        +-------+------+---------+
        | 5     | 16×  | 0.256V  |
        +-------+------+---------+

    .. method:: read(channel)

        Read voltage between a `channel` and `GND`.

        Takes 1ms. Returns a number between 0 and 65535.

    .. method:: diff(channel1, channel2)

        Read voltage between two channels.

        Takes 1ms. Returns a number between -65536 and 65535.

    .. method:: alert_start(channel, threshold)

        Start continuous measurement, set ALERT pin on threshold.

    .. method:: alert_read()

        Get the last reading from the continuous measurement.

.. class:: ADS1015(i2c, address=0x48)

    Same as :class:ADS1115, but returns 12-bit numbers (0-4095 and -4096-4095).

