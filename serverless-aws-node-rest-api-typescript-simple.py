# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'org': 'serverlessinc', 'app': 'aws-node-rest-api-typescript', 'service': 'aws-node-rest-api-typescript', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x'}, 'functions': {'hello': {'handler': 'handler.hello', 'events': [{'http': {'path': '/', 'method': 'get'}}]}}, 'plugins': ['serverless-plugin-typescript']}