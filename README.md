Repository of CLI mixins
========================

Various command line options are tedious to write and/or difficult to remember.
To make common command line options easier to invoke this repository makes
these "shortcuts" available, e.g. for the command line tool `colcon`.

How to fetch the information
----------------------------

To register this repository with `colcon` (using the identifier "default")
invoke the following command:

```
colcon mixin add default https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml
```

Afterwards as well as on a regular base fetch the latest content from the
repository:

```
colcon mixin update default
```

How to use the information
--------------------------

To show the mixins available and their mapping invoke the following command:

```
colcon mixin show
```

To apply CLI mixins pass the option `--mixin` to the colcon verb followed by
the names of the mixins.

How to contribute additional information
----------------------------------------

Initially fork this repository.
For each contribution perform the following steps:

* Create or modify one or multiple files ending with `.mixin`.
* Add any new files in alphabetical order to the `index.yaml` file.
* Run the `lint.py` script to ensure that the changes follow the recommended
  yaml style.
* Create a pull request with the changes.
