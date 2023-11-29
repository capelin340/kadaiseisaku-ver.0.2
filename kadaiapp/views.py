from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView,DetailView
from .models import BlogPost
from .forms import BlogPostForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

from django.shortcuts import render, get_object_or_404
from .models import BlogPost




class IndexView(ListView):
    '''トップページのビュー
    
    テンプレートのレンダリングに特化したTemplateViewを継承
    
    Attributes:
      template_name: レンダリングするテンプレート
    '''
    # index.htmlをレンダリングする
    template_name ='index.html'
    context_object_name = 'orderby_records'
    queryset = BlogPost.objects.order_by('-posted_at')

    paginate_by = 4

class BlogDetail(DetailView):
    template_name = 'post.html'
    model = BlogPost

class G1View(ListView):
    template_name = 'G1_list.html'
    model = BlogPost
    context_object_name = 'G1_records'
    queryset = BlogPost.objects.filter(category = 'G1').order_by('-posted_at')
    paginate_by = 2

class G2View(ListView):
    template_name = 'G2_list.html'
    model = BlogPost
    context_object_name = 'G2_records'
    queryset = BlogPost.objects.filter(category = 'G2').order_by('-posted_at')
    paginate_by = 2
    
class G3View(ListView):
    template_name = 'G3_list.html'
    model = BlogPost
    context_object_name = 'G3_records'
    queryset = BlogPost.objects.filter(category = 'G3').order_by('-posted_at')
    paginate_by = 2

class UserView(ListView):
    template_name = 'User_list.html'
    model = BlogPost
    context_object_name = 'User_records'
    queryset = BlogPost.objects.filter(category = 'User').order_by('-posted_at')
    paginate_by = 2
    
class BlogPostSuccessView(TemplateView):
    template_name = 'post_suc.html'
    context_object_name = '-posted_at'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('kadaiapp:contact')

    def form_valid(self,form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ:{}'.format(title)

        message = \
            '送信者名: {0}\n メールアドレス{1}\n タイトル:{2}\n メッセージ:\n{3}' \
            .format(name, email ,title, message)
        from_email = 'admin@example.com'
        to_list = ['admin@example.com']
        message = EmailMessage(subject = subject, body = message, from_email = from_email, to = to_list,)
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
    
class MypageView(ListView):
    '''マイページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
      paginate_by: 1ページに表示するレコードの件数
    '''
    # mypage.htmlをレンダリングする
    template_name ='mypage.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
    
      queryset = BlogPost.objects.filter(
        user=self.request.user).order_by('-posted_at')
      # クエリによって取得されたレコードを返す
      return queryset

class CreatePost(FormView):
    template_name = "post.html"
    context_object_name = '-posted_at'
    success_url = reverse_lazy('kadaiapp:post_suc')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
       context = super(CreatePost, self).get_context_data(**kwargs)
       return context
    
    def get_queryset(self):
       return BlogPost.objects.order_by('-posted_at')


class CreatePost(CreateView):
    form_class = BlogPostForm
    template_name = 'post.html'
    success_url = reverse_lazy('kadaiapp:post_suc')  # フォームが正常に送信された後のリダイレクト先URL

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.user = self.request.user
        return super().form_valid(form)
    



def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

