import csv
import sys
from email.utils import parsedate_to_datetime

import requests
from bs4 import BeautifulSoup

RSS_URL = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"
MAX_ITEMS = 10
OUTPUT_CSV = "news_10.csv"


def clean_summary(description_html: str, title: str) -> str:
    if not description_html:
        return "(요약 없음)"

    html_soup = BeautifulSoup(description_html, "html.parser")
    candidates = [a.get_text(" ", strip=True) for a in html_soup.find_all("a")]

    for candidate in candidates:
        text = " ".join(candidate.split())
        if text and text != title:
            return text

    fallback = " ".join(html_soup.get_text(" ", strip=True).split())
    if fallback and fallback != title:
        if len(fallback) > 180:
            return fallback[:177] + "..."
        return fallback

    return title


def format_pub_date(pub_date: str) -> str:
    if not pub_date:
        return "(발행시간 없음)"

    try:
        dt = parsedate_to_datetime(pub_date)
        return dt.strftime("%Y-%m-%d %H:%M")
    except Exception:
        return pub_date


def fetch_rss(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    response.encoding = "utf-8"
    return response.text


def parse_items(xml_text: str, limit: int = 10):
    soup = BeautifulSoup(xml_text, "xml")
    items = soup.find_all("item")

    parsed = []
    for item in items[:limit]:
        title = item.title.get_text(strip=True) if item.title else "(제목 없음)"
        raw_description = item.description.get_text(" ", strip=True) if item.description else ""
        summary = clean_summary(raw_description, title)
        link = item.link.get_text(strip=True) if item.link else "(링크 없음)"
        raw_pub_date = item.pubDate.get_text(strip=True) if item.pubDate else ""
        pub_date = format_pub_date(raw_pub_date)

        parsed.append(
            {
                "title": title,
                "summary": summary,
                "link": link,
                "pub_date": pub_date,
            }
        )

    return parsed


def print_items(items):
    print("=" * 80)
    print(f"최신 뉴스 {len(items)}건")
    print("=" * 80)

    for idx, news in enumerate(items, start=1):
        print(f"[{idx}] {news['title']}")
        print(f"발행시간: {news['pub_date']}")
        print(f"링크    : {news['link']}")
        print(f"요약    : {news['summary']}")
        print("-" * 80)


def save_to_csv(items, file_path: str):
    with open(file_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "summary", "link", "pub_date"])
        writer.writeheader()
        writer.writerows(items)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    try:
        xml_text = fetch_rss(RSS_URL)
        items = parse_items(xml_text, MAX_ITEMS)

        if not items:
            print("RSS에서 뉴스 항목을 찾지 못했습니다.")
            return

        print_items(items)
        save_to_csv(items, OUTPUT_CSV)
        print(f"CSV 저장 완료: {OUTPUT_CSV}")
    except requests.RequestException as e:
        print(f"네트워크 요청 중 오류가 발생했습니다: {e}")
    except Exception as e:
        print(f"처리 중 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
