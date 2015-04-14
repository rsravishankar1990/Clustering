#Scaling effect of variables

This snippet just shows why standardizing variables is an important
thing before clustering. The scale of the variables plays a huge effect
in the dissimilarity values that are calculated between objects.

#Euclidean Distance:

The euclidean distance is proportional to the difference between each 
data point on each dimension. The only way the difference can grow or 
shrink in value is if the weightage applied to a particular variable is
increased or decreased. The scale of the variable implies a weightage. 

For example, the difference between the inches and foot while measuring
height could make a huge difference while computing dissimilarity values.

#Example

In this snippet, a naive example has been taken for three objects and 
their heights and weights. 

Name		(Height,		Weight)

Ravi		(12,			95)
Shankar		(1075,		93)
Raja		(13,			115)

Here it can be seen that the objects 'Ravi' and 'Shankar' are similar in Weight,
but very dissimilar in Height. And its opposite with 'Ravi' and 'Raja'.
The snippet goes through a range of scaling values to increase the scale of
Weight and tries to see which of 'Shankar' or 'Raja' is closer to 'Ravi'.
As the scaling values increase, the originally closer 'Raja' starts becoming
distant to 'Ravi' as can be seen from this graph.

![Effect of scale of variables in clustering](/Scaling Effect/Scaling Effect in clustering.png)
