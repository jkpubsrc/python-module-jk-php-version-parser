#!/usr/bin/python3




import jk_testing
import jk_json
import jk_version

import jk_php_version_parser






PARSER = jk_php_version_parser.ComposerVersionParser()





def _parseAndCompareJSON(ctx:jk_testing.TestContext, textToParse:str, jsonExpected):
	x = PARSER.parse(textToParse)
	assert isinstance(x, jk_version.BaseVersionConstraint)
	jsonReceived = x.toJSON()

	linesReceived = jk_json.dumps(jsonReceived, indent="\t", sort_keys=True).split("\n")
	linesExpected = jk_json.dumps(jsonExpected, indent="\t", sort_keys=True).split("\n")

	if jsonReceived == jsonExpected:
		ctx.log.debug("--input---" + "-" * 90)
		ctx.log.debug(textToParse)
		ctx.log.debug("--result--" + "-" * 90)
		for line in linesReceived:
			ctx.log.debug(line)
		ctx.log.debug("-" * 100)
		return

	ctx.log.warn("--input---" + "-" * 90)
	ctx.log.warn(textToParse)
	ctx.log.warn("--result--" + "-" * 90)
	for line in linesReceived:
		ctx.log.warn(line)
	ctx.log.warn("--expected" + "-" * 90)
	for line in linesExpected:
		ctx.log.warn(line)
	ctx.log.warn("-" * 100)

	raise jk_testing.AssertionException("received != expected!")
#






#
# Successes
#

@jk_testing.TestCase()
def test_parsing_elementar_1(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, ">= 1.2.3",
		[	">=",	"1.2.3"	]
	)
#

@jk_testing.TestCase()
def test_parsing_elementar_caret(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, "^1.2.3",
		[
			"and",
			[
				[	">=",	"1.2.3"	],
				[	"<",	"2.0.0"	],
			],
		]
	)
#

@jk_testing.TestCase()
def test_parsing_elementar_tilde(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, "~1.2.3",
		[
			"and",
			[
				[	">=",	"1.2.3"	],
				[	"<",	"1.3.0"	],
			],
		]
	)
#

@jk_testing.TestCase()
def test_parsing_multi_1(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, ">=1.2.3 <1.4",
		[
			"and",
			[
				[	">=",	"1.2.3"	],
				[	"<",	"1.4"	],
			],
		]
	)
#

@jk_testing.TestCase()
def test_parsing_multi_or(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, "1.2.3 || 1.2.5",
		[
			"or",
			[
				[	"==", "1.2.3",	],
				[	"==", "1.2.5",	],
			],
		]
	)
#

#
# ----
# Test Cases https://getcomposer.org/doc/articles/versions.md
# ----
#

@jk_testing.TestCase()
def test_parsing_composer_1(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, "1.3.2",
		[	"==", "1.3.2",	],
	)
#

@jk_testing.TestCase()
def test_parsing_composer_2(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, ">=1.3.2",
		[	">=", "1.3.2",	],
	)
#

@jk_testing.TestCase()
def test_parsing_composer_3(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, "<1.3.2",
		[	"<", "1.3.2",	],
	)
#

@jk_testing.TestCase()
def test_parsing_composer_4a(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, ">=1.3.0 <1.4.0",
		[
			"and",
			[
				[	">=", "1.3.0",	],
				[	"<", "1.4.0",	],
			]
		]
	)
#

@jk_testing.TestCase()
def test_parsing_composer_4b(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, "1.3.*",
		[
			"and",
			[
				[	">=", "1.3.0",	],
				[	"<", "1.4.0",	],
			]
		]
	)
#

@jk_testing.TestCase()
def test_parsing_composer_5a(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, ">=1.3.2 <1.4.0",
		[
			"and",
			[
				[	">=", "1.3.2",	],
				[	"<", "1.4.0",	],
			]
		]
	)
#

@jk_testing.TestCase()
def test_parsing_composer_5b(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, "~1.3.2",
		[
			"and",
			[
				[	">=", "1.3.2",	],
				[	"<", "1.4.0",	],
			]
		]
	)
#

@jk_testing.TestCase()
def test_parsing_composer_6a(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, ">=1.3.0 <2.0.0",
		[
			"and",
			[
				[	">=", "1.3.0",	],
				[	"<", "2.0.0",	],
			]
		]
	)
#

@jk_testing.TestCase()
def test_parsing_composer_6b(ctx:jk_testing.TestContext):
	x = PARSER.parse("~1.3")
	_parseAndCompareJSON(ctx, "~1.3",
		[
			"and",
			[
				[	">=", "1.3",	],
				[	"<", "2.0",		],
			]
		]
	)
#

@jk_testing.TestCase()
def test_parsing_composer_7a(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, ">=1.3.2 <2.0.0",
		[
			"and",
			[
				[	">=", "1.3.2",	],
				[	"<", "2.0.0",	],
			]
		]
	)
#

@jk_testing.TestCase()
def test_parsing_composer_7b(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, "^1.3.2",
		[
			"and",
			[
				[	">=", "1.3.2",	],
				[	"<", "2.0.0",	],
			]
		]
	)
#

@jk_testing.TestCase()
def test_parsing_composer_8a(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, ">=0.3.2 <0.4.0",
		[
			"and",
			[
				[	">=", "0.3.2",	],
				[	"<", "0.4.0",	],
			]
		]
	)
#

@jk_testing.TestCase()
def test_parsing_composer_8b(ctx:jk_testing.TestContext):
	_parseAndCompareJSON(ctx, "^0.3.2",
		[
			"and",
			[
				[	">=", "0.3.2",	],
				[	"<", "0.4.0",	],
			]
		]
	)
#

#
# Errors
#


# TODO



################################################################################################################################



testDriver = jk_testing.TestDriver()

results = testDriver.runTests([
	(test_parsing_elementar_1, True),
	(test_parsing_elementar_caret, True),
	(test_parsing_elementar_tilde, True),

	(test_parsing_multi_1, True),
	(test_parsing_multi_or, True),

	(test_parsing_composer_1, True),
	(test_parsing_composer_2, True),
	(test_parsing_composer_3, True),
	(test_parsing_composer_4a, True),
	(test_parsing_composer_4b, True),
	(test_parsing_composer_5a, True),
	(test_parsing_composer_5b, True),
	(test_parsing_composer_6a, True),
	(test_parsing_composer_6b, True),
	(test_parsing_composer_7a, True),
	(test_parsing_composer_7b, True),
	(test_parsing_composer_8a, True),
	(test_parsing_composer_8b, True),
])

reporter = jk_testing.TestReporterHTML()
reporter.report(results, webbrowserType="chromium")











