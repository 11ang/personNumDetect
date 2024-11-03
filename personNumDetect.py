import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from ultralytics import YOLO
import cv2


class ImageSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #A simple Qt window with an image selected on the left and the image recognition result displayed on the right
        self.setGeometry(100, 100, 800, 600)


        main_layout = QHBoxLayout()


        left_layout = QVBoxLayout()

        self.image_label = QLabel()
        self.image_label.setFixedSize(600, 400)
        left_layout.addWidget(self.image_label)

        self.select_button = QPushButton('select Image')
        self.select_button.clicked.connect(self.selectImage)
        left_layout.addWidget(self.select_button)

        right_layout = QVBoxLayout()
        self.result_label = QLabel()
        right_layout.addWidget(self.result_label)


        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('person number detect')

    def selectImage(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "select Image", "", "Image Files (*.png *.jpg *.bmp)")
        if image_path:
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio))
            #This place introduces the model of yolov8, but you need to set up the yolov8 environment first
            model = YOLO('yolov8m.pt')
            detections = model.predict(image_path, classes=[0])
            boxes = detections[0].boxes #0 represents the person of the yolov8 model
            names = detections[0].names
            labels_num_dict = {}
            for box in boxes:
                cls_id = box.cls.cpu().detach().numpy()[0].astype(int)
                for key in names.keys():
                    if cls_id == key:
                        if names[key] in labels_num_dict:
                            labels_num_dict[names[key]] += 1
                        else:
                            labels_num_dict[names[key]] = 1

            if 'person' in labels_num_dict:
                person_count = labels_num_dict['person']
                self.result_label.setText(f"There are {person_count} people in the picture.")
            else:
                self.result_label.setText("No people are detected in the picture.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageSelector()
    ex.show()
    sys.exit(app.exec_())