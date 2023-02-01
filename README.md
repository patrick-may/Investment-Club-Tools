# Jenny Portfolio Repository
A repo with various useful code-centered tools for the *Hans H. Jenny Investment Club* to be used in making easy and nice graphics, verifying if a stock meets guidelines, etc.

# Tools Here Currently
`guideline_verifier.ipynb` - is a simple script that auto-pulls financial data from an open yahoo finance endpoint and calculates their YoY changes. I am certain there is a more efficient way to do this analysis, but the dataframe I get from working with yfinance is a bit wacky so I have instead worked around it in an inefficient way.

You will need to install various dependencies, but then all you need to do is change the `lookup` variable to the ticker you want to investigate.
