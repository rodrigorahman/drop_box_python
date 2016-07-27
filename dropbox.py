import dropbox

client = dropbox.client.DropboxClient("ge5n4SXKJ9gAAAAAAAASeyi5ntOgIjkWErD4wWkoAHuzcpnz5Rwh82C80Mf9c3ZA")
print 'linked account: ', client.account_info()

f = open('pacotes.txt')
client.put_file('pacotes.txt', f);
