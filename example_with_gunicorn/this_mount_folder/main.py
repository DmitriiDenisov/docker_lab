import os, sys
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_PATH)
from scripts.AutoSelfie_bot import AutoSelfieBot

REQUEST_KWARGS = {
    'proxy_url': 'socks5://80.211.195.141:1488',
    # Optional, if you need authentication:
    'urllib3_proxy_kwargs': {
        'username': 'kurwaproxy',
        'password': 'x555abr',
    }
}

f = open(os.path.join(PROJECT_PATH, 'token.txt'), 'r')
token = f.read(100)

currentr_PID = os.getpid()
with open(os.path.join(PROJECT_PATH, 'data', 'PID.txt'), 'w') as f:
    f.write(str(currentr_PID))


def main():
    AutoSelfieBot(token=token, request_kwargs=REQUEST_KWARGS, model_name='resnet_weights.17--0.95.hdf5.model')


if __name__ == '__main__':
    main()
# dp.add_handler(RegexHandler("English", send_cat, pass_user_data=True))
