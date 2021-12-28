from django.shortcuts import render, redirect
from .models import Category, Photo
# Create your views here.

def gallery(request):
    # photos = {
    #     0:'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg',
    #     1:'https://images.ctfassets.net/hrltx12pl8hq/61DiwECVps74bWazF88Cy9/2cc9411d050b8ca50530cf97b3e51c96/Image_Cover.jpg',
    #     2:'https://www.gettyimages.com/gi-resources/images/500px/983794168.jpg',
    #     3:'https://cdn.pixabay.com/photo/2021/08/25/20/42/field-6574455__340.jpg'
    # }
    category = request.GET.get('category')
    if category == None:
        
        photos = Photo.objects.all()
    else:

        photos = Photo.objects.filter(category__name = category)

    categories = Category.objects.all()
    context = {
        'categories' : categories,
        'photos': photos
    }
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        
        photo = Photo.objects.create(category = category, image = image, description=data['description'])

        return redirect('gallery')
    context = {
        'categories' : categories
    }
    return render(request, 'photos/add.html', context)

def paintApp(request):
    return render(request, 'photos/display.html')