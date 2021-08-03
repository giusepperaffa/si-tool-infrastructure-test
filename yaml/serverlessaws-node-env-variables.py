# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'function-with-environment-variables', 'frameworkVersion': '>=1.2.0 <2.0.0', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'environment': {'EMAIL_SERVICE_API_KEY': 'KEYEXAMPLE1234'}}, 'functions': {'createUser': {'handler': 'handler.createUser', 'environment': {'PASSWORD_ITERATIONS': 4096, 'PASSWORD_DERIVED_KEY_LENGTH': 256}}, 'resetPassword': {'handler': 'handler.resetPassword'}}}