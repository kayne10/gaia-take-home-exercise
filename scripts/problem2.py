import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

'''
Hypothesis1: Users with fewer videos completed/watched are more likely to churn than
users with more videos completed/watched.

Hypothesis2: Users who have a large number of days without watching videos are
more likely to churn than users with significantly less number of days without
watching videos.
'''

# plot for a possible hypothesis1
def plot_vids_completed_vs_videos_watched(df1,df2):
    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_title('Total Videos Completed Vs. Total Videos Watched')
    ax.set_xlabel('Total Videos Watched')
    ax.set_ylabel('Total Videos Completed')
    x1 = df1['total_videos_watched']
    y1 = df1['total_videos_completed']
    x2 = df2['total_videos_watched']
    y2 = df2['total_videos_completed']
    ax.scatter(x1,y1,label='Churned',color='r',alpha=0.9)
    ax.scatter(x2,y2,label='Not Churned',color='b',alpha=0.3)
    plt.savefig('../images/vids_linear.png')

# another plot for a possible hypothesis1
def plot_vids_completed(df):
    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_title('Not Churned & Churned comparisons')
    aggdf = df.groupby('churn').agg(
        {
            'total_videos_watched':'mean',
            'total_videos_completed':'mean'
        }
    )
    aggdf.plot(kind='bar')
    plt.savefig('../images/churn_comparison.png')

# plot for another possible hypothesis2
def plot_days_of_no_activity(df):
    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_title('Not Churned & Churned comparisons')
    aggdf = df.groupby('churn').agg(
        {
            'days_since_last_video_view':'mean',
            'days_since_last_login':'mean'
        }
    )
    aggdf.plot(kind='bar')
    plt.savefig('../images/no_activity.png')

def plot_hist_distribution(df):
    fig = plt.figure(figsize=(15,8))
    ax = fig.add_subplot(111)
    unique_shows,counts = np.unique(df['total_videos_watched'].values,return_counts=True)
    ax.hist(counts,density=True,bins=40,facecolor="darkblue",alpha=0.7,histtype='stepfilled')
    xmin, xmax = ax.get_xlim()
    pdf_range = np.linspace(xmin, xmax, counts.size)
    distn = stats.norm(loc=counts.mean(),scale=counts.std())
    ax.plot(pdf_range, distn.pdf(pdf_range),'darkorange', lw=4, label='pdf');
    plt.show()

def load_data():
    # Loads a CSV file and returns a pandas DataFrame
    df = pd.read_csv('../data/data_science_analyst_data.csv')
    return df

if __name__ == '__main__':
    df = load_data()
    churned = df[df['churn']==1]
    not_churned = df[df['churn']==0]
    plot_vids_completed_vs_videos_watched(churned, not_churned)
    plot_vids_completed(df)
    plot_days_of_no_activity(df)
    # plot_hist_distribution(not_churned)
    # plot_hist_distribution(churned)
