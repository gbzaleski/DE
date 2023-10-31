from minio import Minio
from minio.error import S3Error

file = "data.csv"
file_minio = "data_minio.csv"
ACCESS_KEY = "minio"
SECRET_KEY = "minio123"

def main():
    # Create a client with the MinIO server playground, its access key and secret key.
    client = Minio(
        "localhost:9000",
        access_key=ACCESS_KEY,
        secret_key=SECRET_KEY,
        secure=False,
    )

    found = client.bucket_exists("asiatrip")
    if not found:
        client.make_bucket("asiatrip")
    else:
        print("Bucket 'asiatrip' already exists")

    result = client.fput_object(
        "asiatrip", file_minio, file,
    )
    print(
        f"created {file_minio} in bucket 'asiatrip' at etag: "
        + result.etag,
    )

# Worked:
# gbz@gbz:~/DataEng/lab2$ python3 task2.py 
# created data_minio.csv in bucket 'asiatrip' at etag: 8465e53cc071c48b402a2a7308c0a6f1


try:
    main()
except S3Error as exc:
    print("error occurred.", exc)


# Manual:
# Running Minio on docker:
    # docker run -p 9000:9000 \
    # -e "MINIO_ACCESS_KEY=minio" \
    # -e "MINIO_SECRET_KEY=minio123" \
    # minio/minio server /data
