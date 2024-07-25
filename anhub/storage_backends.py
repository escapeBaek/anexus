import os
import requests
import jwt
from django.core.files.storage import Storage
from django.conf import settings
from datetime import datetime, timedelta

class SupabaseStorage(Storage):
    def __init__(self):
        self.supabase_url = settings.SUPABASE_URL
        self.supabase_key = settings.SUPABASE_KEY
        self.supabase_secret = settings.SUPABASE_JWT_SECRET
        self.bucket = settings.SUPABASE_STORAGE_BUCKET

    def _generate_jwt(self):
        payload = {
            "role": "authenticated",
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, self.supabase_secret, algorithm="HS256")
        return token

    def _save(self, name, content):
        url = f"{self.supabase_url}/storage/v1/object/{self.bucket}/{name}"
        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self._generate_jwt()}",
            "Content-Type": content.content_type
        }
        response = requests.put(url, headers=headers, data=content.read())
        if response.status_code != 200:
            raise Exception(f"Failed to upload file to Supabase: {response.text}")
        return name

    def url(self, name):
        return f"{self.supabase_url}/storage/v1/object/public/{self.bucket}/{name}"

    def exists(self, name):
        url = f"{self.supabase_url}/storage/v1/object/public/{self.bucket}/{name}"
        response = requests.head(url)
        return response.status_code == 200
