import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5736526417:AAG6pV3pz5hqANX3w49g5ur2FRBpF4ywMHc")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQEZ5g8AoYsRSGIsolhSRtMS9ywDI84B_rrlL1uGIN2ITejeQuSYMOMu7eNeXXwbr0RwIVu2LXJOop-CEE29nwdwrUhgpmxcGYZ93g0CoSD73yYQ8PJZ_HmcLOZ-bUa5khy0VAFOt23-33mXgNs9M1EKXnX58vaRdI_TjDYSdnbxx8ery4ZGe2HqnO5J00jl7PLVfrkD8mYcF8NJDwRaQsUs-GvMExxi7DicACEq5RmlFoQReObP4d1ayCZ2nNHr4BVFQlw4MW8eFd2rDwzQc9j-sqYKkIaClcsrEI8Cbm3jAi8CfYzd9h37ga0MG8Z1Np1OXVur7XWuq0FS9QQ4ccOCfpapNgAAAAFO6MgtAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Alone_dil_121_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5618845741")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
