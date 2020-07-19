from polls.models import Poll, Test, Question


def save_m2m_data(data):
    test_dict = {}
    quest_dict = {}

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
        question = Question(
            title=d['question'],
            true_answer=d['correctanswer'],
            option_a=d['answer-a'],
            option_b=d['answer-b'],
            option_c=d['answer-c']
        )

        question.save()
        test.question.add(question)


def get_related_id(obj):
    related_id = []
    for test in tests:
        if test in related_tests:
            related_id.append(test.id)
