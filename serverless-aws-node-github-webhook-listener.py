# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'github-webhook-listener', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'environment': {'GITHUB_WEBHOOK_SECRET': 'REPLACE-WITH-YOUR-SECRET-HERE'}}, 'functions': {'githubWebhookListener': {'handler': 'handler.githubWebhookListener', 'events': [{'http': {'path': 'webhook', 'method': 'post', 'cors': True}}]}}}