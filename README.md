PyPI Alfred Workflow for [Alfred 2](http://www.alfredapp.com)
=============================================================

This workflow allows you to search the PyPI API for packages by name only currently.

There are 2 commands avalible to you:

* pypi
* pip

The ``pypi`` Command
--------------------

The ``pypi`` command will search the PyPI API, this seems to not deliver the same results as the web front end of
pypi.python.org. Once the list of packages matching the name has been given pressing ``enter`` will open the
url to that package in your default browser.

![PyPi Workflow Screenshot](http://pypiworkflow.chris.reeves.io/pypi_flask.png)

The ``pip`` Command
-------------------

The ``pip`` command operates in the same way in the sense that it queroes PyPi for packages. However pressing enter
will copy to your clipboard the ``pip install`` command for the package you have selected. This will alos include
the version of the the package is currently at.

![Pip Workflow Screenshot](http://pypiworkflow.chris.reeves.io/pip_flask.png)
