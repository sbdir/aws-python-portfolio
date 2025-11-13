# lambda-hello-world

AWS Lambda（Python）で実装したシンプルな Hello API のサンプルです。  
API Gateway からの呼び出しを想定しています。

## 想定動作

- `GET /hello?name=Sota` のようなリクエストを受け取り、
- `{"message": "Hello, Sota!", "requested_at": "..."}` のような JSON を返します。

## デプロイイメージ

- ランタイム: Python 3.x
- ハンドラー: `handler.lambda_handler`
- トリガー: API Gateway（HTTP API / REST API いずれでも可）

※このリポジトリではインフラ定義（CDK / CloudFormation）は省略し、  
　Lambda 本体のコードイメージのみを掲載しています。
