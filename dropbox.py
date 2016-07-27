import dropbox

oauth_key = "ge5n4SXKJ9gAAAAAAAASeyi5ntOgIjkWErD4wWkoAHuzcpnz5Rwh82C80Mf9c3ZA"

client = dropbox.client.DropboxClient(oauth_key)

f = open('pacotes.txt')

client.put_file('pacotes.txt', f);
