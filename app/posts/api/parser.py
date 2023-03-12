from flask_restful import  reqparse

post_parser = reqparse.RequestParser()

post_parser.add_argument('title', type=str,help='post title is required', required=True )
post_parser.add_argument('body', type=str,help='post body' )
post_parser.add_argument('category_id', type=str,help='post body' )


