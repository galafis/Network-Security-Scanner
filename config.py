import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'change-this-secret-key-in-production'
    # Additional configuration can be added here
    # For example, database settings, rate limits, etc.

