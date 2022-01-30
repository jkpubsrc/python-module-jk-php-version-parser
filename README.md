jk_php_version_parser
==========

Introduction
------------

This python module implements version parsing as defined by the PHP tool `composer`.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/python-module-jk-php-version-parser)
* [pypi.python.org](https://pypi.python.org/pypi/jk_php_version_parser)

Why this module?
----------------

Python is an excellent language to support management of data, software packages, etc.
Not only PHP `composer` but even some data/software packages provide version information in PHP `composer` notation.
This module has been written to parse this data.

Functionality
--------------------------

This module implements all aspects of the specification provided at:
* https://getcomposer.org/doc/articles/versions.md

This module parses all kinds of valid version notation and produces objects of type `jk_version.BaseVersionConstraint`
(which is the base class for version constraints provided by module `jk_version`). This way this module aids in
validations of versions modeled by instances of `jk_version.Version`.

How to use this module
----------------------

### Import this module

Please include this module into your application by using the following code:

```python
import jk_php_version_parser
```

However, as version and constraint objects are provided by module `jk_version` you will likely need to access classes
provided by `jk_version` as well. Therefore it is recommended to import `jk_version` as well:

```python
import jk_version
```

### Instantiate the parser

Now the first thing you need to do is to instantiate a parser:

```python
parser = jk_php_version_parser.ComposerVersionParser()
```

### Parse a version string

Now the parser is ready for parsing. Here is an example of how to do that:

```python
versionString = ">=0.1.2 <0.9 || 1.0 || 1.0.1 || >1.1.1"
constraint = parser.parse(versionString)
```

Now you received a constraint you can match against a specific version later.

### For debugging purposes: Inspect details about the constraint

However, you might want to first inspect details about this constraint for debugging purposeses. You can easily do this
by serializing the constraint to a JSON data structure. The constraint objects from `jk_version` provide a very suitable
method for this purpose: `toJSON()`. The data returend can then be prettyprinted, e.g. with `jk_json.prettyPrint(..)`:

```python
import jk_json
jk_json.prettyPrint(constraint.toJSON())
```

In this particular example the printed JSON will look like this:

```JSON
[
	"or",
	[
		[
			"and",
			[
				[
					">=",
					"0.1.2"
				],
				[
					"<",
					"0.9"
				]
			]
		],
		[
			"==",
			"1.0"
		],
		[
			"==",
			"1.0.1"
		],
		[
			">",
			"1.1.1"
		]
	]
]
```

### Check versions against the constraint

First of all we need some versions we can check. For demonstration purposes let's create a list of some versions:

```python
versionList = [
	jk_version.Version("0.1.1"),
	jk_version.Version("0.1.2"),
	jk_version.Version("1.0"),
	jk_version.Version("1.0.0"),
	jk_version.Version("1.0.1"),
	jk_version.Version("1.1"),
	jk_version.Version("1.1.1"),
	jk_version.Version("1.2"),
]
```

Now we can check the versions:

```python
for version in versionList:
	print("Version  {:10}: {}".format(
		repr(str(version)),
		"match" if constraint.check(version) else "no match",
	))
```

This will generate the following output:

```
Version  '0.1.1'   : no match
Version  '0.1.2'   : match
Version  '1.0'     : match
Version  '1.0.0'   : match
Version  '1.0.1'   : match
Version  '1.1'     : no match
Version  '1.1.1'   : no match
Version  '1.2'     : match
```

Compatible Modules
-------------------

Version number parsers:
* [jk_version](https://github.com/jkpubsrc/python-module-jk-version)

Contact Information
-------------------

* Jürgen Knauth: pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



