# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'text-analysis-via-sns-post-processing', 'frameworkVersion': '>=1.1.0 <2.0.0', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'region': 'us-east-1', 'stage': 'dev', 'iamRoleStatements': [{'Effect': 'Allow', 'Resource': '*', 'Action': ['sns:*']}]}, 'functions': {'addNote': {'handler': 'addNote.addNote', 'events': [{'http': {'path': 'notes', 'method': 'post', 'cors': True}}]}, 'analyzeNote': {'handler': 'analyzeNote.analyzeNote', 'events': [{'sns': 'analyzeNote'}]}}}