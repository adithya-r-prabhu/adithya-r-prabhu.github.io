import re
from IPython.display import HTML, IFrame
from IPython.lib.display import YouTubeVideo

yt_link = re.compile(r'(https?://)?(www\.)?((youtu\.be/)|(youtube\.com/watch/?\?v=))([A-Za-z0-9-_]+)', re.I)
yt_embed = '<iframe width="560" height="315" src="https://www.youtube.com/embed/{0}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

def convert_ytframe(text):
  return yt_link.sub(lambda match: yt_embed.format(match.groups()[5]), text)
 
url=input("please enter the url here--")
if __name__ == '__main__':
    embedlink=(convert_ytframe(url))
    
print(embedlink)
