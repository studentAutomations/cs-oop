import os
from dhooks import Webhook, Embed, File

WEBHOOK_URL = [os.getenv('PROBA')]
for url in WEBHOOK_URL:
    hook = Webhook(url) 

    hook.send('**@everyone CS je ažuriran!**')
    
    image2_path = 'cs-oop-nova-obavestenja.png'  

    hook.send(file=File(image2_path, name='cs-oop-nova-obavestenja.png'))

    hook.send('**>>> https://cs.elfak.ni.ac.rs/nastava/**')
