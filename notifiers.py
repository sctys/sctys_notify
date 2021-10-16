def get_notifier(notifier_name, project, logger):
    notifier_object_name = notifier_name.capitalize() + 'Notifier'
    file_name = notifier_name + '_notifier'
    notifier_file = __import__(file_name, fromlist=[notifier_object_name])
    notifier_object = getattr(notifier_file, notifier_object_name)(project, logger)
    return notifier_object

