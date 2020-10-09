# MetaCharacters

.       => Any Character Except New Line
\d      => Digit (0=>9)
\D      => Not a Digit (0=>9)
\w      => Word Character (a=>z, A=>Z, 0=>9, _)
\W      => Not a Word Character
\s      => Whitespace (space, tab, newline)
\S      => Not Whitespace (space, tab, newline)

## Anchors

These don't match any characters, but rather indicate positions before or after a character

\b      => Word Boundary (whitespace or a non alphanumeric character)
\B      => Not a Word Boundary
^       => Beginning of a String
$       => End of a String

## Character Sets

[]      => Matches Characters in brackets
[^ ]    => Matches Characters NOT in brackets
|       => Either Or
( )     => Group

## Quantifiers

Quantifiers Indicate how many times do we want a character or pattern to repeat

*       => 0 or More
+       => 1 or More
?       => 0 or One
{3}     => Exact Number
{3,4}   => Range of Numbers (Minimum, Maximum)

## Sample Regexs

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
