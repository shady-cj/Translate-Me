# Translate-Me

## INTRODUCTION

A simple project for text translation... You can translate a text from any language to a language of your choice This uses boto3 api for the translation thus a requirement.

## REQUIREMENTS
* **python** - Required to start the application
* **boto3** - To run the boto3 api client
* **click** - To provide a more interactive prompt to the user

## USAGE
Making sure a files are present.
Simply run
`python translate.py`
User will be prompted for the text to be translated... and the language to translate to.
For the language you should use the language code e.g en for English.. You can check out [Language Codes](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html) For more options

Another way to use this function is through a feature provided by **click**

`python translate.py --phrase "oui" --lang "en"`

From the above the phrase is _oui_ which is a french word and my language option is _en_ which is the code for english. The output result is **YES**.


