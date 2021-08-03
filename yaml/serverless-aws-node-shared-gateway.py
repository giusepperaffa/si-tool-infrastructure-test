# =========================
# Infrastructure Dictionary
# =========================
InfrastructureDict = {'service': 'shared-gateway', 'provider': {'name': 'aws', 'runtime': 'nodejs12.x', 'region': 'ap-southeast-1'}, 'resources': {'Resources': {'SharedGW': {'Type': 'AWS::ApiGateway::RestApi', 'Properties': {'Name': 'SharedGW'}}}, 'Outputs': {'apiGatewayRestApiId': {'Value': {'Ref': 'SharedGW'}, 'Export': {'Name': 'SharedGW-restApiId'}}, 'apiGatewayRestApiRootResourceId': {'Value': {'Fn::GetAtt': ['SharedGW', 'RootResourceId']}, 'Export': {'Name': 'SharedGW-rootResourceId'}}}}}