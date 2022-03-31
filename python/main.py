from argparse import ArgumentParser, Namespace

from subscriber import Subscriber
from publisher import Publisher


def execute(args: Namespace):
    if args.mode == "sub_channels":
        sub: Subscriber = Subscriber(args.host, args.topic, args.listening)
        sub.listen()
    if args.mode == "read_card_to_mqtt":
        pub: Publisher = Publisher(args.host)
        pub.read_card_to_mqtt()


def get_argparser():
    result = ArgumentParser(description="Card Reader")
    result.add_argument("mode", metavar="MODE", type=str,
                        help="Set the mode ['sub_channels', 'read_card_to_mqtt']",
                        choices=["sub_channels", "read_card_to_mqtt"])
    result.add_argument("host", metavar="HOST", type=str,
                        help="Set the MQTT host")
    result.add_argument("-t", "--topic", metavar="TOPIC", type=str,
                        help="Set the subscribed MQTT topic")
    result.add_argument("-c", "--channels", metavar="CHANNEL", type=int, nargs="*", dest="listening",
                        help="Set the subscribed Channels")
    return result


if __name__ == '__main__':
    parser = get_argparser()

    execute(parser.parse_args())
