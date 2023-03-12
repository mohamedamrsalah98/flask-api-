from app.models import Post,db
from flask import render_template, redirect, url_for,request
from app.posts import posts_blueprint
# from app.posts.forms import PostForm,CategoryForm




@posts_blueprint.route('/')
def posts_index():
    posts = Post.get_all_posts()
    return render_template('posts/allposts.html', posts=posts)


@posts_blueprint.route('/<int:id>')
def posts_info(id):
    show_post = Post.query.get_or_404(id)
    return render_template('posts/showpost.html', show_post=show_post)


@posts_blueprint.route('/<int:id>/delete')
def posts_delete(id):
    del_post = Post.query.get_or_404(id)
    x = del_post.delete_object()
    if x:
        return redirect(url_for("posts_index"))


#### create


@posts_blueprint.route('/create', methods=['GET','POST'])
def create_post():
    if request.method == 'GET':
        return render_template('posts/addpost.html',)
    elif request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        category_id = request.form['cat_id']

        add_post = Post(title=title, body=body,category_id=category_id)
        db.session.add(add_post)
        db.session.commit()
        return redirect(url_for("posts_index"))


@posts_blueprint.route('/post/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    edit_post = Post.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('posts/editpost.html', edit_post=edit_post)
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        edit_post.title = title
        edit_post.body = body
        db.session.add(edit_post)
        db.session.commit()
        return redirect(url_for("posts_index"))










