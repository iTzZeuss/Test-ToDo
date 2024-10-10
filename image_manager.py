import cloudinary
import cloudinary.uploader
from uuid import uuid4
import config

# Cloudinary configuration
cloudinary.config(
    cloud_name=config.CLOUD_NAME,  # Replace with your cloud name
    api_key=config.CLOUD_API_KEY,        # Replace with your API key
    api_secret=config.CLOUD_SECRET   # Replace with your API secret
)

# In-memory storage for file URLs and public IDs (replace with a database for production)
file_storage = {}

def upload_to_cloudinary(photo):
    filename = str(uuid4())  # Generate a unique filename

    try:
        # Upload file to Cloudinary
        upload_result = cloudinary.uploader.upload(photo, public_id=filename)
        return upload_result['secure_url'], filename  # Return URL and public_id
    except Exception as e:
        print(f"Error uploading file to Cloudinary: {e}")
        return None, None

def delete_from_cloudinary(public_id):
    try:
        cloudinary.uploader.destroy(public_id)
        return True
    except Exception as e:
        print(f"Error deleting file from Cloudinary: {e}")
        return False

def update_cloudinary(photo, public_id):
    # Delete the existing file
    delete_from_cloudinary(public_id)

    # Upload the new file
    return upload_to_cloudinary(photo)
