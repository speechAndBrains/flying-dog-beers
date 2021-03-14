#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:08:52 2021

@author: sam
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.figure_factory as ff
import math 
import plotly.graph_objects as go
import pandas as pd
import scipy.stats as sc


#get style sheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#initialise
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

###################
#starting parameters for fig 1 and 2 - e.g. example 1
ex1_startingMean=5
ex1_startingSD=1
ex1_startingSampleSize=10
###################
#starting paramters for fig 3 - e.g. example 2
ex2_startingMean_1=0
ex2_startingMean_2=10
ex2_startingSampleSize=50
ex2_startingSD=1

################# Example 1 - Figs 1 and 2
#generate data for example 1
ex1_init=np.round(np.random.normal(ex1_startingMean, ex1_startingSD, ex1_startingSampleSize))
#calculate the actual mean
trueMean=np.mean(ex1_init)

fig1=px.scatter(x=ex1_init, y=[range(1,11,1)],range_x=[-20, 40],title='Scatter Plot')

fig2 = ff.create_distplot([ex1_init],['group1'],bin_size=0.1, show_rug=False)

####################Example 2 - Fig 3 & 4
#generate data for two samples
ex2_init1=np.round(np.random.normal(ex2_startingMean_1, ex2_startingSD, ex2_startingSampleSize))
ex2_init2=np.round(np.random.normal(ex2_startingMean_2, ex2_startingSD, ex2_startingSampleSize))

fig3=go.Figure()
fig3.add_trace(go.Histogram(x=ex2_init1,histnorm='probability density'))#,nbins=[np.round(1+math.log(50,2))])#,histnorm='probability density'))
fig3.add_trace(go.Histogram(x=ex2_init2,histnorm='probability density'))

fig4=go.Figure()
fig4.add_trace(go.Scatter(mode='markers',x=ex2_init1,marker=dict(color='LightSkyBlue')))
fig4.update_layout(xaxis_range=[-50,50])
fig4.add_trace(go.Scatter(mode='markers',x=ex2_init2,marker=dict(color='Red')))
##########
fig5=go.Figure()

app.layout = html.Div([
    dcc.Markdown('''
                 # 5PSYC011W Cognitive and Clinical Research Methods 
                 > Content created by Dr. Samuel Evans - S.Evans1@westminster.ac.uk  
                 > This interactive tutorial is made using Python and the Dash library.  Please feel free to distribute and make use of it in teaching and learning.      
                 
                 ## Understanding means, variance, standard deviation and probability distributions  
                    
                 ---
                 **Learning Outcomes:**
                 * To remind you how means, variance and the standard deviation is calculated
                 * To understand how means and standard deviations influence the outcome of statistical tests
                 * To understand the concept underlying probability distributions and how they are used to derive p-values
                 ---
                 
                  **Basic calculations: means, variance and standard deviation**   
                 
                  You can get a really long way in statistics by just understanding 
                  what means, variance and standard deviations are. These simple calculations are the basis of most
                  parametric statistics that use the general linear model (e.g. t-tests, ANOVAs, multiple regression).
                 
                  Everyone knows how to calculate the mean of a set of numbers. 
                  It's just the 'average'. We calculate it by adding a set of 
                  numbers together and dividing by the number of numbers in the set. 
                  We use statistics like the mean
                  as a simple way of summarising a set of numbers, so that we 
                  don't have to write out all the numbers in a set in order to descrbe them.
                
                  That's why we use means to describe data. When we use the mean, we no longer need to 
                  write all the numbers out, we can just write one number that 
                  represents the set. The mean tells us about the general magnitude of a set of numbers
                  but it doesn't tell us how spread out the numbers are. 
                  That's why we calculate the variance or standard deviation. 
                 
                  The more spread out the numbers are within a set, the worse the mean is as a summary
                  of the numbers. Imagine if a set of number were \[100 100 100 100 100 100] then the 
                  mean would be exactly 100 - e.g. a perfect summary. However, if the values
                  vary a lot such as \[10000 100 100 100 1 1], the mean is 1,717 and clearly
                  is not a very useful summary of the values. 
                 
                  Variance and the standard deviation are ways of describing the 
                  spread of data.  Another way of thinking 
                  about it, is that variance and standard deviation tell us how precise or
                  accurate the mean is as a summary of the data. 
                 
                  In the case of the set \[100 100 100 100 100 100], the mean is 100 and 
                  the standard deviation is 0. Here, the mean is a perfect summary of the data.
                  If the variance or standard deviation is above 0 this means that there
                  is some variation around the mean - that is the mean is
                  not a perfect summary of the data. A larger variance or standard deviation means the 
                  numbers in the set are more spread out from one another and so the mean is a worse summary of the data.
                 
                 > **Play around with the mean and standard deviation of the sample using these sliders**
                 
                 > ** 1. Make sure you understand how the variance and standard deviation are calculated by looking at the box below.  Notice this updates everytime you move the slider.**
                 > 
                 > ** 2. What happens to the data points when you increase the standard deviation?**
                 > 
                 > ** 3. What is the relationship between the scatter plot and the histogram?**
                 '''
    ),
    html.Div(
        children='Change the target mean with this slider:'
    ),
    html.Div(
        id='ex1_mean_output',
        children=str(ex1_startingMean)
    ),
    dcc.Slider(
        id='ex1_mean',
        min=0,
        max=10,
        step=1,
        value=ex1_startingMean,
        marks={0:'0',10:'10'},
    ),
    html.Div(
        'Change the target standard deviation with this slider:'
    ),
    html.Div(
        id='ex1_sd_output',
        children=str(ex1_startingSD)),
    dcc.Slider(
        id='ex1_sd',
        min=0,
        max=10,
        step=0.1,
        value=ex1_startingSD,
        marks={0:'0',10:'10'}
    ),
    dcc.Textarea(
        id='ex1_textarea',
        value='The Values are: ' + str(ex1_init),
        style={'width': '100%', 'height': 200},
    ),
    dcc.Markdown('''
                 The calculation above is the population standard deviation when you know you have measured the whole population of a sample
                 in psychology this hardly ever happens.  Instead we mostly calculate the sample standard deviation. To do this you divide by the number of our participants minus 1 \[e.g. n-1].
                 For the sample standard deviation dividing by n-1 allows you to account for the uncertainty involved in measuring a sample rather than the whole population.
                 '''
    ),
    dcc.RadioItems(
        id='ex_radio1',
        options=[
        {'label': 'Show deviations', 'value': 'Yes'},
        {'label': 'Hide deviations','value': 'No'}
        ],
        value='No'
        ),
    dcc.Graph(
        id='example-graph_1',
        figure=fig1
    ),
    dcc.Graph(
        id='example-graph_2',
        figure=fig2
    ),
    dcc.Markdown('''
                 **Understanding how and why means and variance/standard deviation affect statistical tests**    
                 Most statistical tests are just a ratio of the size of the effect divided by the error in measurement of that effect.
                 In the case of an independent t-test, this size of effect is the difference between the means of the two groups. 
                 The experimental hypothesis predicts that this difference will be large.  This is then divided by the amount of error in measurement. 
                 This is estimated from the amount of variation in the numbers.  If you remember the means are a good estimate of the data, 
                 if there is only a small amount of variation in the set of numbers. So it makes sense to use the variation in measurement 
                 to estimate the amount of error.  Because they are a ratio, if the number on the top is large and the number underneath is small, this will result in a large number, 
                 if it is the other way around and the error is larger it will result in a small number.
                 
                 > **Play around with the mean and standard deviation of two sample using these sliders.  Below the graph you can see how the t-value
                 > and p-value of an independent samples t-test changes**    
                 
                 > **1. Keep the standard deviation low.  Start with the same means and then slowly move the means apart.  How do the statistics change?**   
                 
                 > **2. Now set the means and only chnage the standard deviation. What happens as the standard deviation increases?**                
                 '''),
    html.Div(
        children='Change the target mean for sample 1 with this slider:'
    ),
    html.Div(
        id='ex2_mean_output_1',
        children=str(ex2_startingMean_1)
    ),
    dcc.Slider(
        id='ex2_mean_1',
        min=0,
        max=10,
        step=0.1,
        value=ex2_startingMean_1,
        marks={0:'0',10:'10'},
    ),
    html.Div(
        children='Change the target mean for sample 2 with this slider:'
    ),
    html.Div(
        id='ex2_mean_output_2',
        children=str(ex2_startingMean_2)
    ),
    dcc.Slider(
        id='ex2_mean_2',
        min=0,
        max=10,
        step=0.1,
        value=ex2_startingMean_2,
        marks={0:'0',10:'10'},
    ),
    html.Div(
        children='Change the target SD for both samples:'
    ),
    html.Div(
        id='ex2_sd_output',
        children=str(ex2_startingSD)
    ),
    dcc.Slider(
        id='ex2_sd',
        min=0,
        max=10,
        step=0.1,
        value=ex2_startingSD,
        marks={0:'0',10:'10'}
    ),
    dcc.Graph(
        id='example-graph_3',
        figure=fig3),
    dcc.Textarea(
        id='ex2_textarea',
        value='',
        style={'width': '100%', 'height': 30},
    ),
    dcc.Markdown(''' 
                 **How is the t-statistic actually calculated?**  
                 As we said above the t-statistic is just a ratio of the size of the effect (the difference between the means).  Divided 
                 by the error in measurement (the amount of variation in measurement).  In the case of an independent samples t-test this is the 
                 pooled standard deviation of both samples.
                 > **Play around with the sliders of the means and standard deviation to see '''
    ),
    dcc.RadioItems(
        id='ex_radio2',
        options=[
        {'label': 'Show deviations', 'value': 'Yes'},
        {'label': 'Hide deviations','value': 'No'}
        ],
        value='No'
    ),
    dcc.Graph(
        id='example-graph_4',
        figure=fig4),
    html.Button('Go!', id='ex3_button', n_clicks=0),
    dcc.Graph(
        id='example-graph_5',
        figure=fig5),
])

@app.callback(
    Output('example-graph_1', 'figure'),
    Output('example-graph_2', 'figure'),
    Output('ex1_mean_output', 'children'),
    Output('ex1_sd_output','children'),
    Output('ex1_textarea','value'),
    Input('ex1_mean', 'value'),
    Input('ex1_sd', 'value'),
    Input('ex_radio1','value')
    )
def callback_a(ex1_mean,ex1_sd,showDevs1):
    #change sample size for flecibilitibitly!!
    ##Example 1 - Figs 1 & 2
    x1=np.round(np.random.normal(ex1_mean, ex1_sd,10))
    trueMean=np.mean(x1)
    fig1=px.scatter(x=x1, y=[range(1,11,1)],range_x=[-20, 40],title='Scatter Plot')
    fig1.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink',tickmode="auto",nticks=100)
    fig1.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig1.add_shape(type="line", x0=trueMean, y0=1, x1=trueMean, y1=10,line=dict(color="Blue",width=4,dash="dashdot"))
    
    #If display deviations is ticked
    if showDevs1 == 'Yes':
        for i in range(len(x1)):
            fig1.add_shape(type="line", x0=trueMean, y0=i+1, x1=x1[i], y1=i+1,line=dict(color="LightBlue",width=4,dash="dashdot"))
                       
    fig1.update_shapes(dict(xref='x', yref='y'))
   
    
    fig1.layout.update(showlegend=False)
    returnText='The Values are: ' + str(x1) + '\n' + '\n' + 'Population standard deviation' + '\nStep 1. Calculate the mean by adding the values and dividing by the number of numbers: ' + str(trueMean) + '\nStep 2. Subtract the mean from each value: ' + str(x1-trueMean) + \
        '\nStep 3. Square them: ' + str((x1-trueMean)**2) + '\nStep 4: Sum them: ' + str(sum((x1-trueMean)**2)) + \
            '\nStep 5: Take the mean of the squared differences (the variance): ' + str((sum((x1-trueMean)**2))/len(x1)) + '\nStep 6: Squareroot to undo the squaring (the population standard deviation): ' + \
                str(math.sqrt((sum((x1-trueMean)**2))/len(x1))) 
                
    fig2=px.histogram(x=x1,nbins=60,range_x=[-20, 40],title='Histogram')
    #fig2 = ff.create_distplot([x1],['group1'],bin_size=0.1, show_rug=False)
    #fig2.layout.update(showlegend=False)
    #fig2.update_layout(xaxis_range=[-20,40])
    fig2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink',tickmode="auto",nticks=100)
    
    
    return fig1,fig2,ex1_mean, ex1_sd, returnText

@app.callback(
    Output('example-graph_3', 'figure'),
    Output('example-graph_4', 'figure'),
    Output('ex2_mean_output_1', 'children'),
    Output('ex2_mean_output_2','children'),
    Output('ex2_sd_output','children'),
    Output('ex2_textarea','value'),
    Input('ex2_mean_1', 'value'),
    Input('ex2_mean_2', 'value'),
    Input('ex2_sd', 'value'),
    Input('ex_radio2','value'),
    )
def callback_a(ex2_mean_1,ex2_mean_2,ex2_sd,showDevs2):
    #change sample size for flecibilitibitly!!
    ##Example 1 - Figs 1 & 2
   
    ex2_x1=np.round(np.random.normal(ex2_mean_1, ex2_sd,100))
    ex2_x2=np.round(np.random.normal(ex2_mean_2, ex2_sd,100))
      
    fig3=go.Figure()
    fig3.add_trace(go.Histogram(x=ex2_x1))#,histnorm='probability density'))#,nbins=[np.round(1+math.log(50,2))])#,histnorm='probability density'))
    fig3.add_trace(go.Histogram(x=ex2_x2))#,histnorm='probability density'))#,nbins=[np.round(1+math.log(50,2))])#,histnorm='probability density'))   
    fig3.update_layout(barmode='overlay')
    fig3.update_layout(xaxis_range=[-50,50])
    fig3.update_traces(opacity=0.7)
    fig3.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink',tickmode="auto",nticks=100)
    fig3.layout.update(showlegend=False)
    result=sc.ttest_ind(ex2_x1,ex2_x2)
    
    ex2_returnText='T-value: ' + str(result[0]) + ' pvalue: ' + str(result[1])
    
    fig4=go.Figure()
    fig4.add_trace(go.Scatter(mode='markers',x=ex2_x1,marker=dict(color='Blue')))
    fig4.update_layout(xaxis_range=[-50,50])
    fig4.add_trace(go.Scatter(mode='markers',x=ex2_x2,marker=dict(color='Red')))
    fig4.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink',tickmode="auto",nticks=100)
    fig4.layout.update(showlegend=False)
    fig4.add_shape(type="line", x0=np.mean(ex2_x1), y0=1, x1=np.mean(ex2_x1), y1=100,line=dict(color="Blue",width=4,dash="dashdot"))
    fig4.add_shape(type="line", x0=np.mean(ex2_x2), y0=1, x1=np.mean(ex2_x2), y1=100,line=dict(color="Red",width=4,dash="dashdot"))
    
   # fig4.add_shape(type="line", x0=np.mean(ex2_x1), y0=i+1, x1=x1[i], y1=i+1,line=dict(color="LightBlue",width=4,dash="dashdot"))
    trMean1=np.mean(ex2_x1)
    trMean2=np.mean(ex2_x2)
    
    if showDevs2 == 'Yes':
       for i in range(len(ex2_x1)):
           fig4.add_shape(type="line", x0=trMean1, y0=i+1, x1=ex2_x1[i], y1=i+1,line=dict(color="Blue",width=4,dash="dashdot"))
           fig4.add_shape(type="line", x0=trMean2, y0=i+1, x1=ex2_x2[i], y1=i+1,line=dict(color="Red",width=4,dash="dashdot"))
           fig4.update_shapes(dict(xref='x', yref='y'))
    
    
    return fig3, fig4, ex2_mean_1,ex2_mean_2,ex2_sd, ex2_returnText

@app.callback(
    Output('example-graph_5', 'figure'),
    Input('ex3_button', 'value'),
    )
def callback_a(clickz):
    distr=np.random.normal(0,1,1000)

    #fig5=go.Figure()
    #fig5.add_trace(go.Histogram(x=distr))
    
    fig5=go.Figure() 
    
    if clickz is not None:
        fig5 = ff.create_distplot([distr],['group1'],bin_size=.1)
    #fig5=px.histogram(x=distr,nbins=1000,title='Histogram of null distribution')
    
      
    return fig5

if __name__ == '__main__':
    app.run_server(debug=True)   