import os


photo_path = 'https://github.com/studentAutomations/cs-oop/blob/main/cs-oop-nova-obavestenja.png'  


if os.path.exists(photo_path):
    os.remove(photo_path)  
