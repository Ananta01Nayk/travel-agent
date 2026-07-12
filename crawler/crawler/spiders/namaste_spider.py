import scrapy
from scrapy.spiders import SitemapSpider
from bs4 import BeautifulSoup
import trafilatura
from datetime import datetime


class NamasteSpider(SitemapSpider):

    name = "namaste"

    allowed_domains = ["namasteindiatrip.com"]

    sitemap_urls = [
        "https://www.namasteindiatrip.com/sitemap_index.xml",
        "https://www.namasteindiatrip.com/blog/sitemap_index.xml",
    ]

    sitemap_follow = [r".*"]

    sitemap_rules = [
        (r".*", "parse_page"),
    ]

    custom_settings = {
        "ROBOTSTXT_OBEY": True,
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_START_DELAY": 1,
        "AUTOTHROTTLE_MAX_DELAY": 5,
        "AUTOTHROTTLE_TARGET_CONCURRENCY": 2,
        "DOWNLOAD_DELAY": 0.5,
    }

    def parse_page(self, response):

        if response.status != 200:
            return

        soup = BeautifulSoup(response.text, "lxml")

        title = response.css("title::text").get(default="").strip()

        meta_description = response.css(
            'meta[name="description"]::attr(content)'
        ).get(default="").strip()

        canonical = response.css(
            'link[rel="canonical"]::attr(href)'
        ).get(default=response.url)

        h1 = [
            h.get_text(" ", strip=True)
            for h in soup.find_all("h1")
        ]

        h2 = [
            h.get_text(" ", strip=True)
            for h in soup.find_all("h2")
        ]

        content = trafilatura.extract(
            response.text,
            include_comments=False,
            include_tables=True,
        )

        if not content:
            content = soup.get_text(" ", strip=True)

        url = response.url.lower()

        if "/blog/" in url:
            page_type = "blog"
        elif "tour" in url:
            page_type = "tour_package"
        elif "destination" in url:
            page_type = "destination"
        else:
            page_type = "other"

        packages = self.extract_packages(soup, response)

        yield {
            "url": response.url,
            "canonical_url": canonical,
            "status": response.status,
            "title": title,
            "meta_description": meta_description,
            "h1": h1,
            "h2": h2,
            "content": content,
            "packages": packages,
            "page_type": page_type,
            "crawled_at": datetime.utcnow().isoformat(),
        }

    def extract_packages(self, soup, response):

        packages = []

        for card in soup.select("div.prc_row"):

            package = {}

            # ----------------------------
            # Basic Information
            # ----------------------------

            title = card.select_one("h2.prc_head")

            package["title"] = (
                title.get_text(" ", strip=True)
                if title else ""
            )

            duration = card.select_one("p.prc-dur")

            if duration:
                package["duration"] = duration.get_text(" ", strip=True)
            else:
                package["duration"] = ""

            # ----------------------------
            # Price
            # ----------------------------

            package["price"] = ""

            if card.get("data-price"):
                package["price"] = f"INR {card['data-price']}"

            else:
                price = card.select_one("div.prCn")

                if price:
                    package["price"] = " ".join(price.stripped_strings)

            # ----------------------------
            # Image
            # ----------------------------

            img = card.select_one("img")

            package["image"] = (
                response.urljoin(img["src"])
                if img and img.has_attr("src")
                else ""
            )

            # ----------------------------
            # Detail URL
            # ----------------------------

            detail = card.select_one("a[href]")

            package["detail_url"] = (
                response.urljoin(detail["href"])
                if detail
                else response.url
            )

            # ----------------------------
            # Includes
            # ----------------------------

            includes = []

            for li in card.select("ul li"):
                text = li.get_text(" ", strip=True)

                if text:
                    includes.append(text)

            package["includes"] = includes

            # ----------------------------
            # Raw Text
            # ----------------------------

            package["raw_text"] = card.get_text(
                "\n",
                strip=True,
            )

            # ----------------------------
            # Metadata
            # ----------------------------

            package["city"] = card.get("data-city", "")

            package["duration_days"] = card.get("data-dur", "")

            package["filter"] = card.get("data-all", "")

            if package["title"]:
                packages.append(package)

        return packages