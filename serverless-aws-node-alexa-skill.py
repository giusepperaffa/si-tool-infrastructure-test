# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-node-alexa-skill', 'frameworkVersion': '>=1.4.0 <2.0.0', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x'}, 'functions': {'luckyNumber': {'handler': 'handler.luckyNumber', 'events': ['alexaSkill']}}}