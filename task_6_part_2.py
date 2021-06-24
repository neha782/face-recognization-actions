
import boto3

#Python Program for creating a connection

ec2 = boto3.client('ec2',
                'ap-south-1',
                aws_access_key_id='',
                aws_secret_access_key='')


#### creating a new instance ####
new_reservation = ec2.run_instances(ImageId="ami-0ad704c126371a549",
                                   InstanceType="t2.micro",
                                    MaxCount = 1,
                                    MinCount =1,
                                    SecurityGroupIds=["sg-2793705b"])

#instances["Instances"][0]["InstanceId"]
instance = new_reservation["Instances"][0]["InstanceId"]

# create_volume(size, zone, snapshot=None, volume_type=None, iops=None)
vol = ec2.create_volume(Size=10, AvailabilityZone="ap-south-1a")

Volume_Id=vol["VolumeId"]

#### Attach a volume ####
result = ec2.attach_volume (VolumeId='volume_Id',
                            InstanceId='instance', Device="/dev/sdf"
                           )
