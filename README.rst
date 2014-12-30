SQLCompletion
=============

A library to analyze SQL statements and provide completion categories.

Usage:
------

.. code:: Python

    suggest_type(full_text, cursor_pos=None)

If the cursor_pos is None then it is assumed to be at the end of the line.

returns a tuple that has two lists (['type'], ['scope']). 

A type is a category of SQL token such as 'tables', 'columns', 'keywords',
'functions', etc.

eg:

.. code:: Python

    >> suggest_type('SELECT * FROM ')
    (['tables'], [])
    
    >> suggest_type('SELECT  FROM abc', 7) # Cursor is after 'SELECT '
    (['columns', 'functions'], ['abc'])

It will resolve aliases and suggest the real table name.

.. code:: Python

    >> suggest_type('SELECT a. FROM abc a', 10) # Cursor is at 'SELECT a.'
    (['columns'], ['abc'])
