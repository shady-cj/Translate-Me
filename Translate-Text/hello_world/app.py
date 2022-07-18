import json
import boto3


def lambda_handler(event, context):
    
    client = boto3.client("translate", region_name="us-east-1")
    body = json.loads(event["body"])
    phrase = body.get("phrase")
    lang_code = body.get("lang_code")
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
