# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'hellotime-app', 'provider': {'name': 'aws'}, 'functions': {'hello': {'runtime': 'python3.6', 'events': [{'http': {'method': 'get', 'path': 'greet'}}], 'handler': 'web/handler.hello'}, 'time': {'runtime': 'nodejs12.x', 'events': [{'http': {'method': 'get', 'path': 'time'}}], 'handler': 'api/handler.timestamp'}}}