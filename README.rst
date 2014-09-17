.. image:: https://badge.fury.io/py/alarm.png
    :target: http://badge.fury.io/py/alarm
.. image:: https://pypip.in/d/alarm/badge.png
    :target: https://pypi.python.org/pypi/alarm
.. image:: https://pypip.in/license/alarm/badge.png
    :target: https://pypi.python.org/pypi/alarm


CLI Alarm Clock
===============

Alarm is CLI utility written in Python language.

Requirements
------------

.. code-block:: bash

    - Python 2 or 3
    - Mplayer


Installation
------------

Using `pip <https://pip.pypa.io/en/latest/>`_ :

.. code-block:: bash

    $ pip install alarm

    uninstall:

    $ pip uninstall alarm
   

Command Line Tool Usage
-----------------------

.. code-block:: bash

    usage: alarm [-h] [-v]
                 [-s] <day> <alarm time> <song>

    optional arguments
      -h, --help       show this help message and exit
      -v, --version    print version and exit
      -s, --set        set alarm day, time and sound
    
    example: alarm -s 17 06:00 /path/to/song.mp3


Example:

.. code-block:: bash
   
    $ alarm -s 17 22:05 ~/Music/xristina.ogg

    +==============================================================================+
    |                              CLI Alarm Clock                                 |
    +==============================================================================+
    | Alarm set at : Wednesday 22:05                                               |
    | Sound file : /home/dslackw/Music/xristina.ogg                                |
    | Time : 21:06:41                                                              |
    +==============================================================================+
