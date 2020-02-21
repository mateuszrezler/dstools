from IPython.display import display as dp, Markdown as md
import pandas as pd


def df_summary(df, heading='Summary', heading_level=3):
    """Display rendered summary of a DataFrame."""
    table = pd.concat(
        [df.dtypes, df.isnull().sum(), (~df.isnull()).sum()], axis=1)
    table.reset_index(inplace=True)
    table.columns = 'Columns', 'Dtype', 'Null', 'Non-Null'
    dp(md('#'*heading_level + f' {heading}\n'
          f'*Rows*: **{df.shape[0]}**  \n'
          f'*Columns*: **{df.shape[1]}**'), table)

