# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-python-alexa-skill', 'frameworkVersion': '>=1.4.0 <2.0.0', 'provider': {'name': 'aws', 'runtime': 'python2.7'}, 'functions': {'luckyNumber': {'handler': 'handler.lucky_number', 'events': ['alexaSkill']}}}