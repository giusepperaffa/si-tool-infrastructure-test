# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-python-rest-api', 'frameworkVersion': '2', 'provider': {'name': 'aws', 'runtime': 'python3.8', 'lambdaHashingVersion': '20201221'}, 'functions': {'hello': {'handler': 'handler.hello', 'events': [{'http': {'path': '/', 'method': 'get'}}]}}}