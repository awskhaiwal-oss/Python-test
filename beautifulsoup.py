import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Find data using id param
results = soup.find(id="ResultsContainer")

filter_jobs_with_python_keyword = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_jobs_only = [
    h2_element.parent.parent.parent for h2_element in filter_jobs_with_python_keyword
]

for job_card in python_jobs_only:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    link_url = job_card.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")