# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'param_panel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1037, 890)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbSubjects = QtWidgets.QLabel(Dialog)
        self.lbSubjects.setObjectName("lbSubjects")
        self.verticalLayout_4.addWidget(self.lbSubjects)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pbSelectAllSubjects = QtWidgets.QPushButton(Dialog)
        self.pbSelectAllSubjects.setObjectName("pbSelectAllSubjects")
        self.horizontalLayout_3.addWidget(self.pbSelectAllSubjects)
        self.pbUnselectAllSubjects = QtWidgets.QPushButton(Dialog)
        self.pbUnselectAllSubjects.setObjectName("pbUnselectAllSubjects")
        self.horizontalLayout_3.addWidget(self.pbUnselectAllSubjects)
        self.pbReverseSubjectsSelection = QtWidgets.QPushButton(Dialog)
        self.pbReverseSubjectsSelection.setObjectName("pbReverseSubjectsSelection")
        self.horizontalLayout_3.addWidget(self.pbReverseSubjectsSelection)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.lwSubjects = QtWidgets.QListWidget(Dialog)
        self.lwSubjects.setObjectName("lwSubjects")
        self.verticalLayout_4.addWidget(self.lwSubjects)
        self.lbBehaviors = QtWidgets.QLabel(Dialog)
        self.lbBehaviors.setObjectName("lbBehaviors")
        self.verticalLayout_4.addWidget(self.lbBehaviors)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pbSelectAllBehaviors = QtWidgets.QPushButton(Dialog)
        self.pbSelectAllBehaviors.setObjectName("pbSelectAllBehaviors")
        self.horizontalLayout_4.addWidget(self.pbSelectAllBehaviors)
        self.pbUnselectAllBehaviors = QtWidgets.QPushButton(Dialog)
        self.pbUnselectAllBehaviors.setObjectName("pbUnselectAllBehaviors")
        self.horizontalLayout_4.addWidget(self.pbUnselectAllBehaviors)
        self.pbReverseBehaviorsSelection = QtWidgets.QPushButton(Dialog)
        self.pbReverseBehaviorsSelection.setObjectName("pbReverseBehaviorsSelection")
        self.horizontalLayout_4.addWidget(self.pbReverseBehaviorsSelection)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.lwBehaviors = QtWidgets.QListWidget(Dialog)
        self.lwBehaviors.setObjectName("lwBehaviors")
        self.verticalLayout_4.addWidget(self.lwBehaviors)
        self.cbIncludeModifiers = QtWidgets.QCheckBox(Dialog)
        self.cbIncludeModifiers.setObjectName("cbIncludeModifiers")
        self.verticalLayout_4.addWidget(self.cbIncludeModifiers)
        self.cbExcludeBehaviors = QtWidgets.QCheckBox(Dialog)
        self.cbExcludeBehaviors.setObjectName("cbExcludeBehaviors")
        self.verticalLayout_4.addWidget(self.cbExcludeBehaviors)
        self.frm_time = QtWidgets.QFrame(Dialog)
        self.frm_time.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_time.setObjectName("frm_time")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frm_time)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.rb_full = QtWidgets.QRadioButton(self.frm_time)
        self.rb_full.setChecked(True)
        self.rb_full.setObjectName("rb_full")
        self.horizontalLayout_5.addWidget(self.rb_full)
        self.rb_interval = QtWidgets.QRadioButton(self.frm_time)
        self.rb_interval.setObjectName("rb_interval")
        self.horizontalLayout_5.addWidget(self.rb_interval)
        self.rb_limit = QtWidgets.QRadioButton(self.frm_time)
        self.rb_limit.setObjectName("rb_limit")
        self.horizontalLayout_5.addWidget(self.rb_limit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.frm_time_interval = QtWidgets.QFrame(self.frm_time)
        self.frm_time_interval.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_time_interval.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_time_interval.setObjectName("frm_time_interval")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frm_time_interval)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frm_time_interval)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbStartTime = QtWidgets.QLabel(self.frm_time_interval)
        self.lbStartTime.setObjectName("lbStartTime")
        self.horizontalLayout.addWidget(self.lbStartTime)
        self.lbEndTime = QtWidgets.QLabel(self.frm_time_interval)
        self.lbEndTime.setObjectName("lbEndTime")
        self.horizontalLayout.addWidget(self.lbEndTime)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.frm_time_interval)
        self.verticalLayout_4.addWidget(self.frm_time)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pbCancel = QtWidgets.QPushButton(Dialog)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_2.addWidget(self.pbCancel)
        self.pbOK = QtWidgets.QPushButton(Dialog)
        self.pbOK.setObjectName("pbOK")
        self.horizontalLayout_2.addWidget(self.pbOK)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Parameters"))
        self.lbSubjects.setText(_translate("Dialog", "Subjects"))
        self.pbSelectAllSubjects.setText(_translate("Dialog", "Select all"))
        self.pbUnselectAllSubjects.setText(_translate("Dialog", "Unselect all"))
        self.pbReverseSubjectsSelection.setText(_translate("Dialog", "Reverse selection"))
        self.lbBehaviors.setText(_translate("Dialog", "Behaviors"))
        self.pbSelectAllBehaviors.setText(_translate("Dialog", "Select all"))
        self.pbUnselectAllBehaviors.setText(_translate("Dialog", "Unselect all"))
        self.pbReverseBehaviorsSelection.setText(_translate("Dialog", "Reverse selection"))
        self.cbIncludeModifiers.setText(_translate("Dialog", "Include modifiers"))
        self.cbExcludeBehaviors.setText(_translate("Dialog", "Exclude behaviors without events"))
        self.rb_full.setText(_translate("Dialog", "Full observation(s)"))
        self.rb_interval.setText(_translate("Dialog", "Limit to time interval"))
        self.rb_limit.setText(_translate("Dialog", "Limit to observed events"))
        self.label.setText(_translate("Dialog", "Time interval"))
        self.lbStartTime.setText(_translate("Dialog", "Start time"))
        self.lbEndTime.setText(_translate("Dialog", "End time"))
        self.pbCancel.setText(_translate("Dialog", "Cancel"))
        self.pbOK.setText(_translate("Dialog", "OK"))
