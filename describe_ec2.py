#! /usr/bin/env python3
#################################################################################
#     File Name           :     describe_ec2.py
#     Created By          :     Eloi Silva
#     Creation Date       :     [2019-07-17 21:01]
#     Last Modified       :     [2020-11-10 15:24]
#     Description         :     Describe AWS EC2 Instance
#################################################################################

import boto3


def describe(*regions, state='running'):
    describe_format = ' {0} {1:<20s}{0} {2:<22s}{0} {3:<10s}{0} {4:<16s}{0} {5:<20s}{0} {6:<16s}{0}'
    describe_format_header = ' {0} {1:^20s}{0} {2:^22s}{0} {3:^10s}{0} {4:^16s}{0} {5:^20s}{0} {6:^16s}{0}'
    describe_format_header = describe_format_header.format('|', 'Name', 'InstanceId', 'State', 'PublicIP', 'SSH KeyName', 'AZ')
    print(' |%s|' % str((len(describe_format_header) - 3) * '-'))
    print(describe_format_header.format('|', 'Name', 'InstanceId', 'State', 'PublicIP', 'SSH KeyName', 'AZ'))
    print(' |%s|' % str((len(describe_format_header) - 3) * '-'))
    try:
        for region in regions:
            client = boto3.client(service_name='ec2', region_name=region)
            reservations = client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': [state]}]).get('Reservations')
            for instance in reservations:
                def ifname(instance):
                    if 'Tags' in instance and len(instance['Tags']) > 0:
                        tags = instance['Tags']
                        name = [tag['Value'] for tag in tags if tag['Key'] == 'Name']
                        if name: return name[0]
                    return 'None'

                def ifkey(instance, key):
                    if key in instance.keys():
                        return instance[key]
                    else:
                        return 'None'
                instance = instance['Instances'][0]
                instance_name = ifname(instance)
                instance_id = ifkey(instance, 'InstanceId')
                instance_key = ifkey(instance, 'KeyName')
                instance_state = ifkey(instance['State'], 'Name')
                ipaddr_public = ifkey(instance, 'PublicIpAddress')
                instance_az = ifkey(instance['Placement'], 'AvailabilityZone')
                print(describe_format.format('|', instance_name, instance_id, instance_state, ipaddr_public, instance_key, instance_az))
    except (KeyboardInterrupt, EOFError):
        pass
    except Exception as e:
        print(region, 'Error: ', e)
    print(' |%s|' % str((len(describe_format_header) - 3) * '-'))


if __name__ == '__main__':
    import sys
    state = 'running'
    state = '*'

    if len(sys.argv) > 1:
        regions_list = sys.argv[1:]
        describe(*regions_list, state=state)
    else:
        from regions import regions_list
        describe(*regions_list, state=state)
