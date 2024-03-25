# Review extractor

To grab all reviews from pull requests up to 6 months old:

`python grabreviews.py > reviews.txt`

In reality, it may get only 4 months due to rate limits

Special characters in review comments will land in binary, making it difficult to grep. So copy entire contents of `reviews.txt` and paste it into a new file `reviews-t.txt` in vscode.

Do your greps on `reviews-t.txt`, or use
`python extractenglish.py >reviews-english.txt`

Similarly copy entire contents of `reviews-english.txt` and paste to `reviews-english-t.txt`

Then use `python hashtohash_comment.py` 