from flask import render_template, url_for, flash, redirect
from Project_Package.models import User, Videos, Playlist
from Project_Package.form import RegistrationForm, LoginForm
from Project_Package import app


videos_data = [{
    'title' : 'المزدوجة .. قصة صعب تتكرر',
    'playlist' : 'The complete story',
    'author' : 'Sameh Sanad',
    'thumbnail' : 'csU3l5pWt1Y-HD.jpg',
    'link' : 'OfnrHUe3w3c',
    'id' : 1
},
{
    'title' : 'الأزرق .. و بكــ ــاء المقابــ ــر',
    'playlist' : 'The compelete story',
    'author' : 'Sameh Sanad',
    'thumbnail' : '7vapvzCCYvo-HD.jpg',
    'link' : '0S59hW9NN58',
    'id' : 2
},
{
    'title' : 'جـ ـثة المقطم .. ملفات البحث الجنائي',
    'playlist' : 'The compelete story',
    'author' : 'Sameh Sanad',
    'thumbnail' : 'GdAfRVqSgko-HD.jpg',
    'link' : '',
    'id' : 3
},
{
    'title' : 'شقة زفتى .. ســ ــفاح الغربية | قصة تحتاج لتركيز قوي',
    'playlist' : 'The compelete story',
    'author' : 'Sameh Sanad',
    'thumbnail' : 'vSJfv_8h5Fw-HD.jpg',
    'link' : '',
    'id' : 4
},
{
    'title' : 'ثـ ـعبان فيصل .. الكل تبرأ منه | نوع مختلف من البشر',
    'playlist' : 'The compelete story',
    'author' : 'Sameh Sanad',
    'thumbnail' : 'JD1uju_xRvY-HD.jpg',
    'link' : 'NnPd6pgX-AY',
    'id' : 5
},
{
    'title' : 'أنهار .. قلبها كبير | كل الأطراف سعيدة | و مفاجأة في التنفيذ',
    'playlist' : 'The compelete story',
    'author' : 'Sameh Sanad',
    'thumbnail' : 'Ur5JPPf6f6U-HD.jpg',
    'link' : '',
    'id' : 6
},]

playlist_data = [
    {
      'name' : 'The complete story',
      'icon' : 'Sameh_Sanad.png',
      'description' : 'story'
    },
    {
        'name' : 'The complete story',
        'icon' : 'Sameh_Sanad.png',
        'description' : 'story'
    },
    {
        'name' : 'The complete story',
        'icon' : 'Sameh_Sanad.png',
        'description' : 'story'
    },
    {
        'name' : 'The complete story',
        'icon' : 'Sameh_Sanad.png',
        'description' : 'story'
    },
    {
        'name' : 'The complete story',
        'icon' : 'Sameh_Sanad.png',
        'description' : 'story'
    },
    {
        'name' : 'The complete story',
        'icon' : 'Sameh_Sanad.png',
        'description' : 'story'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', videos_data=videos_data, playlist_data=playlist_data, title='Home')

@app.route('/watch/<int:video_id>')
def watch(video_id):
    found_video = None
    for v in videos_data:
        if v.get('id') == video_id:
            found_video = v
            break
            
    if not found_video:
        return "Video not found", 404

    current_index = videos_data.index(found_video)
    
    next_index = (current_index + 1) % len(videos_data)
    next_video_id = videos_data[next_index].get('id')

    previous_index = (current_index - 1) % len(videos_data)
    previous_video_id = videos_data[previous_index].get('id')
    
    return render_template('watch.html',video=found_video,next_video_id=next_video_id,previous_video_id=previous_video_id)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', title = 'Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)

