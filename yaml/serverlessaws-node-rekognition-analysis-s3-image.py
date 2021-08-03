# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'rekognition-analysis-s3-image', 'frameworkVersion': '>=1.10.0', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'memorySize': 512, 'timeout': 10, 'stage': 'dev', 'region': 'us-east-1', 'iamRoleStatements': [{'Effect': 'Allow', 'Action': ['s3:*'], 'Resource': '*'}, {'Effect': 'Allow', 'Action': ['rekognition:*'], 'Resource': '*'}]}, 'functions': {'imageAnalysis': {'handler': 'handler.imageAnalysis', 'events': [{'http': {'path': 'analysis', 'method': 'post'}}]}}}