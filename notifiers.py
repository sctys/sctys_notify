def send_message(message, agent_name):
    agent = agent_name.capitalize() + 'Notifier'
    file_name = agent_name + '_notifier'
    agent_file = __import__(file_name, fromlist=[agent])
    agent = getattr(agent_file, agent)()
    agent.send_message(message)

