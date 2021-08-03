# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-golang-simple-http-endpoint', 'frameworkVersion': '>=1.28.0 <2.0.0', 'provider': {'name': 'aws', 'runtime': 'go1.x'}, 'functions': {'hello': {'handler': 'bin/hello', 'events': [{'http': {'path': 'hello', 'method': 'get'}}]}, 'world': {'handler': 'bin/world', 'events': [{'http': {'path': 'world', 'method': 'get'}}]}}, 'package': {'exclude': ['./**'], 'include': ['./bin/**']}}