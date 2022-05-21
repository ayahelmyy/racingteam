#!/usr/bin/env python3
# # license removed for brevity
import rospy
from std_msgs.msg import String
def callback(data):  
    rospy.loginfo("rescevied data:%s", data.data)
def listener():
    rospy.init_node("data_processing",anonymous= True)      
    rospy.Subscriber('/raw_data',String,callback)
    rospy.spin() 
if __name__ == '__main__':
      try:
         listener()
      except rospy.ROSInterruptException:
         pass