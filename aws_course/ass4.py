import boto
import boto.s3.connection
import time
import os

s3 = boto.connect_s3()

#create two buckets
for i in range(2):
    now = time.time()
    bucketname = 'mybucket'+str(now)
    bucket = s3.create_bucket(bucketname)
    filename=raw_input('File to store in %s: '% bucketname)
    key = bucket.new_key(filename)
    key.set_contents_from_filename(filename)
    key.set_acl('public-read')


allbuckets = s3.get_all_buckets()

#print info of buckets and objects
for x in allbuckets:
    print x
    bucketcontents=x.list()	
    for c in bucketcontents:
        print c

#download objects to a folder
for z in allbuckets:
    bucketcontents=z.get_all_keys()	
    for e in bucketcontents:
        try:
            os.makedirs('downloaded')
        except:
            e.get_contents_to_filename('downloaded/'+str(e.key))

#delete objects and buckets
for y in allbuckets:
    bucketcontents=y.list()	
    for d in bucketcontents:
        y.delete_key(d)
    s3.delete_bucket(y)





