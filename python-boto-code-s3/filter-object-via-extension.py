"""
    if you want to count only images from your bucket, 
    you can filter objects by their extension.
"""

import boto3
import time

s3 = boto3.resource('s3')
bucket = s3.Bucket('<bucket-name>')

# you can add more image extensions if you want
extensions = ('.png', '.jpg', '.jpeg', '.webp')


def count_total_objects():
    total_images_in_bucket = 0
    total_folders_in_bucket = 0
    
    """
    Find total number of images and folders in a specific prefix
    
    """
    for obj in bucket.objects.all():
        time.sleep(0.3)
        if obj.key.endswith(extensions):
            total_images_in_bucket += 1
        elif obj.key.endswith("/"):
            total_folders_in_bucket += 1
        else:
            print("Object is neither image nor folder")
    
    return (total_images_in_bucket, total_folders_in_bucket)
            

if __name__ == "__main__":
    count = count_total_objects()
    print(f"Total images: {count[0]}")
    print(f"Total folders: {count[1]}")
