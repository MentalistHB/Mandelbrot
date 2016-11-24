import boto
import boto.s3.connection

access_key = 'AKIAIRBBN7ZV7UPV7F6A'
secret_key = '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'

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)

#for bucket in conn.get_all_buckets():
#        print("{name}\t{created}".format(
#                name = bucket.name,
#                created = bucket.creation_date,
#        ))

bucket = conn.get_bucket('mandelbrots3')
#for bucket in conn.get_all_buckets():
#        print("{name}\t{created}".format(
#                name = bucket.name,
#                created = bucket.creation_date,
#        ))

#key = bucket.new_key('mediabrot.png')
#key.set_contents_from_filename('mediabrot.png')
#key.set_canned_acl('public-read')
#url = key.generate_url(expires_in=10, query_auth=False, force_http=True)
for key in bucket.list():
	
	print("Deleting file: {}".format(key.name))
	bucket.delete_key(key.name)
