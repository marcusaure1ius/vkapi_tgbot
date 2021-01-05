import os

from dotenv import load_dotenv
load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')

TG_TOKEN = os.getenv('TG_TOKEN')

TG_ADMIN_ID = os.getenv('TG_ADMIN_ID')