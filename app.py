from flask import Flask, redirect, render_template, request, url_for
import validators
import nanoid
from mongoengine import *
import dotenv
import os

dotenv.load_dotenv()

app = Flask(__name__)
connect('url-shortener',host=os.getenv('MONGO_URI'))


def validate_url(url):
    """
    Validates if the url is really applicable
    :param url: url to validate type: str
    :return: bool
    """
    if(validators.url(url)):
        return True
    return False

class Url(Document):
    """
    Database models for url and slug
    """
    slug = StringField(max_length=100)
    url = URLField(max_length=1024, required=True)


@app.route('/newurl', methods=['POST'])
def new_url():
    succeeded = False
    slug = request.form['slug']
    url = request.form['url']
    valid = True
    if validate_url(url) == False:
        valid = False
        err = 'Not a valid url 🥺'
        return render_template('index.html',valid=valid, err=err)

    if slug == "":
        slug = nanoid.generate(size=5)
    #print(slug)
    newUrl = Url(slug=slug, url=url)
    exists = Url.objects.filter(slug__iexact=slug)
    if not exists:
        try:
            newUrl.save()
            succeeded = True
            return render_template('index.html', succeeded=succeeded, slug=slug)
        except Exception as e:
            return render_template('index.html', succeeded=succeeded, url=url, exception=str(e))
    else:
        succeeded = False
        in_use = f'❌ Slug {slug} already in use ❌'
        return render_template('index.html', succeeded=succeeded, url=url, in_use=in_use)


@app.route('/')
def main():
    """
    Main page
    :return: index.html
    """
    return render_template('index.html')

@app.route('/<slug>', methods=['GET'])
def get_url(slug):
    """
    Redirecting to the website if slug and corresponding url is found
    for example /slug : found --> redirecting
    :param slug: request parameter
    :return: Either flask redirection or 404 page
    """
    try:
        url = Url.objects.get(slug=slug)['url']
        if url:
            return redirect(url)
    except Exception as e:
        return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)