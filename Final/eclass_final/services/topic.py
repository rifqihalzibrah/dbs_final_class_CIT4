def get_all():
    from eclass_final.models.topic import get_all_topics
    topics, error = get_all_topics()
    return topics, error


def get_by_id(id):
    from eclass_final.models.topic import get_topic_by_id
    topic, error = get_topic_by_id(id)
    return topic, error


def save(data: dict):
    from eclass_final.models.topic import create_topic, update_topic, topic_submission
    error = ''
    if data:
        if data.get('title') and data.get('body') and not data.get('id'):
            _, error = create_topic(data)
        if data.get('title') and data.get('body') and data.get('id'):
            _, error = update_topic(data)
        if data.get('user_id') and data.get('topic_id') and data.get('body') and not data.get('id'):
            _, error = topic_submission(data)
    return _, error

def submit(data: dict):
    from eclass_final.models.topic import topic_submission
    error = ''
    if data:
        if data.get('user_id') and data.get('topic_id') and data.get('body') and not data.get('id'):
            _, error = topic_submission(data)
    return _, error

def delete(id):
    from eclass_final.models.topic import delete_topic
    topic, error = delete_topic(id)
    return topic, error
