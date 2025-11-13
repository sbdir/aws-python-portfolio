import json
from datetime import datetime, timezone


def lambda_handler(event, context):
    """
    シンプルな Hello API。
    - event: API Gateway からのリクエスト情報
    - context: Lambda 実行コンテキスト

    戻り値は API Gateway HTTP API / REST API でそのままレスポンスになります。
    """
    # クエリパラメータから name を取得（なければ "World"）
    name = None
    if isinstance(event, dict):
        query = event.get("queryStringParameters") or {}
        name = query.get("name") if isinstance(query, dict) else None

    if not name:
        name = "World"

    now = datetime.now(timezone.utc).isoformat()

    body = {
        "message": f"Hello, {name}!",
        "requested_at": now,
        "input_event_sample": {
            "path": event.get("path") if isinstance(event, dict) else None,
            "httpMethod": event.get("httpMethod") if isinstance(event, dict) else None,
        },
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8"
        },
        "body": json.dumps(body, ensure_ascii=False),
    }
