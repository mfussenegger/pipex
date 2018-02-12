=====
pipex
=====

Pipex is a proof of concept application launcher for python. It automatically
creates a virtualenv and installs packages that are specified in the first
couple of lines of a python script::


    #!/usr/bin/env pipex
    # pipex --pkg crate

    from crate.client import connect

    conn = connect()
    c = conn.cursor()
    c.execute('select 1')
    print(c.fetchall())
