# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'serve-dynamic-html-via-http-endpoint', 'frameworkVersion': '>=1.1.0 <2.0.0', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x'}, 'functions': {'landingPage': {'handler': 'handler.landingPage', 'events': [{'http': {'method': 'get', 'path': 'landing-page'}}]}}}