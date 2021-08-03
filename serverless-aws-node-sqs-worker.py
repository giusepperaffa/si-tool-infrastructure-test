# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-node-sqs-worker', 'frameworkVersion': '2', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'lambdaHashingVersion': '20201221', 'stage': 'dev'}, 'constructs': {'jobs': {'type': 'queue', 'worker': {'handler': 'handler.consumer'}}}, 'functions': {'producer': {'handler': 'handler.producer', 'events': [{'http': {'method': 'post', 'path': 'produce'}}], 'environment': {'QUEUE_URL': '${construct:jobs.queueUrl}'}}}, 'plugins': ['serverless-lift']}