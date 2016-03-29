import requests
from bs4 import BeautifulSoup
from django.views.generic import TemplateView

base_url = 'https://www.youtube.com/'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_string = self.request.GET.get('search_string')
        scraped_content = requests.get("https://www.youtube.com/results?search_query={}+karaoke+version".format(search_string)).content
        clean_data = BeautifulSoup(scraped_content).find(class_="yt-lockup-title")
        context['scraped_content'] = clean_data.prettify()
        return context


class VideoView(TemplateView):
    template_name = 'video.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ending = self.request.GET.get('v')
        context["ending"] = ending
        return context