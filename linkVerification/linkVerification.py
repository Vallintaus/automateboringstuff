import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def verify_links(url):
    broken_links = []
    try:
        res = requests.get(url)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html.parser')

        links = soup.find_all('a', href=True)

        for link in links:
            link_url = urljoin(url, link['href'])

            try:
                link_response = requests.head(link_url, allow_redirects=True)
                if link_response.status_code == 404:
                    broken_links.append(link_url)

            except requests.RequestException as e:
                print(f"Error checking link {link_url}: {e}")

    except requests.RequestException as e:
        print(f"Error fetching page {url}: {e}")

    return broken_links



# Example usage
url = "https://www.youtube.com/"  # Replace with the URL you want to check
broken_links = verify_links(url)
if broken_links:
    print("Broken links found:")
    for link in broken_links:
        print(link)
else:
    print("No broken links found.")