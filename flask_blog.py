from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
{
	'author':'Manas Ranjan Pati',
	'title' : 'Day as a Software Developer',
	'content' : 'Hi My day as a Software Developer is not so good today!!!',
	'date_posted' : 'April-20-2021'
},
{
	'author':'Manas Ranjan Pati',
	'title' : 'Life of Pi',
	'content' : 'What is Lorem Ipsum?Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry',
	'date_posted' : 'April-20-2022'
}
]




@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


if __name__ == "__main__":
	app.run(debug=True)

