from django.shortcuts import render,redirect,get_object_or_404
from instagram.models import Post, Profile
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import NewPostForm, UserForm, ProfileForm, CommentForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user.id
    user = request.user
    posts = Post.objects.all()
    ordering=['-date_posted']
    if Profile.objects.filter(user = request.user).count() == 0:
        prof = Profile(user=request.user)
        prof.save()
    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user

    ordering=['-date_posted']
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('index')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form":form})

@login_required(login_url='/accounts/login/')
def profile(request,user_id=None):
    if user_id == None:
        user_id=request.user.id
    current_user = User.objects.get(id = user_id)
    user = current_user
    images = Post.objects.filter(user=current_user)
    profile = Profile.objects.all()

    return render(request, 'profile.html', locals())

@login_required
def userprofile(request, user_id):
    users = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=users)
    images = Post.objects.filter(user=users)
    followers = len(Follow.objects.followers(users))
    following = len(Follow.objects.following(users))
    posts = len(Image.objects.filter(user=users))
    people_following = Follow.objects.following(request.user)
    return render(request, 'profile/userprofile.html', {"user": users, "profile": profile, "images": images,"followers":followers, "following":following, "posts":posts, "people_following":people_following})

@login_required(login_url='/accounts/login/')
def follow(request, user_id):
    users = User.objects.get(id=user_id)
    follow = Follow.objects.add_follower(request.user, users)
    return render(request, 'profile.html', {"users": users, "follow":follow})

@login_required(login_url='/accounts/login')
def updateprofile(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('profile')

	else:
			form = ProfileForm()
	return render(request, 'updateprofile.html',{"form":form })

@login_required(login_url='/accounts/login')
def comment_on(request, image_id):
    image = get_object_or_404(Post, pk=image_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user.profile
            comment.photo = image
            comment.save()
    return redirect('index')


@login_required(login_url='/accounts/login/')
def find(request, name):
    results = Profile.find_profile(name)
    return render(request, 'search.html', locals())

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profile": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def comment(request, image_id):
    current_user = request.user 
    images = Image.objects.get(id=image_id)
    if request.method == 'POST':
        form1 = CommentForm(request.POST) 
        if form1.is_valid():
            image = form1.save(commit=False)
            image.writer = current_user
            image.image = images
            image.save()
        return redirect('display')
    else:
        form1=CommentForm    
    return render(request,'comment.html',{"form1":form1,"images":images})