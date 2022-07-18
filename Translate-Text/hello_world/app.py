import json
import boto3


def lambda_handler(event, context):
    
    client = boto3.client("translate", region_name="us-east-1")
    if "body" in event:
        event = json.loads(event["body"])
    phrase = event.get("phrase")
    lang_code = event.get("lang_code")
    result = client.translate_text(Text=phrase, SourceLanguageCode="auto", TargetLanguageCode=lang_code)
    translation = result["TranslatedText"]

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "Phrase": phrase,
                "Translation": translation
            }
        ),
    }
