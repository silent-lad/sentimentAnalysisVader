from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
#from vaderSentiment import SentimentIntensityAnalyzer

# --- examples -------
sentences = ["VADER is smart, handsome, and funny.",  # positive sentence example
             # punctuation emphasis handled correctly (sentiment intensity adjusted)
             "VADER is smart, handsome, and funny!",
             # booster words handled correctly (sentiment intensity adjusted)
             "VADER is very smart, handsome, and funny.",
             "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
             # combination of signals - VADER appropriately adjusts intensity
             "VADER is VERY SMART, handsome, and FUNNY!!!",
             # booster words & punctuation make this close to ceiling for score
             "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!",
             "VADER is not smart, handsome, nor funny.",  # negation sentence example
             "The book was good.",  # positive sentence
             # negated negative sentence with contraction
             "At least it isn't a horrible book.",
             # qualified positive sentence is handled correctly (intensity adjusted)
             "The book was only kind of good.",
             # mixed negation sentence
             "The plot was good, but the characters are uncompelling and the dialog is not great.",
             "Today SUX!",  # negative slang with capitalization emphasis
             # mixed sentiment example with slang and constrastive conjunction "but"
             "Today only kinda sux! But I'll get by, lol",
             "Make sure you :) or :D today!",  # emoticons handled
             "Catch utf-8 emoji such as such as 💘 and 💋 and 😁",  # emojis handled
             "Not bad at all"  # Capitalized negation
             ]

analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))
