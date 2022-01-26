import time
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.publish_key = 'pub-c-d0716815-2e18-4c38-b531-3fdb6ad80f02'
pnconfig.subscribe_key = 'sub-c-5b78bd40-7e8f-11ec-8e41-c2c95df3c49a'

TEST_CHANNEL = 'TEST_CHANNEL'


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Channel : {message_object.channel} | Message: {message_object.message}')

class PubSub():
    '''
    Hnadles the publish/subscribe layer of the application
    Provides communication between the nodes of the blockchain network
    '''
    def __init__(self):
        self.pubnub= PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        '''
        Publish the message object to the channel
        '''
        self.pubnub.publish().channel(channel).message(message).sync()

def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(TEST_CHANNEL, {'foo': 'bar'})

if __name__ == '__main__':
    main()