#!/usr/bin/python3


import jk_version
import jk_php_version_parser
import jk_json



# ----------------------------------------------------------------
# Instantiate the parser

parser = jk_php_version_parser.ComposerVersionParser()

# ----------------------------------------------------------------
# Parse a version string

versionString = ">=0.1.2 <0.9 || 1.0 || 1.0.1 || >1.1.1"
constraint = parser.parse(versionString)

# ----------------------------------------------------------------
# For debugging purposes: Inspect details about the constraint

jk_json.prettyPrint(constraint.toJSON())

print()
print("-" * 120)
print()

# ----------------------------------------------------------------
# Check versions against the constraint

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

for version in versionList:
	print("Version  {:10}: {}".format(
		repr(str(version)),
		"match" if constraint.check(version) else "no match",
	))



