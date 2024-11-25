import os
from dhooks import Webhook, Embed, File

# Get the webhook URL from environment variable
WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN')]


for url in WEBHOOK_URL:
    hook = Webhook(url) 

    hook.send('**@everyone Nova obavestenja na CS-u!**')

    
    image2_path = 'cs-oop-nova-obavestenja.png'  # Local path to the image

    
    # Send the embed and attach the image
    hook.send(file=File(image2_path, name='cs-oop-nova-obavestenja.png'))

    hook.send('**>>> https://cs.elfak.ni.ac.rs/nastava/**')
