# Testing the Wit Python API

from wit import Wit

client = Wit(access_token = 'NSYOCSCMCJCWU6Y55G3K5TRA65PSDBLY')

response = client.message('What is the weather today?')
print "WIT AI: " + str(response)
