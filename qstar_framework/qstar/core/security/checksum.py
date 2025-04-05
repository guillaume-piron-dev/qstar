# qstar/core/security/checksum.py
import hashlib
import os


def compute_checksum(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("Fichier introuvable")

    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def verify_checksum(file_path, expected_hash):
    actual_hash = compute_checksum(file_path)
    return actual_hash == expected_hash


if __name__ == "__main__":
    test_file = "./trained_model.bin"
    print("Empreinte SHA256 :", compute_checksum(test_file))
