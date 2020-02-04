from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
import cv2
import random
import time
from copy import deepcopy
import imutils
from object_detection import object_detector



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 865)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 164, 186, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(166, 167, 175, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 80, 781, 621))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 90, 211, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(40, 50, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        
        
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 101, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 760, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 240, 211, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 440, 211, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_2")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setGeometry(QtCore.QRect(40, 40, 101, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_6.setGeometry(QtCore.QRect(40, 70, 101, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_7.setGeometry(QtCore.QRect(40, 100, 101, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(40, 40, 111, 20))
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setGeometry(QtCore.QRect(40, 70, 101, 20))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 760, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 20, 651, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Object Detection and Tracking"))
        self.label.setText(_translate("MainWindow", "Output"))
        self.groupBox.setTitle(_translate("MainWindow", "Trackers"))

        #self.comboBox.activated.connect(self.multipletracker)
        self.comboBox.setItemText(0, _translate("MainWindow", "Choose Any"))
        self.comboBox.setItemText(1, _translate("MainWindow", "BOOSTING"))
        self.comboBox.setItemText(2, _translate("MainWindow", "MIL"))
        self.comboBox.setItemText(3, _translate("MainWindow", "KCF"))
        self.comboBox.setItemText(4, _translate("MainWindow", "TLD"))
        self.comboBox.setItemText(5, _translate("MainWindow", "MEDIANFLOW"))
        

        
        self.label_2.setText(_translate("MainWindow", "Multiple Trackers"))

        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton.clicked.connect(self.process)
        
        self.groupBox_2.setTitle(_translate("MainWindow", "Detection with DL"))
        self.checkBox_5.setText(_translate("MainWindow", "YOLO"))
        self.checkBox_6.setText(_translate("MainWindow", "SSD"))
        self.checkBox_7.setText(_translate("MainWindow", "MASK-RCNN"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Detection + Tracking"))
        self.checkBox.setText(_translate("MainWindow", "YOLO with KCF"))
        self.checkBox_2.setText(_translate("MainWindow", "SSD with KCF"))
        self.pushButton_3.setText(_translate("MainWindow", "STOP"))
        self.pushButton_3.clicked.connect(self.stop)
        self.label_3.setText(_translate("MainWindow", "Real Time Object Detection and Tracking"))

    def process(self,i):
        item = (self.comboBox.currentIndex())
        if item == 1:
            self.boosting()
        elif item==2:
            self.mil()
        elif item==3:
            self.kcf()
        elif item==4:
            self.tld()
        elif item==5:
            self.medianflow()
    
        else:
            pass

       
        
        
        if self.checkBox_5.isChecked() == True:
            self.yolo()
        elif self.checkBox_6.isChecked() == True:
            self.ssd()
        elif self.checkBox_7.isChecked() == True:
            self.maskrcnn()
        elif self.checkBox.isChecked() == True:
            self.yolokcf()
        elif self.checkBox_2.isChecked() == True:
            self.ssdkcf()
        else:
            pass
    
    def stop(self):
        if cv2.waitKey(1):
            cap.release()
            cv2.destroyAllWindows()
            self.label.clear()
           
    def boosting(self):
        global cap
        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
        tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW']
        tracker_type = tracker_types[0]
     
        if int(minor_ver) < 3:
            tracker = cv2.Tracker_create(tracker_type)
        else:
            if tracker_type == 'BOOSTING':
                tracker = cv2.TrackerBoosting_create()
            if tracker_type == 'MIL':
                tracker = cv2.TrackerMIL_create()
            if tracker_type == 'KCF':
                tracker = cv2.TrackerKCF_create()
            if tracker_type == 'TLD':
                tracker = cv2.TrackerTLD_create()
            if tracker_type == 'MEDIANFLOW':
                tracker = cv2.TrackerMedianFlow_create()
           
     
        # Read video
        cap = cv2.VideoCapture("model_data/chaplin.mp4")
     
        # Exit if video not opened.
        if not cap.isOpened():
            print ("Could not open video")
            sys.exit()
     
        # Read first frame.
        ok, frame = cap.read()
        if not ok:
            print ('Cannot read video file')
            sys.exit()
         
        # Define an initial bounding box
        bbox = (287, 23, 86, 320)
     
        # Uncomment the line below to select a different bounding box
        bbox = cv2.selectROI(frame, False)
     
        # Initialize tracker with first frame and bounding box
        ok = tracker.init(frame, bbox)
     
        while True:
            # Read a new frame
            ok, frame = cap.read()
            if not ok:
                break
             
            # Start timer
            timer = cv2.getTickCount()
     
            # Update tracker
            ok, bbox = tracker.update(frame)
     
            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
     
            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            else :
                # Tracking failure
                cv2.putText(frame, "Tracking failure detected", (280,190), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
   
            # Display tracker type on frame
            cv2.putText(frame, tracker_type + " Tracker", (280,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255),3,
                                cv2.LINE_AA);
         
            # Display FPS on frame
            cv2.putText(frame, "FPS : " + str(int(fps)), (280,180), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 2);
     
            # Display result
            #cv2.imshow("Tracking", frame)
            nn = cv2.resize(frame, (781, 621))
            frame2 = cv2.cvtColor(nn, cv2.COLOR_BGR2RGB)
            h, w, ch = frame2.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frame2, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.label.setPixmap(pixmap)
     
            # Exit if ESC pressed
            k = cv2.waitKey(1) & 0xff
            if k == 27 : break
        cap.release()
        cv2.destroyAllWindows()
        self.comboBox.setCurrentIndex(0)
            
    def mil(self):
        global cap
        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
        tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW']
        tracker_type = tracker_types[1]
     
        if int(minor_ver) < 3:
            tracker = cv2.Tracker_create(tracker_type)
        else:
            if tracker_type == 'BOOSTING':
                tracker = cv2.TrackerBoosting_create()
            if tracker_type == 'MIL':
                tracker = cv2.TrackerMIL_create()
            if tracker_type == 'KCF':
                tracker = cv2.TrackerKCF_create()
            if tracker_type == 'TLD':
                tracker = cv2.TrackerTLD_create()
            if tracker_type == 'MEDIANFLOW':
                tracker = cv2.TrackerMedianFlow_create()
           
     
        # Read video
        cap = cv2.VideoCapture("model_data/chaplin.mp4")
     
        # Exit if video not opened.
        if not cap.isOpened():
            print ("Could not open video")
            sys.exit()
     
        # Read first frame.
        ok, frame = cap.read()
        if not ok:
            print ('Cannot read video file')
            sys.exit()
         
        # Define an initial bounding box
        bbox = (287, 23, 86, 320)
     
        # Uncomment the line below to select a different bounding box
        bbox = cv2.selectROI(frame, False)
     
        # Initialize tracker with first frame and bounding box
        ok = tracker.init(frame, bbox)
     
        while True:
            # Read a new frame
            ok, frame = cap.read()
            if not ok:
                break
             
            # Start timer
            timer = cv2.getTickCount()
     
            # Update tracker
            ok, bbox = tracker.update(frame)
     
            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
     
            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            else :
                # Tracking failure
                cv2.putText(frame, "Tracking failure detected", (280,190), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
     
            # Display tracker type on frame
            cv2.putText(frame, tracker_type + " Tracker", (280,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255),3,
                                cv2.LINE_AA);
         
            # Display FPS on frame
            cv2.putText(frame, "FPS : " + str(int(fps)), (280,180), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 2);
     
            # Display result
            #cv2.imshow("Tracking", frame)

            nn = cv2.resize(frame, (781, 621))
            frame2 = cv2.cvtColor(nn, cv2.COLOR_BGR2RGB)
            h, w, ch = frame2.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frame2, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.label.setPixmap(pixmap)
     
            # Exit if ESC pressed
            k = cv2.waitKey(1) & 0xff
            if k == 27 : break
        cap.release()
        cv2.destroyAllWindows()
        self.comboBox.setCurrentIndex(0)

    def kcf(self):
        global cap
        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
        tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW']
        tracker_type = tracker_types[2]
     
        if int(minor_ver) < 3:
            tracker = cv2.Tracker_create(tracker_type)
        else:
            if tracker_type == 'BOOSTING':
                tracker = cv2.TrackerBoosting_create()
            if tracker_type == 'MIL':
                tracker = cv2.TrackerMIL_create()
            if tracker_type == 'KCF':
                tracker = cv2.TrackerKCF_create()
            if tracker_type == 'TLD':
                tracker = cv2.TrackerTLD_create()
            if tracker_type == 'MEDIANFLOW':
                tracker = cv2.TrackerMedianFlow_create()
     
        # Read video
        cap = cv2.VideoCapture("model_data/chaplin.mp4")
     
        # Exit if video not opened.
        if not cap.isOpened():
            print ("Could not open video")
            sys.exit()
     
        # Read first frame.
        ok, frame = cap.read()
        if not ok:
            print ('Cannot read video file')
            sys.exit()
         
        # Define an initial bounding box
        bbox = (287, 23, 86, 320)
     
        # Uncomment the line below to select a different bounding box
        bbox = cv2.selectROI(frame, False)
     
        # Initialize tracker with first frame and bounding box
        ok = tracker.init(frame, bbox)
     
        while True:
            # Read a new frame
            ok, frame = cap.read()
            if not ok:
                break
             
            # Start timer
            timer = cv2.getTickCount()
     
            # Update tracker
            ok, bbox = tracker.update(frame)
     
            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
     
            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            else :
                # Tracking failure
                cv2.putText(frame, "Tracking failure detected", (280,190), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
     
            # Display tracker type on frame
            cv2.putText(frame, tracker_type + " Tracker", (280,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255),3,
                                cv2.LINE_AA);
         
            # Display FPS on frame
            cv2.putText(frame, "FPS : " + str(int(fps)), (280,180), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 2);
     
            # Display result
            #cv2.imshow("Tracking", frame)
            nn = cv2.resize(frame, (781, 621))
            frame2 = cv2.cvtColor(nn, cv2.COLOR_BGR2RGB)
            h, w, ch = frame2.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frame2, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.label.setPixmap(pixmap)
     
            # Exit if ESC pressed
            k = cv2.waitKey(1) & 0xff
            if k == 27 : break
        cap.release()
        cv2.destroyAllWindows()
        self.comboBox.setCurrentIndex(0)

    def tld(self):
        global cap
        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
        tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW']
        tracker_type = tracker_types[3]
     
        if int(minor_ver) < 3:
            tracker = cv2.Tracker_create(tracker_type)
        else:
            if tracker_type == 'BOOSTING':
                tracker = cv2.TrackerBoosting_create()
            if tracker_type == 'MIL':
                tracker = cv2.TrackerMIL_create()
            if tracker_type == 'KCF':
                tracker = cv2.TrackerKCF_create()
            if tracker_type == 'TLD':
                tracker = cv2.TrackerTLD_create()
            if tracker_type == 'MEDIANFLOW':
                tracker = cv2.TrackerMedianFlow_create()
    
     
        # Read video
        cap = cv2.VideoCapture("model_data/chaplin.mp4")
     
        # Exit if video not opened.
        if not cap.isOpened():
            print ("Could not open video")
            sys.exit()
     
        # Read first frame.
        ok, frame = cap.read()
        if not ok:
            print ('Cannot read video file')
            sys.exit()
         
        # Define an initial bounding box
        bbox = (287, 23, 86, 320)
     
        # Uncomment the line below to select a different bounding box
        bbox = cv2.selectROI(frame, False)
     
        # Initialize tracker with first frame and bounding box
        ok = tracker.init(frame, bbox)
     
        while True:
            # Read a new frame
            ok, frame = cap.read()
            if not ok:
                break
             
            # Start timer
            timer = cv2.getTickCount()
     
            # Update tracker
            ok, bbox = tracker.update(frame)
     
            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
     
            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            else :
                # Tracking failure
                cv2.putText(frame, "Tracking failure detected", (280,190), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
     
            # Display tracker type on frame
            cv2.putText(frame, tracker_type + " Tracker", (280,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255),3,
                                cv2.LINE_AA);
         
            # Display FPS on frame
            cv2.putText(frame, "FPS : " + str(int(fps)), (280,180), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 2);
     
            # Display result
            #cv2.imshow("Tracking", frame)
            nn = cv2.resize(frame, (781, 621))
            frame2 = cv2.cvtColor(nn, cv2.COLOR_BGR2RGB)
            h, w, ch = frame2.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frame2, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.label.setPixmap(pixmap)
     
            # Exit if ESC pressed
            k = cv2.waitKey(1) & 0xff
            if k == 27 : break
        cap.release()
        cv2.destroyAllWindows()
        self.comboBox.setCurrentIndex(0)
        
    def medianflow(self):
        global cap
        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
        tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW']
        tracker_type = tracker_types[4]
     
        if int(minor_ver) < 3:
            tracker = cv2.Tracker_create(tracker_type)
        else:
            if tracker_type == 'BOOSTING':
                tracker = cv2.TrackerBoosting_create()
            if tracker_type == 'MIL':
                tracker = cv2.TrackerMIL_create()
            if tracker_type == 'KCF':
                tracker = cv2.TrackerKCF_create()
            if tracker_type == 'TLD':
                tracker = cv2.TrackerTLD_create()
            if tracker_type == 'MEDIANFLOW':
                tracker = cv2.TrackerMedianFlow_create()

     
        # Read video
        cap = cv2.VideoCapture("model_data/chaplin.mp4")
     
        # Exit if video not opened.
        if not cap.isOpened():
            print ("Could not open video")
            sys.exit()
     
        # Read first frame.
        ok, frame = cap.read()
        if not ok:
            print ('Cannot read video file')
            sys.exit()
         
        # Define an initial bounding box
        bbox = (287, 23, 86, 320)
     
        # Uncomment the line below to select a different bounding box
        bbox = cv2.selectROI(frame, False)
     
        # Initialize tracker with first frame and bounding box
        ok = tracker.init(frame, bbox)
     
        while True:
            # Read a new frame
            ok, frame = cap.read()
            if not ok:
                break
             
            # Start timer
            timer = cv2.getTickCount()
     
            # Update tracker
            ok, bbox = tracker.update(frame)
     
            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
     
            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            else :
                # Tracking failure
                cv2.putText(frame, "Tracking failure detected", (280,190), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
     
            # Display tracker type on frame
            cv2.putText(frame, tracker_type + " Tracker", (280,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255),3,
                                cv2.LINE_AA);
         
            # Display FPS on frame
            cv2.putText(frame, "FPS : " + str(int(fps)), (280,180), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 2);
     
            # Display result
            #cv2.imshow("Tracking", frame)
            nn = cv2.resize(frame, (781, 621))
            frame2 = cv2.cvtColor(nn, cv2.COLOR_BGR2RGB)
            
            h, w, ch = frame2.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frame2, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.label.setPixmap(pixmap)
     
            # Exit if ESC pressed
            k = cv2.waitKey(1) & 0xff
            if k == 27 : break
        cap.release()
        cv2.destroyAllWindows()
        self.comboBox.setCurrentIndex(0)

    
   

    def yolo(self):
        global cap
        # Initialize the parameters
        confThreshold = 0.5  #Confidence threshold
        nmsThreshold = 0.4   #Non-maximum suppression threshold
        inpWidth = 416       #Width of network's input image
        inpHeight = 416      #Height of network's input image
                
        # Load names of classes
        classesFile = "model_data/deeptrack/coco_classes.txt"
        classes = None
        with open(classesFile, 'rt') as f:
            classes = f.read().rstrip('\n').split('\n')

        # Give the configuration and weight files for the model and load the network using them.
        modelConfiguration = "model_data/deeptrack/yolov2.cfg"
        modelWeights = "model_data/deeptrack/yolov2.weights"

        net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        # Get the names of the output layers
        def getOutputsNames(net):
            # Get the names of all the layers in the network
            layersNames = net.getLayerNames()
            # Get the names of the output layers, i.e. the layers with unconnected outputs
            return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        # Draw the predicted bounding box
        def drawPred(classId, conf, left, top, right, bottom):
            # Draw a bounding box.
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)
            
            label = '%.2f' % conf
                
            # Get the label for the class name and its confidence
            if classes:
                assert(classId < len(classes))
                label = '%s:%s' % (classes[classId], label)

            #Display the label at the top of the bounding box
            labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            top = max(top, labelSize[1])
            cv2.rectangle(frame, (left, top - round(1.5*labelSize[1])), (left + round(1.5*labelSize[0]), top + baseLine), (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0,0,0), 1)

        # Remove the bounding boxes with low confidence using non-maxima suppression
        def postprocess(frame, outs):
            frameHeight = frame.shape[0]
            frameWidth = frame.shape[1]

            # Scan through all the bounding boxes output from the network and keep only the
            # ones with high confidence scores. Assign the box's class label as the class with the highest score.
            classIds = []
            confidences = []
            boxes = []
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    classId = np.argmax(scores)
                    confidence = scores[classId]
                    if confidence > confThreshold:
                        center_x = int(detection[0] * frameWidth)
                        center_y = int(detection[1] * frameHeight)
                        width = int(detection[2] * frameWidth)
                        height = int(detection[3] * frameHeight)
                        left = int(center_x - width / 2)
                        top = int(center_y - height / 2)
                        classIds.append(classId)
                        confidences.append(float(confidence))
                        boxes.append([left, top, width, height])

            # Perform non maximum suppression to eliminate redundant overlapping boxes with
            # lower confidences.
            indices = cv2.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
            for i in indices:
                i = i[0]
                box = boxes[i]
                left = box[0]
                top = box[1]
                width = box[2]
                height = box[3]
                drawPred(classIds[i], confidences[i], left, top, left + width, top + height)

        # Process inputs
        #winName = 'Deep learning object detection in OpenCV'
        #cv2.namedWindow(winName, cv2.WINDOW_NORMAL)

       # outputFile = "/home/majeed/learnopencv/ObjectDetection-YOLO/yolo_out_py.avi"
        
        cap = cv2.VideoCapture(0)

        # Get the video writer initialized to save the output video
        #if (not args.image):
         #  vid_writer = cv2.VideoWriter(outputFile, cv2.VideoWriter_fourcc('M','J','P','G'), 30, (round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

        while cv2.waitKey(1) < 0:
            
            # get frame from the video
            hasFrame, frame = cap.read()
            
            # Stop the program if reached end of video
            if not hasFrame:
                #print("Done processing !!!")
                #print("Output file is stored as ", outputFile)
                cv2.waitKey(300)
                # Release device
                cap.release()
                break

            # Create a 4D blob from a frame.
            blob = cv2.dnn.blobFromImage(frame, 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop=False)

            # Sets the input to the network
            net.setInput(blob)

            # Runs the forward pass to get output of the output layers
            outs = net.forward(getOutputsNames(net))

            # Remove the bounding boxes with low confidence
            postprocess(frame, outs)

            # Put efficiency information. The function getPerfProfile returns the overall time for inference(t) and the timings for each of the layers(in layersTimes)
            t, _ = net.getPerfProfile()
            
            label = 'YOLO ; Inference time: %.2f ms' % (t * 1000.0 / cv2.getTickFrequency())
            cv2.putText(frame, label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3,
                                cv2.LINE_AA)
            cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Write the frame with the detection boxes

            
            
            nn = cv2.resize(frame, (781, 621))
            frame2 = cv2.cvtColor(nn, cv2.COLOR_BGR2RGB)
            h, w, ch = frame2.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frame2.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.label.setPixmap(pixmap)
    

    def ssd(self):
        global cap
        # Labels of Network.
        classNames = { 0: 'background',
            1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
            5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
            10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
            14: 'motorbike', 15: 'person', 16: 'pottedplant',
            17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor' }

        # Open video file or capture device. 
        #if args.video:
         #   cap = cv2.VideoCapture(args.video)
        #else:
        cap = cv2.VideoCapture(0)
        modelfile = "model_data/deeptrack/MobileNetSSD_deploy.caffemodel";
        txtfile = "model_data/deeptrack/MobileNetSSD_deploy.prototxt";
        #Load the Caffe model 
        net = cv2.dnn.readNetFromCaffe(txtfile, modelfile)

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            frame_resized = cv2.resize(frame,(300,300)) # resize frame for prediction

            # MobileNet requires fixed dimensions for input image(s)
            # so we have to ensure that it is resized to 300x300 pixels.
            # set a scale factor to image because network the objects has differents size. 
            # We perform a mean subtraction (127.5, 127.5, 127.5) to normalize the input;
            # after executing this command our "blob" now has the shape:
            # (1, 3, 300, 300)
            blob = cv2.dnn.blobFromImage(frame_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5), False)
            #Set to network the input blob 
            net.setInput(blob)
            #Prediction of network
            detections = net.forward()

            #Size of frame resize (300x300)
            cols = frame_resized.shape[1] 
            rows = frame_resized.shape[0]

            #For get the class and location of object detected, 
            # There is a fix index for class, location and confidence
            # value in @detections array .
            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2] #Confidence of prediction 
                if confidence > 0.2: # Filter prediction 
                    class_id = int(detections[0, 0, i, 1]) # Class label

                    # Object location 
                    xLeftBottom = int(detections[0, 0, i, 3] * cols) 
                    yLeftBottom = int(detections[0, 0, i, 4] * rows)
                    xRightTop   = int(detections[0, 0, i, 5] * cols)
                    yRightTop   = int(detections[0, 0, i, 6] * rows)
                    
                    # Factor for scale to original size of frame
                    heightFactor = frame.shape[0]/300.0  
                    widthFactor = frame.shape[1]/300.0 
                    # Scale object detection to frame
                    xLeftBottom = int(widthFactor * xLeftBottom) 
                    yLeftBottom = int(heightFactor * yLeftBottom)
                    xRightTop   = int(widthFactor * xRightTop)
                    yRightTop   = int(heightFactor * yRightTop)
                    # Draw location of object  
                    cv2.rectangle(frame, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop),
                                  (0, 255, 0))

                    # Draw label and confidence of prediction in frame resized
                    if class_id in classNames:
                        label = 'SSD:'+ classNames[class_id] + ": " + str(confidence)
                        labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

                        yLeftBottom = max(yLeftBottom, labelSize[1])
                        cv2.rectangle(frame, (xLeftBottom, yLeftBottom - labelSize[1]),
                                             (xLeftBottom + labelSize[0], yLeftBottom + baseLine),
                                             (255, 255, 255), cv2.FILLED)
                         
                        cv2.putText(frame, label, (xLeftBottom, yLeftBottom),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0),3,
                                cv2.LINE_AA)

                        #print(label) #print class and confidence

            #cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
            #cv2.imshow("frame", frame)
            nn = cv2.resize(frame, (781, 621))
            frame2 = cv2.cvtColor(nn, cv2.COLOR_BGR2RGB)
            h, w, ch = frame2.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frame2.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.label.setPixmap(pixmap)
        
            if cv2.waitKey(1) >= 0:  # Break with ESC 
                break

        cap.release()
        cv2.destroyAllWindows()



    def maskrcnn(self):
        global cap
        # Initialize the parameters
        confThreshold = 0.5  # Confidence threshold
        maskThreshold = 0.3  # Mask threshold

        
        # Draw the predicted bounding box, colorize and show the mask on the image
        def drawBox(frame, classId, conf, left, top, right, bottom, classMask):
            # Draw a bounding box.
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)
            
            # Print a label of class.
            label = '%.2f' % conf
            if classes:
                assert(classId < len(classes))
                label = '%s:%s' % (classes[classId], label)
            
            # Display the label at the top of the bounding box
            labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            top = max(top, labelSize[1])
            cv2.rectangle(frame, (left, top - round(1.5*labelSize[1])), (left + round(1.5*labelSize[0]), top + baseLine), (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 1)

            # Resize the mask, threshold, color and apply it on the image
            classMask = cv2.resize(classMask, (right - left + 1, bottom - top + 1))
            mask = (classMask > maskThreshold)
            roi = frame[top:bottom+1, left:right+1][mask]

            # color = colors[classId%len(colors)]
            # Comment the above line and uncomment the two lines below to generate different instance colors
            colorIndex = random.randint(0, len(colors)-1)
            color = colors[colorIndex]

            frame[top:bottom+1, left:right+1][mask] = ([0.3*color[0], 0.3*color[1], 0.3*color[2]] + 0.7 * roi).astype(np.uint8)

            # Draw the contours on the image
            mask = mask.astype(np.uint8)
            contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(frame[top:bottom+1, left:right+1], contours, -1, color, 3, cv2.LINE_8, hierarchy, 100)

        # For each frame, extract the bounding box and mask for each detected object
        def postprocess(boxes, masks):
            # Output size of masks is NxCxHxW where
            # N - number of detected boxes
            # C - number of classes (excluding background)
            # HxW - segmentation shape
            numClasses = masks.shape[1]
            numDetections = boxes.shape[2]

            frameH = frame.shape[0]
            frameW = frame.shape[1]

            for i in range(numDetections):
                box = boxes[0, 0, i]
                mask = masks[i]
                score = box[2]
                if score > confThreshold:
                    classId = int(box[1])
                    
                    # Extract the bounding box
                    left = int(frameW * box[3])
                    top = int(frameH * box[4])
                    right = int(frameW * box[5])
                    bottom = int(frameH * box[6])
                    
                    left = max(0, min(left, frameW - 1))
                    top = max(0, min(top, frameH - 1))
                    right = max(0, min(right, frameW - 1))
                    bottom = max(0, min(bottom, frameH - 1))
                    
                    # Extract the mask for the object
                    classMask = mask[classId]

                    # Draw bounding box, colorize and show the mask on the image
                    drawBox(frame, classId, score, left, top, right, bottom, classMask)


        # Load names of classes
        classesFile = "model_data/Mask-RCNN/mscoco_labels.names";
        classes = None
        with open(classesFile, 'rt') as f:
           classes = f.read().rstrip('\n').split('\n')

        # Give the textGraph and weight files for the model
        textGraph = "model_data/Mask-RCNN/mask_rcnn_inception_v2_coco_2018_01_28.pbtxt";
        modelWeights = "model_data/Mask-RCNN/mask_rcnn_inception_v2_coco_2018_01_28/frozen_inference_graph.pb";

        # Load the network
        net = cv2.dnn.readNetFromTensorflow(modelWeights, textGraph);
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        # Load the classes
        colorsFile = "model_data/Mask-RCNN/colors.txt";
        with open(colorsFile, 'rt') as f:
            colorsStr = f.read().rstrip('\n').split('\n')
        colors = [] #[0,0,0]
        for i in range(len(colorsStr)):
            rgb = colorsStr[i].split(' ')
            color = np.array([float(rgb[0]), float(rgb[1]), float(rgb[2])])
            colors.append(color)
        
            # Webcam input
        cap = cv2.VideoCapture(0)

        while cv2.waitKey(1) < 0:
            
            # Get frame from the video
            hasFrame, frame = cap.read()
            
            # Stop the program if reached end of video
            if not hasFrame:
                #print("Done processing !!!")
        
                cv2.waitKey(3000)
                break

            # Create a 4D blob from a frame.
            blob = cv2.dnn.blobFromImage(frame, swapRB=True, crop=False)

            # Set the input to the network
            net.setInput(blob)

            # Run the forward pass to get output from the output layers
            boxes, masks = net.forward(['detection_out_final', 'detection_masks'])

            # Extract the bounding box and mask for each of the detected objects
            postprocess(boxes, masks)

            # Put efficiency information.
            t, _ = net.getPerfProfile()
            label = 'Mask-RCNN, Inference time for a frame : %0.0f ms' % abs(t * 1000.0 / cv2.getTickFrequency())
            cv2.putText(frame, label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))

            nn = cv2.resize(frame, (781, 621))
            frame2 = cv2.cvtColor(nn, cv2.COLOR_BGR2RGB)
            h, w, ch = frame2.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frame2.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.label.setPixmap(pixmap)


    def drawPred1(self,frame, objects_detected):

            objects_list = list(objects_detected.keys())

            for object_, info in objects_detected.items():
                box = info[0]
                confidence = info[1]
                label = '%s: %.2f' % (object_, confidence)
                p1 = (int(box[0]), int(box[1]))
                p2 = (int(box[0] + box[2]), int(box[1] + box[3]))
                cv2.rectangle(frame, p1, p2, (0, 255, 0))
                left = int(box[0])
                top = int(box[1])
                labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                top = max(top, labelSize[1])
                cv2.rectangle(frame, (left, top - labelSize[1]), (left + labelSize[0], top + baseLine), (255, 255, 255), cv2.FILLED)
                cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))  
               

    def postprocess1(self,frame, out, threshold, classes, framework):

        frameHeight = frame.shape[0]
        frameWidth = frame.shape[1]
        objects_detected = dict()

        if framework == 'Caffe':
            # Network produces output blob with a shape 1x1xNx7 where N is a number of
            # detections and an every detection is a vector of values
            # [batchId, classId, confidence, left, top, right, bottom]
            for detection in out[0, 0]:
                confidence = detection[2]
                if confidence > threshold:
                    left = int(detection[3] * frameWidth)
                    top = int(detection[4] * frameHeight)
                    right = int(detection[5] * frameWidth)
                    bottom = int(detection[6] * frameHeight)
                    #classId = int(detection[1]) - 1  # Skip background label
                    
                    classId = int(detection[1])
                    i = 0
                    label = classes[classId]
                    label_with_num = str(label) + '_' + str(i)
                    while(True):
                        if label_with_num not in objects_detected.keys():
                            break
                        label_with_num = str(label) + '_' + str(i)
                        i = i+1
                    objects_detected[label_with_num] = [(int(left),int(top),int(right - left), int(bottom-top)),confidence] 
                    #print(label_with_num + ' at co-ordinates '+ str(objects_detected[label_with_num]))

        else:
            # Network produces output blob with a shape NxC where N is a number of
            # detected objects and C is a number of classes + 4 where the first 4
            # numbers are [center_x, center_y, width, height]
            for detection in out:
                confidences = detection[5:]
                classId = np.argmax(confidences)
                confidence = confidences[classId]
                if confidence > threshold:
                    center_x = int(detection[0] * frameWidth)
                    center_y = int(detection[1] * frameHeight)
                    width = int(detection[2] * frameWidth)
                    height = int(detection[3] * frameHeight)
                    left = center_x - (width / 2)
                    top = center_y - (height / 2)
                    
                    i = 0
                    label = classes[classId]
                    label_with_num = str(label) + '_' + str(i)
                    while(True):
                        if label_with_num not in objects_detected.keys():
                            break
                        label_with_num = str(label) + '_' + str(i)
                        i = i+1
                    objects_detected[label_with_num] = [(int(left),int(top),int(width),int(height)),confidence]
                    #print(label_with_num + ' at co-ordinates '+ str(objects_detected[label_with_num]))

        return objects_detected

    def intermediate_detections(self,stream, predictor, threshold, classes):
        
        
        _,frame = stream.read()
        predictions = predictor.predict(frame)
        objects_detected = self.postprocess1(frame, predictions, threshold, classes, predictor.framework)
            
        objects_list = list(objects_detected.keys())
        print('Tracking the following objects', objects_list)

        trackers_dict = dict()    
        #multi_tracker = cv.MultiTracker_create()

        if len(objects_list) > 0:
            
            trackers_dict = {key : cv2.TrackerKCF_create() for key in objects_list}
            for item in objects_list:
                trackers_dict[item].init(frame, objects_detected[item][0])
                
        return stream, objects_detected, objects_list, trackers_dict

    def yolokcf(self):
        global cap

        objects_detected = dict()

        """
        #tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
        #tracker_type = tracker_types[2]
        #tracker = None

        
        if tracker_type == 'BOOSTING':
            tracker = cv.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv.TrackerGOTURN_create()
        """
        model = "model_data/deeptrack/yolov2.weights"
        config = "model_data/deeptrack/yolov2.cfg"
        classes = "model_data/deeptrack/coco_classes.txt"
        predictor = object_detector(model, config)
        cap = cv2.VideoCapture(0)
        #window_name = "Tracking in progress"
        #cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        #cv2.setWindowProperty(window_name, cv2.WND_PROP_AUTOSIZE, cv2.WINDOW_AUTOSIZE)        
        #cv2.moveWindow(window_name,10,10)
        


        if classes:
            with open(classes, 'rt') as f:
                classes = f.read().rstrip('\n').split('\n')
        else:
            classes = list(np.arange(0,100))

        cap, objects_detected, objects_list, trackers_dict = self.intermediate_detections(cap, predictor, 0.35, classes)    

        while cap.isOpened():
        
            grabbed, frame = cap.read()

            if not grabbed:
                break

            timer = cv2.getTickCount()

            """
            #Did not use OpenCV's multitracker because of the restrivtive nature of its Python counterpart.
            #If one tracker in the multitracker fails, there's no way to find out which tracker failed.
            #There's no easy way to delete individual trackers in the multitracker object.
            #Even when multitracker fails,  bboxes will have old values, but 'ok' will be false
            
            #if len(objects_list) > 0:
                #ok, bboxes = multi_tracker.update(frame)
            #bboxes = multi_tracker.getObjects()
            #ok = multi_tracker.empty()
            """
            
            #print('Tracking - ',objects_list)

            if len(objects_detected) > 0:
                del_items = []
                for obj,tracker in trackers_dict.items():
                    ok, bbox = tracker.update(frame)
                    if ok:
                        objects_detected[obj][0] = bbox
                    else:
                        print('Failed to track ', obj)
                        del_items.append(obj) 
            
                for item in del_items:            
                    trackers_dict.pop(item)
                    objects_detected.pop(item)
                    
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

            if len(objects_detected) > 0:
                self.drawPred1(frame, objects_detected)
                # Display FPS on frame
                cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)

            else:
                cv2.putText(frame, 'Tracking Failure. Trying to detect more objects', (50,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
                stream, objects_detected, objects_list, trackers_dict = self.intermediate_detections(stream, predictor, 0.35, classes)   
                
            
            # Display result
            #If resolution is too big, resize the video
            #if frame.shape[1] > 1240:
             #   cv2.imshow(window_name, cv.resize(frame, (1240, 960)))
                
            #else:
             #   cv2.imshow(window_name, frame)
            nn = cv2.resize(frame, (781, 621))
            frame2 = cv2.cvtColor(nn, cv2.COLOR_BGR2RGB)
            h, w, ch = frame2.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frame2.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.label.setPixmap(pixmap)


            #Write to output file
            ##   out.write(frame)
            k = cv2.waitKey(1) & 0xff

            #Force detect new objects if 'q' is pressed
            if k == ord('q'):
                print('Refreshing. Detecting New objects')
                cv2.putText(frame, 'Refreshing. Detecting New objects', (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
                stream, objects_detected, objects_list, trackers_dict = self.intermediate_detections(stream, predictor, 0.35, classes)  
                
            # Exit if ESC pressed    
            if k == 27 : break 

        cap.release()
        #if args.output:
         #   out.release()
        cv2.destroyAllWindows()

        

    def ssdkcf(self):
        global cap

        objects_detected = dict()

        """
        #tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
        #tracker_type = tracker_types[2]
        #tracker = None

        
        if tracker_type == 'BOOSTING':
            tracker = cv.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv.TrackerGOTURN_create()
        """
        model = "model_data/deeptrack/MobileNetSSD_deploy.caffemodel"
        config = "model_data/deeptrack/MobileNetSSD_deploy.prototxt"
        classes = "model_data/deeptrack/MobileNet_classes.txt"
        predictor = object_detector(model, config)
        cap = cv2.VideoCapture(0)
        #window_name = "Tracking in progress"
        #cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        #cv2.setWindowProperty(window_name, cv2.WND_PROP_AUTOSIZE, cv2.WINDOW_AUTOSIZE)        
        #cv2.moveWindow(window_name,10,10)
        


        if classes:
            with open(classes, 'rt') as f:
                classes = f.read().rstrip('\n').split('\n')
        else:
            classes = list(np.arange(0,100))

        cap, objects_detected, objects_list, trackers_dict = self.intermediate_detections(cap, predictor, 0.35, classes)    

        while cap.isOpened():
        
            grabbed, frame = cap.read()

            if not grabbed:
                break

            timer = cv2.getTickCount()

            """
            #Did not use OpenCV's multitracker because of the restrivtive nature of its Python counterpart.
            #If one tracker in the multitracker fails, there's no way to find out which tracker failed.
            #There's no easy way to delete individual trackers in the multitracker object.
            #Even when multitracker fails,  bboxes will have old values, but 'ok' will be false
            
            #if len(objects_list) > 0:
                #ok, bboxes = multi_tracker.update(frame)
            #bboxes = multi_tracker.getObjects()
            #ok = multi_tracker.empty()
            """
            
            #print('Tracking - ',objects_list)

            if len(objects_detected) > 0:
                del_items = []
                for obj,tracker in trackers_dict.items():
                    ok, bbox = tracker.update(frame)
                    if ok:
                        objects_detected[obj][0] = bbox
                    else:
                        print('Failed to track ', obj)
                        del_items.append(obj) 
            
                for item in del_items:            
                    trackers_dict.pop(item)
                    objects_detected.pop(item)
                    
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

            if len(objects_detected) > 0:
                self.drawPred1(frame, objects_detected)
                # Display FPS on frame
                cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)

            else:
                cv2.putText(frame, 'Tracking Failure. Trying to detect more objects', (50,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
                stream, objects_detected, objects_list, trackers_dict = self.intermediate_detections(stream, predictor, 0.35, classes)   
                
            
            # Display result
            #If resolution is too big, resize the video
            #if frame.shape[1] > 1240:
             #   cv2.imshow(window_name, cv.resize(frame, (1240, 960)))
                
            #else:
             #   cv2.imshow(window_name, frame)
            nn = cv2.resize(frame, (781, 621))
            frame2 = cv2.cvtColor(nn, cv2.COLOR_BGR2RGB)
            h, w, ch = frame2.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frame2.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.label.setPixmap(pixmap)


            #Write to output file
            ##   out.write(frame)
            k = cv2.waitKey(1) & 0xff

            #Force detect new objects if 'q' is pressed
            if k == ord('q'):
                print('Refreshing. Detecting New objects')
                cv2.putText(frame, 'Refreshing. Detecting New objects', (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
                stream, objects_detected, objects_list, trackers_dict = self.intermediate_detections(stream, predictor, 0.35, classes)  
                
            # Exit if ESC pressed    
            if k == 27 : break 

        cap.release()
        #if args.output:
         #   out.release()
        cv2.destroyAllWindows()

         


    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

