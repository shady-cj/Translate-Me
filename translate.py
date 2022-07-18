import boto3
import click

@click.command()
@click.option("--phrase", prompt="Enter the text to be translated here", help="A tool to translate text")
@click.option("--lang", prompt="Enter the language code to be translated to", help="The language to code that you want to translate your phrase to")
def translate(phrase, lang):
    client = boto3.client("translate", region_name = "us-east-1")
    click.echo(click.style(f"Your phrase: {phrase}",fg="red"))
    result=client.translate_text(Text=phrase, SourceLanguageCode="auto", TargetLanguageCode=lang)
    
    translation = result["TranslatedText"]
    click.echo(click.style(f"Translated To: {translation}", fg="white", bg="red"))


if __name__ == "__main__":
    translate()
