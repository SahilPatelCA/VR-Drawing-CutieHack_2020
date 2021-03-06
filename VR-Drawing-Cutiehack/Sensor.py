###############################################################################
# Copyright (C) 2012-2016 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys, thread, time, socket


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

    def on_init(self, controller):
        print ("Initialized")

    def on_connect(self, controller):
        print ("Connected")

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print ("Disconnected")

    def on_exit(self, controller):
        print ("Exited")

    def on_frame(self, controller):
   
        # Get the most recent frame and report some basic information
        frame = controller.frame()


        # Get hands
        for hand in frame.hands:

            #Checks if hand is left or right
            #handType = "Left hand" if hand.is_left else "Right hand"

            intPos = []
            thumbPos = []
            indexPos = []
   
            # Get fingers
            for finger in hand.fingers:

                #Thumb
                if(finger.type == 0):
                    thumbPos.append(int(finger.tip_position[0]))
                    thumbPos.append(int(finger.tip_position[1]))
                    thumbPos.append(int(finger.tip_position[2]))


                #Index
                if(finger.type == 1):
                    indexPos.append(int(finger.tip_position[0]))
                    indexPos.append(int(finger.tip_position[1]))
                    indexPos.append(int(finger.tip_position[2]))

                # print finger.tip_position


                # print "    %s finger, id: %d, length: %fmm, width: %fmm" % (
                #     self.finger_names[finger.type],
                #     finger.id,
                #     finger.length,
                #     finger.width)
                

            

            print("Coordinates of Index Finger: " )
            print(indexPos)
            print("Coordinates of Thumb: " )
            print(thumbPos)
            intPos = [indexPos, thumbPos]
            for arr in intPos:
                #x
                if arr[0] > 400:
                    arr[0] = 400
                elif arr[0] < -400:
                    arr[0] = -400

                #y
                if arr[1] > 800:
                    arr[1] = 800
                elif arr[1] < 50:
                    arr[1] = 50

                #z
                if arr[2] > 300:
                    arr[2] = 300
                elif arr[2] < -300:
                    arr[2] = -300
            print("2D Array of Index and Thumb")
            print(intPos)

            #Send information to the connected client, if one isnt there wait for connection of another client
            try:
                clientsocket.send(str(intPos))
            except:
                waitForConnection()


        if not frame.hands.is_empty:
            print ("")

        #If no hands are detected send a zero vector to the client
        if frame.hands.is_empty:
            print("No Hands Detected")
            zeroVector = [[-30, 450, -30], [30, 450, 30]]

            #Send information to the connected client, if one isnt there wait for connection of another client
            try:
                clientsocket.send(str(zeroVector))
            except:
                waitForConnection()


#Initializes hand tracker class
def main():
    
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until "Enter" is pressed
    print ("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


#Function to pause program until a websocket connection is made
def waitForConnection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1243))
    s.listen(5)
    print("Listening for a connection")
    global clientsocket
    global address
    clientsocket, address = s.accept()
    print("Connection found")


#Waits for a client to connect to the websocket then proceeds to send coordinates to the client when they connect
if __name__ == "__main__":
    global s
    waitForConnection()
    main()

