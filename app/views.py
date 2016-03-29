import requests
from bs4 import BeautifulSoup
from django.views.generic import TemplateView

base_url = 'https://www.youtube.com/embed/'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_string = self.request.GET.get('search_string')
        scraped_content = requests.get("https://www.youtube.com/results?search_query={}+karaoke+version".format(search_string)).content
        clean_data = BeautifulSoup(scraped_content).find(class_="item-section")
        context['scraped_content'] = clean_data.prettify()
        return context


class VideoView(TemplateView):
    template_name = 'video.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_url = base_url + context["url"]
        videos = requests.get(new_url).content
        clean_video = BeautifulSoup(videos).find_all('pre')
        context["videos"] = [video.prettify() for video in clean_video]
        return context