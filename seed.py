import sys

from app import app
from crawler import MAX_ITEMS, RSS_URL, fetch_rss, parse_items
from models import Post, db


def build_content(item: dict) -> str:
    return "\n".join(
        [
            f"요약: {item['summary']}",
            f"링크: {item['link']}",
            f"발행시간: {item['pub_date']}",
        ]
    )


def seed_posts() -> int:
    xml_text = fetch_rss(RSS_URL)
    items = parse_items(xml_text, MAX_ITEMS)

    titles = [item["title"] for item in items if item.get("title")]

    with app.app_context():
        existing_titles = {
            row[0] for row in db.session.query(Post.title).filter(Post.title.in_(titles)).all()
        }

        inserted = 0
        for item in items:
            title = item.get("title", "").strip()
            if not title or title in existing_titles:
                continue

            post = Post(title=title[:200], content=build_content(item))
            db.session.add(post)
            existing_titles.add(title)
            inserted += 1

        if inserted:
            db.session.commit()

    return inserted


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    try:
        inserted_count = seed_posts()
        print(f"{inserted_count}건 추가됨")
    except Exception as e:
        print(f"0건 추가됨")
        print(f"시드 실행 중 오류: {e}")


if __name__ == "__main__":
    main()
