from marshmallow import Schema, fields

class PlainUserSchema(Schema):
    id = fields.Int(dump_only = True)
    user_name = fields.Str(required = True)
    password = fields.Str(required = True, load_only = True)
    description = fields.Str()
    
class TweetSchema(Schema):
    id = fields.Int(dump_only = True)
    text = fields.Str(required = True)
    user = fields.Nested(PlainUserSchema(), dump_only = True)    
    
class UserTweetSchema(Schema):
    tweets = fields.List(fields.Nested(TweetSchema(), dump_only = True))