# qstar/core/cloud/aws_sync.py
import boto3
import os


class S3Sync:
    def __init__(
        self, bucket_name, aws_access_key, aws_secret_key, region_name="eu-west-1"
    ):
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region_name,
        )
        self.bucket_name = bucket_name

    def upload_file(self, local_path, s3_path):
        if not os.path.exists(local_path):
            raise FileNotFoundError("Fichier local introuvable.")

        self.s3.upload_file(local_path, self.bucket_name, s3_path)
        print(f"✅ Fichier '{local_path}' synchronisé avec S3 à '{s3_path}'")

    def download_file(self, s3_path, local_path):
        self.s3.download_file(self.bucket_name, s3_path, local_path)
        print(f"📥 Fichier '{s3_path}' récupéré dans '{local_path}'")


if __name__ == "__main__":
    # Exemple d'utilisation
    s3 = S3Sync("qstar-models", "your-access-key", "your-secret-key")
    s3.upload_file("./trained_model.bin", "models/trained_model.bin")
