# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'tenant': 'ac360', 'app': 'enterprise', 'service': 'demo-email-form', 'frameworkVersion': '>=1.38.0 <2.0.0', 'provider': {'name': 'aws', 'runtime': 'nodejs10.x'}, 'functions': {'formSubmit': {'handler': 'index.submit', 'events': [{'http': {'path': 'submit', 'method': 'post', 'cors': True}}]}}, 'plugins': None}