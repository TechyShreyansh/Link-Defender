import os

class Config:
    TOKEN = os.getenv("TOKEN")
    ALLOWED_DOMAINS = [
        "shineads.in",
        "dohe.in",
        "themeforest.net",
        "codecanyon.net"
    ]
