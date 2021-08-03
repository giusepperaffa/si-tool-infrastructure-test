# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'upload-to-s3-and-postprocess', 'frameworkVersion': '>=1.1.0', 'custom': {'bucket': '<your-bucket-name>'}, 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'iamRoleStatements': [{'Effect': 'Allow', 'Action': ['s3:*'], 'Resource': '*'}]}, 'functions': {'postprocess': {'handler': 'handler.postprocess', 'events': [{'s3': {'bucket': '${self:custom.bucket}', 'event': 's3:ObjectCreated:*', 'rules': [{'suffix': '.png'}]}}]}}}