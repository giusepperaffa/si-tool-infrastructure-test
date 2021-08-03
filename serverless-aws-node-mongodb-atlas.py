# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'my-service', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x'}, 'functions': {'hello': {'handler': 'handler.hello', 'events': [{'http': 'GET hello'}]}}}