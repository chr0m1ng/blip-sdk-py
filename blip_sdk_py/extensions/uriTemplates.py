from enum import Enum


class UriTemplate(Enum):

    ALIASES = "/aliases"

    ALIAS_IDENTITY = "/aliases/{0}"

    ALIAS_NODE = "/aliases/{0}/{1}"

    ACCOUNT_KEYS = "/account/keys"

    ACCOUNT_KEY = "/account/keys/{0}"

    BUCKETS = "/buckets"

    BUCKET = "/buckets/{0}"

    THREADS = "/threads"

    THREAD = "/threads/{0}"

    EVENT_TRACK = "/event-track"

    EVENT_TRACK_CATEGORY = "/event-track/{0}"

    EVENT_TRACK_CATEGORY_ACTION = "/event-track/{0}/{1}"

    DELEGATIONS = "/delegations"

    DELEGATIONS_IDENTITY = "/delegations/{0}"

    DELEGATIONS_NODE = "/delegations/{0}/{1}"

    DIRECTORY_ACCOUNTS = "/accounts"

    DIRECTORY_ACCOUNT = "/accounts/{0}"

    DIRECTORY_ACCOUNT_KEY = "/accounts/{0}/key"

    CONFIGURATION = "/configuration"

    DOMAIN_CONFIGURATIONS = "/configurations/{0}"

    DOMAIN_CONFIGURATIONS_VALUE = "/configurations/{0}/{1}"

    LINKED_CONTACTS = "/contacts/{0}/linked"

    LINKED_CONTACT = "/contacts/{0}/linked/{1}"

    MESSAGES = "/messages"

    MESSAGE = "/messages/{0}"

    MESSAGE_BUFFER = "/message-buffer"

    MESSAGES_HISTORY = "/messages-history"

    MESSAGE_RESPONSE_TIME = "/message-statistic/responseTime"

    MESSAGE_WORD_COUNT = "/message-statistic/word-count"

    NOTIFICATIONS = "/notifications"

    NOTIFICATION = "/notifications/{0}"

    SESSION_STATISTIC = "/session-statistic/{0}"

    REMOTE_SESSION_DISPATCH = "/sessions/{0}?expiration={1}"

    SESSION = "/sessions/{0}"

    PIPELINE = "/pipeline"
    PIPELINE_SENDERS = PIPELINE + "/senders"

    PRESENCE_INSTANCE = "/presence/{0}"

    PROFILES = "/profile"

    PROFILE = "/profile/{0}"

    RESOURCES = "/resources"

    RESOURCE = "/resources/{0}"

    INTENTIONS = "/intentions"

    INTENTION = "/intentions/{0}"

    INTENTION_QUESTIONS = "/intentions/{0}/questions"

    INTENTION_QUESTION = "/intentions/{0}/questions/{1}"

    INTENTION_ANSWERS = "/intentions/{0}/answers"

    INTENTION_ANSWER = "/intentions/{0}/answers/{1}"

    ENTITIES = "/entities"

    ENTITY = "/entities/{0}"

    ANALYSIS = "/analysis"

    MODELS = "/models"

    ANALYSIS_FEEDBACK = "/analysis/{0}/feedback"
