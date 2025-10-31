# DeepLearning-Andrew-Ng-Course-What-I-Learn
# Goal ---  Understand the Math behind ML 

Neural Network Basic

- House Pricing Example
  input x = House size => Neuron => Output(Price y)
  Relu function for Linear (Max of 0)

# Neural Network

- Uses multiple Neurons
  - for example with the house pricing multiple neurons with data like size, walkability
  - in this example 4 input x and the middle will be figured out by itself
    ![alt text](image-1.png)

the middle ones are called hidden layer
![alt text](image-2.png)

# Model Types

- for example with the house pricing it could use a standard NN (NeuralNetwork)
- CNN Convulutional NN ofent used for Image data
- RNN Recurrent Neural Network
- Custom / Hybrid

# Structured and Unstructured Data

- Structured like a Table with conenctions

Unstructured => for example audio files or images, piece of Text

# Learning progress

- what is effecting the Progress -![alt text](image-3.png)
- scaled data
- the switch from sigmoid funtion to railer funciton
  ![alt text](image-4.png)
- so algorithms cane change the speed of the code and computation so it will can run much faster

# Graded Test to check if i understood those things

ChecK

# Binary classification

# Logistic Regresssion

- for example 1(cat) vs 0 (no Cat) so binary
- Image example what happens under the hood
  -putting for an image all colors so red blue green into a vector then if we have an image for 64x64 pixels it would look like this
  ![alt text](image-5.png)
  maths = (x,y)
  where x is an x dimensional feature vector
  and y the label is either 0 or 1
  ![alt text](image-6.png)
  training examples = (x(1),y(1)),(x(2),y(2)),(x(m),y(m))
  where xm is the last training example
  M = Mtrain

M test(subscript) = number of test examples

![alt text](image-8.png)

Put those x(1) ,x(2) into a Matrix
So Matrix X where M is the number of training examples and the height of this Matrix is NX or called railroads

![alt text](image-7.png)

# x.shape

. python command for finding the shape of the matrix

# y.shape

# Logistic regression

- Given x , want Y^=P(y=1/x)
- X is an X dimensional vector
  Parameters : W also and X dimensional vector
  and b which is just a real number
  Output Y^ =

# sigmoiod function

![](2025-10-26-11-17-30.png)!

Case 1-----> if z is large == then e to the nefative z will be close to 0
that also means if z is very large then sigmoid of z is very close to 1
Case 2-----> if z is very small or a verz large negative number
then sigmoid of z comes very close to zero

# what that all means

- we want to predict something that has only 2 outcomes (0 or 1)
- to make these prediction using two things the parameters (W,B)
- W → weights (how important each feature is)
- B → bias (a number to adjust the prediction)
  ====> so the goal is We want our model to correctly predict the probability that the answer is 1 (true).
  and this is done by tuning W and B

  # Loss(error) function

  ![](2025-10-26-11-37-28.png)

  ![alt text](image-9.png)

- so if y= 1 we want y hat to be large and if y=0 we want y hat to be small and the y hat is the formual y^​=σ(wTx+b) so we change the parameters to archiev this (parameter = w and b)

  # Cost function

J(w,b) = 1/m
![alt text](image-10.png)

# Rules

- the Loss function will be used on a single training example
  ![alt text](image-11.png)
- the cost function will be applied to the entire training set
  J(w,b) = ![alt text](image-12.png)

# Math extra

- how does a convex function look
  ![alt text](image-13.png)

- how does a non convex function look

![alt text](image-14.png)

# Gradient Decent

- initalizing w and b
- it will goe downhill in the direction of steepest decent from the initalizet value

![alt text](image-15.png)

- w = w- alpha(thats the learning rate it will control how big the steps are on eacdh iteration of gradient decent) dJ(w) / dw
- this will be repeated und the algorithm converged or in other word if the algo stops if it doesnt change much anymore
- this is with only b as a parameter but J(w,b) has two then it would look like this
- w:= w-alpha dJ(w,b)/dw
- b:= b-alpha dJ(w,b)/db

# Calculus Tips

- partial derivative symbol will be used instead of lower case d if the function J has 2 or more parameters
  ![alt text](image-16.png)

- The derivative is the slope — it shows how much
  𝑓(𝑥) changes when x changes a little.
  ![alt text](image-17.png)

- rule for
  ![](image-18.png)
- If a goes up a little, a² goes up about 2a times as much
  ![alt text](image-19.png)
- examples
  ![alt text](image-20.png)

-chain rule
![alt text](image-21.png)

- here was dj/dv =3 and dv/da = 1 so dj/da = 3

- backpropagation
  ![alt text](image-22.png)
- what has been done here ===> go backward and figured out that dv = 3 (dj/dw)
  da = 3 dj/da
  ![alt text](image-23.png)
- another example here if we want to find out dj/db
  ![alt text](image-25.png)

# Gradient Descent in Logitic Regression

![](image-26.png)

- goal here is to check how L changes it we switch up w1, w2, or b by a bit
- the chain rule dl/dz = dl/da \* da/dz
