# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-node-twilio', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'environment': {'TWILIO_ACCOUNT_SID': 'YOUR-TWILIO-ACCOUNT-SID-HERE', 'TWILIO_AUTH_TOKEN': 'YOUR-TWILIO-AUTH-TOKEN-HERE', 'TWILIO_PHONE_NUMBER': 'YOUR-TWILIO-PHONE-NUMBER-HERE'}}, 'package': {'exclude': ['*.test.js', 'frontend/**']}, 'functions': {'sendText': {'handler': 'handler.sendText', 'events': [{'http': {'path': 'api/sendText', 'method': 'post', 'integration': 'lambda', 'cors': True}}]}}}