import json
import logging
import azure.functions as func

from function_app import app


@app.function_name(name="eventHubTrigger")
@app.event_grid_trigger(arg_name="event")
def main(event: func.EventGridEvent):
    logging.info('Function triggered to process a message: %s', event.get_body())
    logging.info('  EnqueuedTimeUtc = %s', event.enqueued_time)
    logging.info('  SequenceNumber = %s', event.sequence_number)
    logging.info('  Offset = %s', event.offset)

    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })

    logging.info('Python EventGrid trigger processed an event: %s', result)



