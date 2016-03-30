import requests
from bs4 import BeautifulSoup
from django.views.generic import TemplateView
from urllib.parse import parse_qs


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_string = self.request.GET.get('search_string')
        if search_string:
            scraped_content = requests.get("https://www.youtube.com/results?search_query={}+karaoke+version".format(search_string)).content
            clean_data = BeautifulSoup(scraped_content).find_all(class_="yt-lockup-title")
            context['scraped_content'] = [(song.find("a").get("title"), song.find("a").get("href")) for song in clean_data if not "*" in song.find("a").get("title")][:5]
            context['top_five'] = "Your Top 5 Search Results:"
        return context


class VideoView(TemplateView):
    template_name = 'video.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = self.kwargs.get("url")
        context["ending"] = parse_qs(url[6:]).get("?v")[0]
        return context