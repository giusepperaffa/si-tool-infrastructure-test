# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'serverless-side-rendering-vue-nuxt', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'stage': '${self:custom.secrets.NODE_ENV}', 'region': 'us-east-1', 'environment': {'NODE_ENV': '${self:custom.secrets.NODE_ENV}'}}, 'functions': {'nuxt': {'handler': 'index.nuxt', 'events': [{'http': 'ANY /'}, {'http': 'ANY /{proxy+}'}]}}, 'plugins': ['serverless-apigw-binary', 'serverless-offline'], 'custom': {'secrets': '${file(secrets.json)}', 'apigwBinary': {'types': ['*/*']}}}