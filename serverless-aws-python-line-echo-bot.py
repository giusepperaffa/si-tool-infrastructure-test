# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-python-line-echo-bot', 'provider': {'name': 'aws', 'runtime': 'python3.7'}, 'functions': {'line_bot': {'handler': 'handler.webhook', 'events': [{'http': {'path': '/webhook', 'method': 'POST'}}]}}, 'plugins': ['serverless-python-requirements']}