import boto3
import time

s3 = boto3.resource('s3')
bucket = s3.Bucket('<bucket-name>')

def count_total_objects():
    total_objects_in_bucket = 0
    
    """
    If you have subfolders in your bucket, you can filter objects by prefix.
    E.g.
    
    for _ in bucket.objects.filter(Prefix='extra_images/'):
    
    """
    for _ in bucket.objects.all():
        time.sleep(0.3)
        total_objects_in_bucket += 1
    
    return total_objects_in_bucket


def print_all_object_name():
    for obj in bucket.objects.all():
        print(obj) # prints all properties of the object
        print(obj.key) # prints only the object key (name)
        time.sleep(0.3)



if __name__ == "__main__":
    # total_objects = count_total_objects()
    # print(f"Total Objects: {total_objects}")

    print_all_object_name()
