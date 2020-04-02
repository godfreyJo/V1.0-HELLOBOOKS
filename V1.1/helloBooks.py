from flask import Flask, render_template, url_for
app = Flask(__name__)

books = [
    {
        'title': 'Microeconomics',
        'author': 'Corey Schafer',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'

    },
    {
        'title':'Primary English',
        'author': 'Greg Norman',
        'content': 'Basic English...',
        'date_posted': 'May 20, 2019'},

    {
        'title':'Primary Maths',
        'author': 'Robina Hera',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'}
    ]





@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', books=books)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
