# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-lambda-and-heroku-postgres', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'stage': 'dev'}, 'functions': {'hello': {'handler': 'handler.hello', 'events': [{'http': 'GET hello'}, {'http': 'POST onrelease'}]}}}