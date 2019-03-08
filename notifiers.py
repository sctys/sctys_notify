def send_message(message, agent_name):
    agent = agent_name.capitalize() + 'Notifier'
    file_name = agent_name + '_notifier'
    agent_file = __import__(file_name, fromlist=[agent])
    agent = getattr(agent_file, agent)()
    agent.send_message(message)


def test_send_message(test_message, agent_name):
    send_message(test_message, agent_name)


if __name__ == '__main__':
    test_send_message('test', 'slack')
    test_send_message('test', 'telegram')

