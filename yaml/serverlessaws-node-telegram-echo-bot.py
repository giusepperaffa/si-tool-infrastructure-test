# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-node-telegram-echo-bot', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x'}, 'functions': {'webhook': {'handler': 'handler.webhook', 'events': [{'http': {'path': 'webhook', 'method': 'post'}}]}}}