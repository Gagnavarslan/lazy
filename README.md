# Lazy

A library for lazy objects, started life as a coredata/contrib package.

## Release

Assuming you use virtualenvwrapper, you need to set up your environment,
prior to being able to release:

    mkvirtualenv lazy
    pip install -r requirements/release.txt

Now you can release, by changing version numbers in setup.py, and running:

    fab release

This will release the package to `pypi.coredata.is` (you will need VPN access
for that).
