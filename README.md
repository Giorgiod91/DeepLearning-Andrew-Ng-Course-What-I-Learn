# DeepLearning-Andrew-Ng-Course-What-I-Learn

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
