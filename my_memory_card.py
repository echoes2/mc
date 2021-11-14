from random import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QButtonGroup, QWidget, QHBoxLayout,QVBoxLayout, QGroupBox,QLabel,QPushButton,QRadioButton
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = []
questions_list.append('Когда вышел первый альбом playboi carti', '14 апреля 2017', '12 марта 2020', '5 мая 2018', '30 февраля 2016')
questions_list.append('Какой стенд был у Юкако', 'echoes act 3' 'GER', 'Love Deluxe', 'Hierophant Green')
questions_list.append('Что было у Джони Джостара', 'ничего не было' ,'хамон', 'спин', 'все ответы верны')

app = QApplication([])

points = 0

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Что нужно для C moon.')

RadioGroupBox = QGroupBox("Варианты ответа")
rbtn_1 = QRadioButton('White snake, green baby')
rbtn_2 = QRadioButton('The world, left arm')
rbtn_3 = QRadioButton('requiem arrow')
rbtn_4 = QRadioButton('made in heven, Paradise')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Посмотрим дурак ты или нет')
lb_Correct = QLabel('ты дурак')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignCenter)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=Qt.AlignLeft)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line1.addWidget(points,alignment=Qt.AlignRight)
AnsGroupBox.hide() 

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    global ochko
    if answers[0].isChecked():
        ochko += 1
        tvoe_ochko.setText('Твои очки: ' + str(ochko))
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно ты ДУРАК')

def next_question():
    window.cur_question += 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)

def click_OK():
    if 'Ответить' == btn_OK.text():
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory card')
window.cur_question = -1

btn_OK.clicked.connect(click_OK)

next_question()
window.resize(600,400)
window.show()
app.exec()