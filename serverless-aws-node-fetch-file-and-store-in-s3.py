# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'fetch-file-and-store-in-s3', 'frameworkVersion': '>=1.1.0', 'custom': {'bucket': '<your-bucket-name>'}, 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'stage': 'dev', 'region': 'us-west-1', 'iamRoleStatements': [{'Effect': 'Allow', 'Action': ['s3:PutObject', 's3:PutObjectAcl'], 'Resource': 'arn:aws:s3:::${self:custom.bucket}/*'}]}, 'functions': {'save': {'handler': 'handler.save', 'environment': {'BUCKET': '${self:custom.bucket}'}}}}