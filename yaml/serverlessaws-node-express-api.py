# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-node-express-api', 'frameworkVersion': '2', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'lambdaHashingVersion': '20201221'}, 'functions': {'api': {'handler': 'handler.handler', 'events': [{'http': {'path': '/', 'method': 'ANY'}}, {'http': {'path': '/{proxy+}', 'method': 'ANY'}}]}}}