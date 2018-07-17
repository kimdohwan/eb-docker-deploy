from storages.backends.s3boto3 import S3Boto3Storage

__all__ = (
    'S3DefaultStorage',
    'S3StaticStorage',
)


class S3DefaultStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'private'


class S3StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public_read'
