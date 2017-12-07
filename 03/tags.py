from collections import Counter
from difflib import SequenceMatcher
from itertools import product, combinations
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open(RSS_FEED) as f:
        feed = f.read().lower()

    return [tag.replace('-', ' ') for tag in TAG_HTML.findall(feed)]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    # product = ((tag_a,tag_b) for tag_a in tags for tag_b in tags)
    t = sorted(set(tags))
    combos = combinations(t, 2)
    for tag_a, tag_b in combos:
        if tag_a[0] != tag_b[0]:
            continue
        ratio = SequenceMatcher(None, tag_a, tag_b).ratio()
        if ratio > SIMILAR:
            yield (tag_a, tag_b)


def get_similarities2(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    for pair in product(tags, tags):
        # performance enhancements 1.992s -> 0.144s
        if pair[0][0] != pair[1][0]:
            continue
        pair = tuple(sorted(pair))  # set needs hashable type
        similarity = SequenceMatcher(None, *pair).ratio()
        if SIMILAR < similarity < IDENTICAL:
            yield pair


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    get_similarities(tags)
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
