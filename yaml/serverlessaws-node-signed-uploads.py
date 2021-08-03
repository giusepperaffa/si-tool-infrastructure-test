# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'aws-node-signed-uploads', 'plugins': ['serverless-webpack', 'serverless-offline'], 'custom': {'bucketName': 'testbucket123notaken', 'webpack': {'webpackConfig': 'webpack.config.js', 'includeModules': True, 'packager': 'yarn'}, 'serverless-offline': {'port': 4000}}, 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'stage': "${opt:stage, env:AWS_STAGE, 'dev'}", 'region': "${opt:region, env:AWS_REGION, 'eu-central-1'}", 'environment': {'REGION': '${self:provider.region}', 'BUCKET': {'Ref': 'Uploads'}}, 'versionFunctions': False, 'iamRoleStatements': [{'Effect': 'Allow', 'Action': ['s3:*'], 'Resource': '*'}]}, 'functions': {'upsert-objects': {'handler': 'src/upload.handler', 'name': '${self:provider.stage}-${self:service}-upload', 'memorySize': 128, 'events': [{'http': {'path': 'upload', 'method': 'get', 'cors': True}}]}}, 'resources': {'Resources': {'Uploads': {'Type': 'AWS::S3::Bucket', 'Properties': {'BucketName': '${self:custom.bucketName}', 'CorsConfiguration': {'CorsRules': [{'AllowedHeaders': ['Authorization'], 'AllowedMethods': ['GET'], 'AllowedOrigins': ['*']}, {'AllowedHeaders': ['*'], 'AllowedMethods': ['PUT'], 'AllowedOrigins': ['*']}]}}}}}}