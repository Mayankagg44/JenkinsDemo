import boto3

#Describe RDS
def status_rds():
    client = boto3.client('rds')
    response = client.describe_db_instances(
        DBInstanceIdentifier='database-1'
    )
    print(response)

    for i in response['DBInstances']:
        if i['DBInstanceStatus'] == 'Available':
            client.stop_db_instance(DBInstanceIdentifier = i['DBInstanceIdentifier'])
            print('stopping DB instance {0}'.format(i['DBInstanceIdentifier']))
        elif i['DBInstanceStatus'] == 'stopped':
            client.start_db_instance(DBInstanceIdentifier = i['DBInstanceIdentifier'])
            print('starting DB instance {0}'.format(i['DBInstanceIdentifier']))
        elif i['DBInstanceStatus']=='starting':
            print('DB Instance {0} is in starting state. Please stop the cluster after starting is complete'.format(i['DBInstanceIdentifier']))
        elif i['DBInstanceStatus']=='stopping':
            print('DB Instance {0} is already in stopping state.'.format(i['DBInstanceIdentifier']))

status_rds()
