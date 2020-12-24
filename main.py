
import curses

class Servo:
    def __init__(self, servo_name, min_angle, max_angle):
        self.servo_name=servo_name
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.last_angle_set_perc=0
        self.last_angle_set=self.min_angle

    
    def __str__(self):
        return "{} angle range from '{}' to '{}'".format(self.servo_name, self.min_angle, self.max_angle)

    def set_angle_servo(self, set_angle, perc_flag):
        if perc_flag:
            set_angle_deg = ((self.max_angle - self.min_angle)*(set_angle/100)) + self.min_angle
            set_angle_perc = set_angle
        else:
            set_angle_deg = set_angle
            set_angle_perc = (((set_angle-self.min_angle)/(self.max_angle - self.min_angle))*100) #correct this line

        print("Set {} to {}%({})".format(self.servo_name, set_angle_perc, set_angle_deg))
        self.last_angle_set_perc = set_angle_perc
        self.last_angle_set = set_angle_deg
        
        #put here rasp pi command for servo
          
    def increase_angle(self,angle_step):
        new_angle = self.last_angle_set_perc + angle_step
        set_angle_servo(new_angle,True)
        print(self.last_angle_set_perc)
        
    def decrease_angle(self,angle_step):
        new_angle = self.last_angle_set_perc - angle_step
        set_angle_servo(new_angle,True)
        print(self.last_angle_set_perc)


servo1 = Servo('Servo1',50,150)
servo2 = Servo('Servo2',50,150)
servo3 = Servo('Servo3',50,150)
servo4 = Servo('Servo4',50,150)

servo1.increase_angle(2)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
# screen = curses.initscr()
# curses.noecho() 
# curses.cbreak()
# screen.keypad(True)

# try:
#         while True:   
#             char = screen.getch()
#             if char == ord('q'):
#                 break
#             elif char == curses.KEY_UP:
#                 print ("up")
#             elif char == curses.KEY_DOWN:
#                 print ("down")
#             elif char == curses.KEY_RIGHT:
#                 print ("right")
#             elif char == curses.KEY_LEFT:
#                 print ("left")
#             elif char == 10:
#                 print ("stop")
#             else:
#                 print(char)    
             
# finally:
#     #Close down curses properly, inc turn echo back on!
#     curses.nocbreak(); screen.keypad(0); curses.echo()
#     curses.endwin()