#!/usr/bin/python3




import jk_testing
import jk_version

import jk_php_version_parser





tokenizer = jk_php_version_parser.ComposerVersionTokenizer()





#
# Successes
#

@jk_testing.TestCase()
def test_tokenizing_version_1(ctx:jk_testing.TestContext):
	tokenStream = tokenizer.tokenize("1.2.3")
	tokenStream.dump(printFunc=ctx.log.debug)

	jk_testing.Assert.isEqual(len(tokenStream), 1)

	jk_testing.Assert.isNotNone(
		tokenStream.tryMatchSequence(
			jk_php_version_parser._ComposerTokenPattern("v", "1.2.3"),
		)
	)
#

@jk_testing.TestCase()
def test_tokenizing_version_2(ctx:jk_testing.TestContext):
	tokenStream = tokenizer.tokenize("1.2.3 2.3.4")
	tokenStream.dump(printFunc=ctx.log.debug)

	jk_testing.Assert.isEqual(len(tokenStream), 2)

	jk_testing.Assert.isNotNone(
		tokenStream.tryMatchSequence(
			jk_php_version_parser._ComposerTokenPattern("v", "1.2.3"),
			jk_php_version_parser._ComposerTokenPattern("v", "2.3.4"),
		)
	)
#

@jk_testing.TestCase()
def test_tokenizing_ge(ctx:jk_testing.TestContext):
	tokenStream = tokenizer.tokenize(">= 1.2.3")
	tokenStream.dump(printFunc=ctx.log.debug)

	jk_testing.Assert.isEqual(len(tokenStream), 2)

	jk_testing.Assert.isNotNone(
		tokenStream.tryMatchSequence(
			jk_php_version_parser._ComposerTokenPattern("op", ">="),
			jk_php_version_parser._ComposerTokenPattern("v", "1.2.3"),
		)
	)
#

@jk_testing.TestCase()
def test_tokenizing_gt(ctx:jk_testing.TestContext):
	tokenStream = tokenizer.tokenize("> 1.2.3")
	tokenStream.dump(printFunc=ctx.log.debug)

	jk_testing.Assert.isEqual(len(tokenStream), 2)

	jk_testing.Assert.isNotNone(
		tokenStream.tryMatchSequence(
			jk_php_version_parser._ComposerTokenPattern("op", ">"),
			jk_php_version_parser._ComposerTokenPattern("v", "1.2.3"),
		)
	)
#

@jk_testing.TestCase()
def test_tokenizing_le(ctx:jk_testing.TestContext):
	tokenStream = tokenizer.tokenize("<= 1.2.3")
	tokenStream.dump(printFunc=ctx.log.debug)

	jk_testing.Assert.isEqual(len(tokenStream), 2)

	jk_testing.Assert.isNotNone(
		tokenStream.tryMatchSequence(
			jk_php_version_parser._ComposerTokenPattern("op", "<="),
			jk_php_version_parser._ComposerTokenPattern("v", "1.2.3"),
		)
	)
#

@jk_testing.TestCase()
def test_tokenizing_lt(ctx:jk_testing.TestContext):
	tokenStream = tokenizer.tokenize("< 1.2.3")
	tokenStream.dump(printFunc=ctx.log.debug)

	jk_testing.Assert.isEqual(len(tokenStream), 2)

	jk_testing.Assert.isNotNone(
		tokenStream.tryMatchSequence(
			jk_php_version_parser._ComposerTokenPattern("op", "<"),
			jk_php_version_parser._ComposerTokenPattern("v", "1.2.3"),
		)
	)
#

@jk_testing.TestCase()
def test_tokenizing_range(ctx:jk_testing.TestContext):
	tokenStream = tokenizer.tokenize("1.2.3 - 2.3.4")
	tokenStream.dump(printFunc=ctx.log.debug)

	jk_testing.Assert.isEqual(len(tokenStream), 3)

	jk_testing.Assert.isNotNone(
		tokenStream.tryMatchSequence(
			jk_php_version_parser._ComposerTokenPattern("v", "1.2.3"),
			jk_php_version_parser._ComposerTokenPattern("op", "-"),
			jk_php_version_parser._ComposerTokenPattern("v", "2.3.4"),
		)
	)
#

@jk_testing.TestCase()
def test_tokenizing_version_wildcard(ctx:jk_testing.TestContext):
	tokenStream = tokenizer.tokenize("1.2.*")
	tokenStream.dump(printFunc=ctx.log.debug)

	jk_testing.Assert.isEqual(len(tokenStream), 1)

	jk_testing.Assert.isNotNone(
		tokenStream.tryMatchSequence(
			jk_php_version_parser._ComposerTokenPattern("v", "1.2.*"),
		)
	)
#

@jk_testing.TestCase()
def test_tokenizing_version_gt_wildcard(ctx:jk_testing.TestContext):
	tokenStream = tokenizer.tokenize(">=1.2.*")
	tokenStream.dump(printFunc=ctx.log.debug)

	jk_testing.Assert.isEqual(len(tokenStream), 2)

	jk_testing.Assert.isNotNone(
		tokenStream.tryMatchSequence(
			jk_php_version_parser._ComposerTokenPattern("op", ">="),
			jk_php_version_parser._ComposerTokenPattern("v", "1.2.*"),
		)
	)
#

@jk_testing.TestCase()
def test_tokenizing_version_caret(ctx:jk_testing.TestContext):
	tokenStream = tokenizer.tokenize("^1.2.3")
	tokenStream.dump(printFunc=ctx.log.debug)

	jk_testing.Assert.isEqual(len(tokenStream), 2)

	jk_testing.Assert.isNotNone(
		tokenStream.tryMatchSequence(
			jk_php_version_parser._ComposerTokenPattern("op", "^"),
			jk_php_version_parser._ComposerTokenPattern("v", "1.2.3"),
		)
	)
#

@jk_testing.TestCase()
def test_tokenizing_version_tilde(ctx:jk_testing.TestContext):
	tokenStream = tokenizer.tokenize("~1.2.3")
	tokenStream.dump(printFunc=ctx.log.debug)

	jk_testing.Assert.isEqual(len(tokenStream), 2)

	jk_testing.Assert.isNotNone(
		tokenStream.tryMatchSequence(
			jk_php_version_parser._ComposerTokenPattern("op", "~"),
			jk_php_version_parser._ComposerTokenPattern("v", "1.2.3"),
		)
	)
#




#
# Errors
#


# TODO



################################################################################################################################



testDriver = jk_testing.TestDriver()

results = testDriver.runTests([
	(test_tokenizing_version_1, True),
	(test_tokenizing_version_2, True),
	(test_tokenizing_ge, True),
	(test_tokenizing_gt, True),
	(test_tokenizing_le, True),
	(test_tokenizing_lt, True),
	(test_tokenizing_range, True),
	(test_tokenizing_version_wildcard, True),
	(test_tokenizing_version_gt_wildcard, True),
	(test_tokenizing_version_caret, True),
	(test_tokenizing_version_tilde, True),
	#(test_OR, True),
	#(test_AND, True),
])

reporter = jk_testing.TestReporterHTML()
reporter.report(results, webbrowserType="chromium")











