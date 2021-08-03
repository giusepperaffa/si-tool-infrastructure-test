# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'websocket-authorizer-example', 'provider': {'name': 'aws', 'stage': 'dev', 'runtime': 'nodejs12.x'}, 'functions': {'connect': {'handler': 'handler.connect', 'events': [{'websocket': {'route': '$connect', 'authorizer': {'name': 'auth', 'identitySource': ['route.request.header.Auth']}}}]}, 'default': {'handler': 'handler.default', 'events': [{'websocket': {'route': '$default'}}]}, 'auth': {'handler': 'handler.auth'}}}