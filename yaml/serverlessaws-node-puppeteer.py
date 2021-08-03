# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'scrapper-lambda', 'provider': {'name': 'aws', 'profile': '<your aws profile>', 'runtime': 'nodejs12.x'}, 'plugins': ['serverless-offline', 'serverless-plugin-chrome'], 'package': {'exclude': ['node_modules/puppeteer/.local-chromium/**']}, 'functions': {'hello': {'handler': 'handler.hello', 'memorySize': '1536MB', 'timeout': 30, 'events': [{'http': {'path': '/', 'method': 'get'}}]}}}