#!/usr/bin/env python3
"""
Archives chats in chat.hayk.io
"""

__author__ = "Hayk Khachatryan"
__version__ = "0.0.1"
__license__ = "MIT"

from slackclient import SlackClient

import variables as vars


#####################
#                   #
#       slack       #
#       setup       #
#                   #
#####################

# auth token
SLACK_TOKEN = vars.SLACK_TOKEN
slack_client = SlackClient(SLACK_TOKEN)

# outgoing webhook token
SLACK_WEBHOOK_SECRET = vars.SLACK_WEBHOOK_SECRET

def archive(channel_id):
    '''
    Archives channel

    Arguments:
        channel_id {str}
    '''
    slack_client.api_call(
        "channels.archive",
        channel=channel_id
    )

def get_channels():
    '''
    Returns list of channel_ids
    '''
    channels = slack_client.api_call(
        "channels.list",
        exclude_archived = 1,
        exclude_members = 1
    )

    return [channel['id'] for channel in channels['channels']]

def main():
    print("Getting channel list\n")
    channels = get_channels()

    print("Archiving channels\n")
    count = 0
    for channel in channels:
        archive(channel)
        count += 1
    
    print('Archived ', count, " channels")


if __name__ == '__main__':
    main()