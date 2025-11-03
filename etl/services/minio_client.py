import os
import json
from io import BytesIO

from etl.services.settings import *
from minio import Minio, S3Error


class MinioClient:

    endpoint = os.getenv("MINIO_ENDPOINT")
    access_key = os.getenv("MINIO_ACCESS_KEY")
    secret_key = os.getenv("MINIO_SECRET_KEY")
    bucket = os.getenv("MINIO_BUCKET")

    client = Minio(
        endpoint=endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=False,
    )


    def fun(self):

        found = self.client.bucket_exists(self.bucket)
        if not found:
            self.client.make_bucket(self.bucket)
            print(f'Bucket "{self.bucket}" created')
        else:
            print(f'Bucket "{self.bucket}" already exists')


    def build_put_object(self, object_name, body_bytes):

        try:
            self.client.put_object(
                bucket_name=self.bucket,
                object_name=object_name,
                data=BytesIO(body_bytes),
                length=len(body_bytes),
                content_type="application/json; charset=utf-8",
            )

            print(f'OK: upload {object_name}, {len(body_bytes)} bytes')
        except S3Error as e:
            print(f'ERROR: {e}')
        except Exception as e:
            print(f'Other ERROR: {e}')



