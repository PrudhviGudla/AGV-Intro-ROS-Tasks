# ROS Tasks Documentation

I took screenshots of important things I found on ROS from the wiki ros , surich course, winter workshop, other websites and put them all in a google doc with headings for easy navigation.
https://docs.google.com/document/d/1xJqROzBp-s3CJPQsa1XtOXCJ2lW04Bj3G4JnrTiixrY/edit?usp=sharing

# Intro-ROS-Task1
Done
1) i made a catkin workspace using catkin make.
2) i made a package named task 2
3) i created a folder scripts
4) i wrote two python nodes that publish and subscribe to a topic
5) i wrote a launch file to launch the two nodes simultaneuosly
6) i launched the launch file

![task1](https://user-images.githubusercontent.com/106007058/184814557-ce4531c1-ead1-4d7d-acc6-333f03b7725c.png)

I just faced the problem that there were errors when I forgot to source the environment through
source devel/setup.bash

Also, while writing nodes, I used tab spaces which caused errors.
Then, I found out the indentation required is of 4 spaces not a tab space which is equivalent to 8 spaces

# Intro-ROS-Task2

# Intro-ROS-Task3
Done

https://automaticaddison.com/how-to-launch-the-turtlebot3-simulation-with-ros/#gazebo
1) I installed turtlebot3 into my workspace using the above website as the website was good and provided what I was needing : simulation of turtlebot3
2) I followed the instructions in the website to launch the simulation in Rviz
3) I launched the teleop launch file and controlled the turtlebot using my keyboard.

![Screenshot (606)](https://user-images.githubusercontent.com/106007058/184816577-41292d10-2377-444e-89c3-f0fe09c30ec8.png)
![Screenshot (607)](https://user-images.githubusercontent.com/106007058/184816689-95a1aa17-39f2-44cd-ae2e-e214147c45a7.png)

4) I recorded the topics publised in a bag file using rosbag
5) Then I wrote a node that will access cmd_vel topic of the rosbag, add some gaussian noise using numpy and the publish to the cmd_vel topic.
I launched the simulation. I played the cmd_vel topic of the rosbag. So this time the turtlebot moved with vel values with noise added.
![Screenshot (605)](https://user-images.githubusercontent.com/106007058/184818071-cd17460b-b48b-458a-aecc-a1830796436a.png)

![Screenshot (609)](https://user-images.githubusercontent.com/106007058/184817450-c71f97b5-054d-4ed1-9005-997e78935f42.png)
![Screenshot (610)](https://user-images.githubusercontent.com/106007058/184817532-7f1e33f8-8034-4bc2-9ef6-dccd3f4bb328.png)

6) In the node, I made it print all the twist messages after addition of noise. I also printed the linear.x before addition of noise for comparison.
![Screenshot (604)](https://user-images.githubusercontent.com/106007058/184818019-898d245d-86e2-4763-bb3f-a25c0469b056.png)

I faced problems with the syntax of python while writing the node due to no prior experience with python.
Now, I have started learning python in a proper way.

