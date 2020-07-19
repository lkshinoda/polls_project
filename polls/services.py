from polls.models import Poll, Test, Question, Answer


class Counter:
    def __init__(self):
        self.true = 0
        self.false = 0
        self.total = 0

    def up_true(self):
        self.true += 1

    def up_false(self):
        self.false += 1

    def up_total(self):
        self.total += 1

    def percent_count(self):
        self.percent = round((self.true / self.total) * 100)



def save_m2m_data(data):
    test_dict = {}
    quest_dict = {}
    answer_dict = {}

    for key, value in data.items():
        if 'token' in key:
            continue
        if 'test' in key:
            test_dict[key] = value
        else:
            key, num_key = key.split('_')
            if num_key not in quest_dict:
                quest_dict[num_key] = {}
            quest_dict[num_key][key] = value

    test = Test(
        title=test_dict['test_title'],
        description=test_dict['test_description']
    )

    test.save()

    for i in quest_dict:
        d = quest_dict[i]
        question = Question(title=d['question'])
        question.save()

        question.answer.create(title=d['correctanswer'], is_true=True)
        question.answer.create(title=d['answer-a'])
        question.answer.create(title=d['answer-b'])
        question.answer.create(title=d['answer-c'])

        test.question.add(question)


def answer_handler(data):
    question_pool = {}
    counter = Counter()
    for key, value in data.items():
        if 'question' in key:
            question_id = int(key.split('_')[1])
            answer_id = int(value)
            question = Question.objects.get(id=question_id)
            current_answer = Answer.objects.get(id=answer_id)
            true_answer = get_true_answer(question)
            if current_answer.id == true_answer.id:
                question_pool[question] = {}
                result = {'choice': current_answer, 'correct': true_answer, 'status': True}
                question_pool[question] = result
                counter.up_true()
                counter.up_total()

            else:
                question_pool[question] = {}
                result = {'choice': current_answer, 'correct': true_answer, 'status': False}
                question_pool[question] = result
                counter.up_false()
                counter.up_total()

    percent = counter.percent_count()

    counter.true = counter.true * 10
    counter.total = counter.total * 10
    return question_pool, counter

def get_true_answer(question):
    answers = question.answer.all()
    for answer in answers:
        if answer.is_true:
            return answer