
from __future__ import print_function

#building functions
    
def build_speechlet_response(title, output, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'shouldEndSession': should_end_session
    }
    
def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
    
# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    #need to add ryans code to query sql database
    session_attributes = {}
    card_title = "Welcome"
    #loop through list, add to speech output
    speech_output = "Hello this is a test"
    
    should_end_session = True
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def dispatch(IntentRequest)

if IntentRequest == 'getFlight':
    return get_welcome_response()



# --------------- Main handler ------------------

  def lambda_handler(event, context):

    return(dispatch(event))

    