import boto3
from boto3.dynamodb.conditions import Key, Attr


def query(*, profile_name: str, api_name: str) -> None:
    session = boto3.Session(profile_name=profile_name)
    dynamodb = session.resource(
        "dynamodb",
        endpoint_url="http://localhost:8000",
    )

    table = dynamodb.Table("refdata-transform-api")
    try:
        res = table.query(
            KeyConditionExpression=Key("Apiname").eq(api_name)
        )
        print(f"[Client Result]: {res}")
    except Exception as e:
        print(f"[Client Errors]: {e}")


if __name__ == "__main__":
    query(
        profile_name="",
        api_name="",
    )
