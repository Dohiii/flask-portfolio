#################
#### imports ####
#################
from os import abort
from flask import flash, request, redirect, url_for, render_template
from .forms import PostForm
from . import posts_blueprint
from flask_login import login_required
from ..models import Post
from project import db
from slugify import slugify


################
#### routes ####
################


@posts_blueprint.route('/')
def index():
    return render_template('index.html')


@posts_blueprint.route('/posts')
def posts():
    posts = Post.query.order_by(Post.featured.desc(), Post.created.desc())
    return render_template('posts/posts.html', posts=posts)


@posts_blueprint.route('/add-post', methods=['GET', 'POST'])
@login_required
def add_post():
    form = PostForm(request.form)
    if request.method == 'POST' and form.validate():
        post = Post(form.title.data, form.content.data,
                    form.link.data, form.image.data, form.featured.data,
                    slug=slugify(request.form.get("title"))
                    )
        db.session.add(post)
        db.session.commit()
        flash('Post Aded')
        return redirect(url_for('posts.posts'))
    return render_template('posts/add-post.html', form=form)


@posts_blueprint.route('/<slug>')
def single_post(slug):
    post = Post.query.filter_by(slug=slug).first()

    if not post:
        abort(404)

    return render_template('posts/single_page.html', post=post)


@posts_blueprint.route('/edit/<slug>', methods=['GET', 'POST'])
def edit_post(slug):
    form = PostForm()
    post_to_update = Post.query.filter_by(slug=slug).first()
    form.title.data = post_to_update.title
    form.content.data = post_to_update.content
    form.link.data = post_to_update.link
    form.image.data = post_to_update.image

    if request.method == 'POST':
        post_to_update.title = request.form['title']
        post_to_update.content = request.form['content']
        post_to_update.link = request.form['link']
        post_to_update.image = request.form['image']

        try:
            db.session.commit()
            flash('Post updated successfully')
            return redirect(url_for('posts.posts'))
            # return render_template('add_user.html', form=form, post_to_update=post_to_update)
        except:
            flash('User wasnt updated. Looks like there was a problem, try again')
            return render_template('posts/edit.html', form=form, post_to_update=post_to_update)
    else:
        return render_template('posts/edit.html', form=form, post_to_update=post_to_update, id=id)


@posts_blueprint.route('/delete/<slug>')
def delete(slug):
    post_to_delete = Post.query.filter_by(slug=slug).first()
    try:
        db.session.delete(post_to_delete)
        db.session.commit()
        flash('Post deleted succesfully')
        return redirect(url_for('posts.posts'))
    except:
        flash('Whops there was a problem, try again')
        return render_template('posts/single_page.html', post_to_delete=post_to_delete)


@posts_blueprint.route('/kontakt')
def kontakt():
    return render_template('posts/kontakt.html')
