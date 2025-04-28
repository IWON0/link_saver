import requests
from bs4 import BeautifulSoup

def fetch_link_metadata(url):
    metadata = {
        "title": "",
        "description": "",
        "image": "",
        "link_type": "website"
    }
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return metadata

        soup = BeautifulSoup(response.text, 'html.parser')

        og_title = soup.find('meta', property='og:title')
        og_description = soup.find('meta', property='og:description')
        og_image = soup.find('meta', property='og:image')
        og_type = soup.find('meta', property='og:type')

        if og_title and og_title.get('content'):
            metadata['title'] = og_title['content']
        elif soup.title:
            metadata['title'] = soup.title.string

        if og_description and og_description.get('content'):
            metadata['description'] = og_description['content']
        else:
            desc = soup.find('meta', attrs={'name': 'description'})
            if desc and desc.get('content'):
                metadata['description'] = desc['content']

        if og_image and og_image.get('content'):
            metadata['image'] = og_image['content']

        if og_type and og_type.get('content'):
            og_type_content = og_type['content']
            if og_type_content in ['book', 'article', 'music', 'video']:
                metadata['link_type'] = og_type_content

    except Exception:
        pass

    return metadata
