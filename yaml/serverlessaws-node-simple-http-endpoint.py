# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'serverless-simple-http-endpoint', 'frameworkVersion': '>=1.1.0 <2.0.0', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x'}, 'functions': {'currentTime': {'handler': 'handler.endpoint', 'events': [{'http': {'path': 'ping', 'method': 'get'}}]}}}