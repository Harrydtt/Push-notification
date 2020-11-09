from pushbullet.pushbullet import PushBullet

apiKey = "o.dMQ1q1G7y8q01Tenqc3DfW1GvO7gLH07"
p = PushBullet(apiKey)
# Get a list of devices
devices = p.getDevices()

# Get a list of contacts
contacts = p.getContacts()

# Send a note
p.pushNote(devices[0]["iden"], 'Tada', 'It works')


'''-------------------------------------------------------

# Send a map location
p.pushAddress(devices[0]["iden"], "Eiffel tower", "Eeiffel tower, france")

# Send a list
p.pushList(devices[0]["iden"], "Groceries", ["Apples", "Bread", "Milk"])

# Send a link
p.pushLink(devices[0]["iden"], "Google", "http://www.google.com")

# Send a file
p.pushFile(devices[0]["iden"], "file.txt", "This is a text file", open("file.txt", "rb"))

# Send a note to a channel
p.pushNote('channel_tag', 'Hello world', 'Test body', recipient_type='channel_tag')

# Send a note to an email
p.pushNote('myemail@domain.com', 'Hello world', 'Test body', recipient_type='email')


Using the command line tool:

./pushbullet_cmd.py YOUR_API_KEY_HERE getdevices
./pushbullet_cmd.py YOUR_API_KEY_HERE note udeCmddJpl "Hello World" "Test Body"
./pushbullet_cmd.py YOUR_API_KEY_HERE address udeCmddJpl "Eiffel tower" "Eeiffel tower, france"
./pushbullet_cmd.py YOUR_API_KEY_HERE list udeCmddJpl Groceries Apples Bread Milk
./pushbullet_cmd.py YOUR_API_KEY_HERE link udeCmddJpl Google http://www.google.com
./pushbullet_cmd.py YOUR_API_KEY_HERE file udeCmddJpl test.jpg
./pushbullet_cmd.py YOUR_API_KEY_HERE note "#channel_tag" "Hello World" "Test Body"
'''