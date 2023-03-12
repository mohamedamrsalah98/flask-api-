from flask_restful import Resource, Api,marshal_with,abort
from app.posts.api.serializers import post_serializer
from app.models import Post
from app.posts.api.parser import post_parser



class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    


class PostList(Resource):
    @marshal_with(post_serializer)
    def get(self):
        posts = Post.get_all_posts()
        return posts
    
    @marshal_with(post_serializer)
    def post(self):
        posts_args = post_parser.parse_args()
        post =  Post.create_post(posts_args)
        return  post, 201
    

class PostOperation(Resource):
    @marshal_with(post_serializer)
    def get(self, id):
        post = Post.get_specific_posts(id)
        if post:
            return post, 200

        return abort(404, message="post not found.")

    @marshal_with(post_serializer)
    def put(self, id):
        post = Post.get_specific_posts(id)
        if post:
            posts_args = post_parser.parse_args()
            post.update_posts(posts_args)
            return post, 200

        return 'post not found , please reload the page', 205

    def delete(self, id):
        post = Post.get_specific_posts(id)
        if post:
            post.delete_object()
            return 'post deleted', 204

        return 'post not found , please reload the page', 205






