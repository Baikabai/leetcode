from keybert import KeyBERT


doc = """Electric vehicle batteries are in short supply, and costs for materials such as nickel and cobalt are surging. Yet legacy automaker Ford Motor says it plans to be profitably building millions of EVs a year in just four years.

This week, the Detroit automaker gave investors a little more clarity about how it plans to reach that goal and transform its business built on gas-guzzling cars.

As electric vehicles account for a growing share of the global car market, Ford in March announced it would reorganize its business and separate its internal-combustion engine and electric vehicle efforts. By 2026, it said it expects to build more than 2 million electric vehicles annually — about a third of its total global production — while expanding its operating profit margin.

Wall Street analysts were generally positive about the plan, but some expressed skepticism about the lack of specifics around how the company plans to overcome the supply challenges in the market. Morgan Stanley’s Adam Jonas called it a “stretch” goal and said he lacked confidence in Ford’s ability to secure enough raw materials and tooling to manufacture batteries to even come close to its projection.

Ford addressed some of those concerns in another presentation on July 21, when it told investors that it has secured enough batteries to get to its near-term target: 600,000 EVs per year by the end of 2023. As of now, it said, it has secured about 70% of what it needs to hit its 2026 goal.

Ford promised to share more about how it plans to hit its goals during its annual capital markets day next year. But during its second-quarter earnings call last week, CEO Jim Farley gave some more hints about the automaker’s strategy.
"""
kw_model = KeyBERT()

print(kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), stop_words=None,top_n=8))