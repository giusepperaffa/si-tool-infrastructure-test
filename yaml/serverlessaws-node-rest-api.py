# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-node-rest-api', 'frameworkVersion': '2', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'lambdaHashingVersion': '20201221'}, 'functions': {'hello': {'handler': 'handler.hello', 'events': [{'http': {'path': '/', 'method': 'get'}}]}}}