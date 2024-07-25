# your_project/storage_backends.py

import os
import requests
from django.core.files.storage import Storage
from django.conf import settings

class SupabaseStorage(Storage):
    def __init__(self):
        self.supabase_url = settings.SUPABASE_URL
        self.supabase_key = settings.SUPABASE_KEY
        self.bucket = settings.SUPABASE_STORAGE_BUCKET

    def _save(self, name, content):
        url = f"{self.supabase_url}/storage/v1/object/{self.bucket}/{name}"
        headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
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
