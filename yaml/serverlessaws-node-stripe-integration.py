# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-node-stripe-integration', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'stage': 'test', 'region': 'us-east-1'}, 'package': {'include': ['config/**', 'node_modules/**'], 'exclude': ['package.json']}, 'functions': {'incoming': {'handler': 'handler.incoming', 'events': [{'http': {'path': 'stripe/incoming', 'method': 'post'}}]}}}