Code Reference
==================

Options
^^^^^^^
Class to save all data related to an Option.

.. autoclass:: takeMyOption.options.OptionData
   :members:

   .. automethod:: __init__


Display Frame
^^^^^^^^^^^^^
Class for creating a complete frame of Display Options.

.. autoclass:: takeMyOption.displayFrame.DisplayFrame
   :members:


Display Formatter
^^^^^^^^^^^^^^^^^
The Default Display Format is given. Different Display Formats can be created in
similar fashion.

.. automodule:: takeMyOption.displayFormatters
   :members:

Input Strategies
^^^^^^^^^^^^^^^^
Ways to take Input from user in command line.

.. autoclass:: takeMyOption.inputStrategies.InputStrategies
   :members:

Exceptions
^^^^^^^^^^
Different Exceptions raised by other classes.

.. autoexception:: takeMyOption.exceptions.OptionException
   :members:

.. autoexception:: takeMyOption.exceptions.DisplayFrameException
   :members:

.. autoexception:: takeMyOption.exceptions.InputStrategiesException
   :members:
