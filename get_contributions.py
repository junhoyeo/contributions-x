import httpx
import bs4

def build_api_url(username: str, year: int):
  return (
    f'https://github.com/users/{username}/contributions?'
    f'from={year}-12-01&to={year}-12-31'
  )

def get_contributions(username: str, year: int):
  api_url = build_api_url(username, year)
  html = httpx.get(api_url).text
  print(html)

  soup = bs4.BeautifulSoup(html, 'html.parser')
  rects = soup.find_all('rect', class_='ContributionCalendar-day')

  contributions = []
  for rect in rects:
    if 'data-date' in rect.attrs:
      contributions.append({
        'date': rect.attrs['data-date'],
        'count': int(rect.attrs['data-count']),
      })

  return contributions
