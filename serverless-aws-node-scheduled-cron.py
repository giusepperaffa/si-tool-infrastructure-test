# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-node-scheduled-cron', 'frameworkVersion': '2', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'lambdaHashingVersion': 20201221}, 'functions': {'rateHandler': {'handler': 'handler.run', 'events': [{'schedule': 'rate(1 minute)'}]}, 'cronHandler': {'handler': 'handler.run', 'events': [{'schedule': 'cron(0/2 * ? * MON-FRI *)'}]}}}