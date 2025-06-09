import pandas as pd
import os

os.chdir("C:/Users/andre/Dropbox/MLX/week 1/hackernews_upvote_predictor")

df = pd.read_parquet("data/submissions.parquet.gzip", compression='gzip')   



