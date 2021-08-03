# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': {'name': 'serverless-nest-example'}, 'plugins': ['@hewmen/serverless-plugin-typescript', 'serverless-plugin-optimize', 'serverless-offline'], 'provider': {'name': 'aws', 'runtime': 'nodejs12.x'}, 'package': {'individually': True}, 'functions': {'main': {'handler': 'src/main.handler', 'events': [{'http': {'method': 'any', 'path': '/{proxy+}'}}]}}}