import boto3
import sys

status = sys.argv[1]
#Describe RDS
def status_rds():
    client = boto3.client('rds')
    response = client.describe_db_instances(
        DBInstanceIdentifier='database-1'
    )
    print(response)

    for i in response['DBInstances']:
        if status =='start':
            if i['DBInstanceStatus'] == 'Available' or i['DBInstanceStatus'] == 'starting':
                print("Already start")
                sys.exit(1)
            else:
                client.start_db_instance(DBInstanceIdentifier = i['DBInstanceIdentifier'])
                print('starting DB instance {0}'.format(i['DBInstanceIdentifier']))          
        if status =='stop':
            if i['DBInstanceStatus'] == 'stopped' or i['DBInstanceStatus'] == 'stopping':
                print("Already stopped")
                sys.exit(1)
            else:
                client.start_db_instance(DBInstanceIdentifier = i['DBInstanceIdentifier'])
                print('starting DB instance {0}'.format(i['DBInstanceIdentifier']))

status_rds()
