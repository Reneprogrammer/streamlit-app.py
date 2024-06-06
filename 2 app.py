{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9e4dd14-c1ff-449f-9c0f-37f3b8699e1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "def scrape_article(url):\n",
    "    response = requests.get(url)\n",
    "    if response.status_code == 200:\n",
    "        soup = BeautifulSoup(response.content, 'html.parser')\n",
    "        title = soup.find('h1').text if soup.find('h1') else 'No title found'\n",
    "        content = ' '.join(p.text for p in soup.find_all('p'))\n",
    "        return title, content\n",
    "    else:\n",
    "        return None, None\n",
    "\n",
    "url = 'https://www.economist.com/the-world-in-brief'\n",
    "title, content = scrape_article(url)\n",
    "if title and content:\n",
    "    print(f\"Title: {title}\")\n",
    "    print(f\"Content: {content[:500]}...\")  # Print the first 500 characters of the content\n",
    "else:\n",
    "    print(\"Failed to retrieve the article\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
